from .auth import Auth, AuthError
from .battery import Battery
from .user import User

class MegalionHubAPI:
    def __init__(self, auth: Auth) -> None:
        self.auth = auth

    async def async_get_user(self) -> User:
        user = User(self.auth)
        await user.async_update()
        return user

    async def async_get_batteries(self) -> list[Battery]:
        response = await self.auth.request("get", f"system/stationDevice/list")
        response.raise_for_status()
        raw_data = await response.json()
        if raw_data['code'] != 200:
            raise MegalionHubError(str(raw_data))
        batteries = []
        for device in raw_data['rows']:
            if device['deviceType'] == "ENERGY_STORAGE_EQUIPMENT":
                battery = Battery(device['sn'], self.auth)
                batteries.append(battery)
                await battery.async_update()
        return batteries

class MegalionHubError(Exception):
    pass
