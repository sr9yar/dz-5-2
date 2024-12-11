from datetime import date


test_cases = [
    {
      "start_date": "2022-01-01",
      "end_date": "2022-01-03",
    },
    {
      "start_date": "2022-01-03",
      "end_date": "2022-01-01",
    },
    {
      "start_date": "2022-02-30",
      "end_date": "2022-02-31",
    },
  ]



def date_range(start: str, end: str):
  start_date = None
  end_date = None

  try:
    start_date = date.fromisoformat(start)
    end_date = date.fromisoformat(end)
  except:
    return []

  if start_date > end_date:
    return []
  
  for i in range(start_date.toordinal(), end_date.toordinal() + 1):
    yield date.fromordinal(i)



def main() -> None:
  for case in test_cases:
    line = ', '.join([str(d) for d in date_range(case["start_date"], case["end_date"])])
    print(f"[{line}]")



main()


