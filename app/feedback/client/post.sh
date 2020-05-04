curl \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{ "process": "back_end","request": {"param1": "upsert","param2": [{"service": "curl app","title": "post from curl app","detail": "curl app detail"}]}}' \
    http://localhost:5000/feedback/api
