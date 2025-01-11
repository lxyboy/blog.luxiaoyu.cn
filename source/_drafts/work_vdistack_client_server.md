vdistack client server

### LOGIN PACKAGE

#### REQUEST

|| *Type* || *Description* ||
|| ULONG || uuid length ||
|| STR || uuid ||
|| ULONG || mac length ||
|| STR || mac data ||

#### RESPONSE

|| *Type* || *Description* ||
|| ULONG || result ||
|| ULONG || error msg length ||
|| STR || error msg ||