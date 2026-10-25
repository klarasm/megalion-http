from typing import Any

from .auth import Auth

class Battery:
    """A Megalion Battery (ESS)"""

    def __init__(self, sn: str, auth: Auth) -> None:
        """Initialize the battery"""
        self.device_sn = sn
        self.auth = auth

    async def async_update(self) -> None:
        response = await self.auth.request("get", f"system/stationDevice/list?sn={self.device_sn}")
        response.raise_for_status()
        raw_data = await response.json()
        self.raw_data = raw_data['rows'][0]
        response = await self.auth.request("get", f"system/deviceLatestData/getLatestDataTable?sn={self.device_sn}")
        response.raise_for_status()
        raw_detail = await response.json()
        self.raw_detail = raw_detail['data']
        response = await self.auth.request("get", f"system/deviceLatestData/getCellVoltages?sn={self.device_sn}")
        response.raise_for_status()
        raw_voltages = await response.json()
        self.raw_voltages = raw_voltages['data']
        response = await self.auth.request("get", f"system/deviceLatestData/getCellTemperatures?sn={self.device_sn}")
        response.raise_for_status()
        raw_temperatures = await response.json()
        self.raw_temperatures = raw_temperatures['data']

    @property
    def batchName(self) -> str:
        return self.raw_data['batchName']

    @property
    def batteryRatedEnergy(self) -> float:
        return self.raw_data['batteryRatedEnergy']

    @property
    def batteryTemperature(self) -> float:
        return self.raw_data['batteryTemperature']

    @property
    def chargeStatus(self) -> str:
        return self.raw_data['chargeStatus']

    @property
    def createBy(self) -> str:
        return self.raw_data['createBy']

    @property
    def createTime(self) -> str:
        return self.raw_data['createTime']

    @property
    def createTimeTimezone(self) -> str:
        return self.raw_data['createTimeTimezone']

    @property
    def current(self) -> float:
        return self.raw_data['current']

    @property
    def dayCharge(self) -> float:
        return self.raw_data['dayCharge']

    @property
    def dayDischarge(self) -> float:
        return self.raw_data['dayDischarge']

    @property
    def deviceId(self) -> int:
        return self.raw_data['deviceId']

    @property
    def deviceModel(self) -> str:
        return self.raw_data['deviceModel']

    @property
    def deviceName(self) -> str:
        return self.raw_data['deviceName']

    @property
    def deviceStatus(self) -> str:
        return self.raw_data['deviceStatus']

    @property
    def deviceType(self) -> str:
        return self.raw_data['deviceType']

    @property
    def deviceTypeStr(self) -> str:
        return self.raw_data['deviceTypeStr']

    @property
    def dynamicLinkedDeviceSn(self) -> str:
        return self.raw_data['dynamicLinkedDeviceSn']

    @property
    def inverterBrand(self) -> str:
        return self.raw_data['inverterBrand']

    @property
    def lastOfflineTimeUtc(self) -> str:
        return self.raw_data['lastOfflineTimeUtc']

    @property
    def lastOnlineTimeUtc(self) -> str:
        return self.raw_data['lastOnlineTimeUtc']

    @property
    def realtimePower(self) -> float:
        return self.raw_data['realtimePower']

    @property
    def sn(self) -> str:
        return self.raw_data['sn']

    @property
    def soc(self) -> float:
        return self.raw_data['soc']

    @property
    def staticLinkedDeviceSn(self) -> str:
        return self.raw_data['staticLinkedDeviceSn']

    @property
    def totalCharge(self) -> float:
        return self.raw_data['totalCharge']

    @property
    def totalDischarge(self) -> float:
        return self.raw_data['totalDischarge']

    @property
    def userId(self) -> str:
        return self.raw_data['userId']

    @property
    def voltage(self) -> float:
        return self.raw_data['voltage']

    @property
    def cellVoltages(self) -> list[int]:
        return self.raw_voltages['cellVoltages']

    @property
    def cellTemperatures(self) -> list[int]:
        return self.raw_temperatures['cellTemperatures']
