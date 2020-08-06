class ZhihuTopicMongoPipeline(object):
    """话题发kafka后, 新话题存MongoDB 用于统计"""

    def __init__(self):
        self.mongo_db = ZmtPicArtRW(MONGO_TYPE)

    def process_item(self, item, spider):
        if not item or item.get('item_type') != "question" or item.get('is_new') == 0:  # 只存新的话题
            return item
        # 修改created_time 时间类型 mongo备查ISODate("2012-11-02T07:58:51.718Z")
        item['created_time'] = timestamp_to_otherStyleTime(item['created_time'],
                                                           True) if 'created_time' in item else datetime.now()
        item['publish_time_date'] = timestamp_to_otherStyleTime(item['publish_time'],
                                                                True) if 'publish_time' in item else None
        self.mongo_db.insert_article(item)
        return item