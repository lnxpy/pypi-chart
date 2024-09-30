from string import Template


MERMAID_CHART = Template(
    """---
configs:
   look: handDrawn
---
xychart-beta
   title "$title"
   x-axis "Date" $dates
   y-axis "Downloads" $least_download --> $most_download
   bar $rates"""
)


data = """
{
  "data": [
    {
      "category": "with_mirrors",
      "date": "2024-03-10",
      "downloads": 13
    },
    {
      "category": "with_mirrors",
      "date": "2024-03-11",
      "downloads": 3
    },
    {
      "category": "with_mirrors",
      "date": "2024-03-12",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-03-13",
      "downloads": 8
    },
    {
      "category": "with_mirrors",
      "date": "2024-03-14",
      "downloads": 7
    },
    {
      "category": "with_mirrors",
      "date": "2024-03-15",
      "downloads": 7
    },
    {
      "category": "with_mirrors",
      "date": "2024-03-17",
      "downloads": 6
    },
    {
      "category": "with_mirrors",
      "date": "2024-03-19",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-03-20",
      "downloads": 5
    },
    {
      "category": "with_mirrors",
      "date": "2024-03-22",
      "downloads": 14
    },
    {
      "category": "with_mirrors",
      "date": "2024-03-23",
      "downloads": 19
    },
    {
      "category": "with_mirrors",
      "date": "2024-03-25",
      "downloads": 5
    },
    {
      "category": "with_mirrors",
      "date": "2024-03-26",
      "downloads": 13
    },
    {
      "category": "with_mirrors",
      "date": "2024-03-28",
      "downloads": 21
    },
    {
      "category": "with_mirrors",
      "date": "2024-03-29",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-03-31",
      "downloads": 3
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-02",
      "downloads": 6
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-03",
      "downloads": 11
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-04",
      "downloads": 2
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-05",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-06",
      "downloads": 6
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-07",
      "downloads": 6
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-08",
      "downloads": 20
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-13",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-15",
      "downloads": 6
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-16",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-17",
      "downloads": 6
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-18",
      "downloads": 7
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-19",
      "downloads": 9
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-20",
      "downloads": 12
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-21",
      "downloads": 13
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-22",
      "downloads": 5
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-23",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-24",
      "downloads": 4
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-25",
      "downloads": 3
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-28",
      "downloads": 6
    },
    {
      "category": "with_mirrors",
      "date": "2024-04-30",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-01",
      "downloads": 7
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-02",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-03",
      "downloads": 6
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-04",
      "downloads": 7
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-05",
      "downloads": 2
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-06",
      "downloads": 6
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-08",
      "downloads": 6
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-09",
      "downloads": 4
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-10",
      "downloads": 6
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-11",
      "downloads": 8
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-12",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-13",
      "downloads": 6
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-15",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-16",
      "downloads": 19
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-18",
      "downloads": 8
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-19",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-20",
      "downloads": 6
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-21",
      "downloads": 6
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-22",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-23",
      "downloads": 7
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-24",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-25",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-27",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-30",
      "downloads": 5
    },
    {
      "category": "with_mirrors",
      "date": "2024-05-31",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-01",
      "downloads": 8
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-02",
      "downloads": 6
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-03",
      "downloads": 4
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-06",
      "downloads": 148
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-07",
      "downloads": 25
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-08",
      "downloads": 12
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-09",
      "downloads": 11
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-10",
      "downloads": 37
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-11",
      "downloads": 240
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-12",
      "downloads": 150
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-13",
      "downloads": 27
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-14",
      "downloads": 61
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-15",
      "downloads": 18
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-16",
      "downloads": 24
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-17",
      "downloads": 10
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-18",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-21",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-22",
      "downloads": 12
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-23",
      "downloads": 4
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-24",
      "downloads": 33
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-25",
      "downloads": 4
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-26",
      "downloads": 12
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-27",
      "downloads": 6
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-29",
      "downloads": 27
    },
    {
      "category": "with_mirrors",
      "date": "2024-06-30",
      "downloads": 30
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-01",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-02",
      "downloads": 20
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-03",
      "downloads": 36
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-04",
      "downloads": 13
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-05",
      "downloads": 12
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-06",
      "downloads": 35
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-07",
      "downloads": 17
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-08",
      "downloads": 9
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-10",
      "downloads": 33
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-11",
      "downloads": 26
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-12",
      "downloads": 12
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-13",
      "downloads": 30
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-14",
      "downloads": 12
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-15",
      "downloads": 6
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-16",
      "downloads": 9
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-17",
      "downloads": 9
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-18",
      "downloads": 20
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-19",
      "downloads": 16
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-20",
      "downloads": 20
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-21",
      "downloads": 23
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-22",
      "downloads": 7
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-23",
      "downloads": 19
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-24",
      "downloads": 2
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-25",
      "downloads": 29
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-26",
      "downloads": 24
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-27",
      "downloads": 25
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-30",
      "downloads": 33
    },
    {
      "category": "with_mirrors",
      "date": "2024-07-31",
      "downloads": 21
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-01",
      "downloads": 29
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-02",
      "downloads": 28
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-03",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-04",
      "downloads": 7
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-06",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-07",
      "downloads": 4
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-08",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-09",
      "downloads": 10
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-10",
      "downloads": 3
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-11",
      "downloads": 12
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-12",
      "downloads": 20
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-13",
      "downloads": 8
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-14",
      "downloads": 3
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-15",
      "downloads": 3
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-16",
      "downloads": 12
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-17",
      "downloads": 39
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-18",
      "downloads": 22
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-19",
      "downloads": 6
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-20",
      "downloads": 4
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-21",
      "downloads": 2
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-22",
      "downloads": 1
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-23",
      "downloads": 150
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-24",
      "downloads": 62
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-25",
      "downloads": 44
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-26",
      "downloads": 18
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-27",
      "downloads": 16
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-28",
      "downloads": 13
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-29",
      "downloads": 23
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-30",
      "downloads": 36
    },
    {
      "category": "with_mirrors",
      "date": "2024-08-31",
      "downloads": 15
    },
    {
      "category": "with_mirrors",
      "date": "2024-09-01",
      "downloads": 3
    },
    {
      "category": "with_mirrors",
      "date": "2024-09-02",
      "downloads": 33
    },
    {
      "category": "with_mirrors",
      "date": "2024-09-03",
      "downloads": 19
    },
    {
      "category": "with_mirrors",
      "date": "2024-09-04",
      "downloads": 35
    },
    {
      "category": "with_mirrors",
      "date": "2024-09-05",
      "downloads": 2
    },
    {
      "category": "without_mirrors",
      "date": "2024-03-12",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-03-13",
      "downloads": 2
    },
    {
      "category": "without_mirrors",
      "date": "2024-03-14",
      "downloads": 5
    },
    {
      "category": "without_mirrors",
      "date": "2024-03-23",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-03-26",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-03-29",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-04-04",
      "downloads": 2
    },
    {
      "category": "without_mirrors",
      "date": "2024-04-13",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-04-16",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-04-17",
      "downloads": 6
    },
    {
      "category": "without_mirrors",
      "date": "2024-04-18",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-04-19",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-04-23",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-04-24",
      "downloads": 3
    },
    {
      "category": "without_mirrors",
      "date": "2024-04-25",
      "downloads": 3
    },
    {
      "category": "without_mirrors",
      "date": "2024-04-30",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-05-01",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-05-02",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-05-04",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-05-12",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-05-13",
      "downloads": 6
    },
    {
      "category": "without_mirrors",
      "date": "2024-05-15",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-05-22",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-05-23",
      "downloads": 7
    },
    {
      "category": "without_mirrors",
      "date": "2024-05-24",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-05-25",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-05-31",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-06-01",
      "downloads": 2
    },
    {
      "category": "without_mirrors",
      "date": "2024-06-03",
      "downloads": 2
    },
    {
      "category": "without_mirrors",
      "date": "2024-06-06",
      "downloads": 53
    },
    {
      "category": "without_mirrors",
      "date": "2024-06-07",
      "downloads": 10
    },
    {
      "category": "without_mirrors",
      "date": "2024-06-09",
      "downloads": 2
    },
    {
      "category": "without_mirrors",
      "date": "2024-06-10",
      "downloads": 33
    },
    {
      "category": "without_mirrors",
      "date": "2024-06-11",
      "downloads": 129
    },
    {
      "category": "without_mirrors",
      "date": "2024-06-12",
      "downloads": 38
    },
    {
      "category": "without_mirrors",
      "date": "2024-06-13",
      "downloads": 18
    },
    {
      "category": "without_mirrors",
      "date": "2024-06-14",
      "downloads": 11
    },
    {
      "category": "without_mirrors",
      "date": "2024-06-15",
      "downloads": 2
    },
    {
      "category": "without_mirrors",
      "date": "2024-06-16",
      "downloads": 7
    },
    {
      "category": "without_mirrors",
      "date": "2024-06-17",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-06-21",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-06-23",
      "downloads": 2
    },
    {
      "category": "without_mirrors",
      "date": "2024-06-24",
      "downloads": 3
    },
    {
      "category": "without_mirrors",
      "date": "2024-06-25",
      "downloads": 2
    },
    {
      "category": "without_mirrors",
      "date": "2024-06-29",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-06-30",
      "downloads": 7
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-01",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-02",
      "downloads": 2
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-03",
      "downloads": 3
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-04",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-05",
      "downloads": 12
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-06",
      "downloads": 2
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-07",
      "downloads": 2
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-08",
      "downloads": 2
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-10",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-16",
      "downloads": 3
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-17",
      "downloads": 3
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-18",
      "downloads": 5
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-20",
      "downloads": 2
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-21",
      "downloads": 7
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-22",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-23",
      "downloads": 7
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-24",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-26",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-27",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-30",
      "downloads": 17
    },
    {
      "category": "without_mirrors",
      "date": "2024-07-31",
      "downloads": 9
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-02",
      "downloads": 3
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-03",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-04",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-06",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-07",
      "downloads": 4
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-08",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-09",
      "downloads": 3
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-10",
      "downloads": 3
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-11",
      "downloads": 6
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-12",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-13",
      "downloads": 8
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-15",
      "downloads": 3
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-17",
      "downloads": 15
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-18",
      "downloads": 22
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-20",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-21",
      "downloads": 2
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-22",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-23",
      "downloads": 49
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-24",
      "downloads": 24
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-25",
      "downloads": 26
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-26",
      "downloads": 10
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-27",
      "downloads": 14
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-28",
      "downloads": 13
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-29",
      "downloads": 17
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-30",
      "downloads": 8
    },
    {
      "category": "without_mirrors",
      "date": "2024-08-31",
      "downloads": 5
    },
    {
      "category": "without_mirrors",
      "date": "2024-09-01",
      "downloads": 1
    },
    {
      "category": "without_mirrors",
      "date": "2024-09-02",
      "downloads": 9
    },
    {
      "category": "without_mirrors",
      "date": "2024-09-03",
      "downloads": 6
    },
    {
      "category": "without_mirrors",
      "date": "2024-09-04",
      "downloads": 5
    },
    {
      "category": "without_mirrors",
      "date": "2024-09-05",
      "downloads": 2
    }
  ],
  "package": "hey-mindsdb",
  "type": "overall_downloads"
}
"""
