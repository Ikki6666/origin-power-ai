import logging

import requests

from dify_plugin import ModelProvider
from dify_plugin.errors.model import CredentialsValidateFailedError

logger = logging.getLogger(__name__)


class OriginPowerAIProvider(ModelProvider):
    def validate_provider_credentials(self, credentials: dict) -> None:
        """Validate provider credentials by listing models from the gateway.

        A cheap GET /models call is enough: a 2xx proves both reachability and
        the Bearer key, without spending tokens on a chat completion.
        """
        endpoint_url = (credentials.get("endpoint_url") or "").strip().rstrip("/")
        if not endpoint_url:
            raise CredentialsValidateFailedError("Missing endpoint_url in credentials")

        api_key = (credentials.get("api_key") or "").strip()

        try:
            response = requests.get(
                f"{endpoint_url}/models",
                headers={"Authorization": f"Bearer {api_key}"} if api_key else {},
                timeout=(10, 60),
            )
        except Exception as ex:
            raise CredentialsValidateFailedError(
                f"Failed to reach the gateway at {endpoint_url}: {ex}"
            ) from ex

        if response.status_code in (401, 403):
            raise CredentialsValidateFailedError(
                "API Key rejected by the gateway (HTTP %d). Check the key." % response.status_code
            )
        if response.status_code == 404:
            raise CredentialsValidateFailedError(
                "GET /models not found (HTTP 404). Make sure the Base URL includes "
                "the version prefix, e.g. https://host/v1"
            )
        if response.status_code != 200:
            raise CredentialsValidateFailedError(
                f"Gateway responded with HTTP {response.status_code}: {response.text[:300]}"
            )
