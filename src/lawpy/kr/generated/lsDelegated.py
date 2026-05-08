"""Hand-crafted client for target=lsDelegated (위임법령).
The response has deeply nested, variable structure (dict-or-list) not
suitable for auto-generation. Uses field_validator to normalize.
"""
# ruff: noqa: N802, E501
from __future__ import annotations

from lawpy.kr.base import KoreanBaseClient
from lawpy.kr.generated._models_generated import LsdelegatedDetail


class GeneratedLsdelegatedClient(KoreanBaseClient):
    """Client for target=lsDelegated (위임법령).

    Returns structured nested models reflecting the actual API response.
    """

    def get_lsDelegated_detail(
        self,
        id: str | None = None,
        mst: str | None = None,
    ) -> LsdelegatedDetail:
        """위임법령 조회.

        Args:
            id: 법령 ID (ID 또는 MST 중 하나는 반드시 입력)
            mst: 법령 마스터 번호 (법령테이블의 lsi_seq 값)

        Returns:
            LsdelegatedDetail with nested 법령정보 and 위임조문정보.
        """
        if id is None and mst is None:
            msg = "Either id or mst must be provided for target lsDelegated"
            raise ValueError(msg)
        params: dict = {"target": "lsDelegated", "type": "JSON"}
        if id is not None:
            params["ID"] = id
        if mst is not None:
            params["MST"] = mst
        response = self._make_request(self.SERVICE_URL, params=params)
        data = self._parse_json_response(response, target="lsDelegated")
        root = data.get("lsDelegated", {})
        beopryeong = root.get("법령", {})
        return LsdelegatedDetail.model_validate(beopryeong)


__all__ = ["GeneratedLsdelegatedClient"]
