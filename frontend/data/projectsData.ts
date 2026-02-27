export const projects = [
  {
    slug: "etl-migration",
    title: "Enterprise ETL Migration",
    description:
      "Migrated legacy ETL pipelines to modern AWS Glue architecture improving performance and maintainability.",
    tech: ["AWS Glue", "PySpark", "S3", "Lambda"],
    year: "2024",
    imageUrl:
      "https://images.unsplash.com/photo-1558494949-ef010cbdcc31",
    problem:
      "Legacy pipelines were running on outdated runtime versions and had performance bottlenecks.",
    architecture:
      "S3 → AWS Glue 4 → Transform (PySpark) → RDS → Reporting",
    impact:
      "Reduced runtime by 27% and improved job stability across environments.",
    role:
      "Designed migration strategy, upgraded runtime, optimized transformations and testing.",
    lessons:
      "Backward compatibility planning and incremental rollout reduces risk."
  },
  {
    slug: "consumer-data-sync",
    title: "Consumer Data Sync Engine",
    description:
      "Built backend logic for consistent data updates across consumer-facing systems.",
    tech: ["Python", "SQL", "AWS Lambda", "DocumentDB"],
    year: "2023",
    imageUrl:
      "https://images.unsplash.com/photo-1508780709619-79562169bc64",
    problem:
      "Data inconsistencies between services caused reporting mismatches.",
    architecture:
      "API → Lambda → Validation Layer → DocumentDB",
    impact:
      "Improved data accuracy and reduced reconciliation effort.",
    role:
      "Designed update logic, implemented validation rules and DB consistency checks.",
    lessons:
      "Strong data contracts are critical in distributed systems."
  },
  {
    slug: "consumer-data-sync1",
    title: "Consumer Data Sync Engine1",
    description:
      "Built backend logic for consistent data updates across consumer-facing systems.",
    tech: ["Python", "SQL", "AWS Lambda", "DocumentDB"],
    year: "2023",
    imageUrl:
      "https://images.unsplash.com/photo-1508780709619-79562169bc64",
    problem:
      "Data inconsistencies between services caused reporting mismatches.",
    architecture:
      "API → Lambda → Validation Layer → DocumentDB",
    impact:
      "Improved data accuracy and reduced reconciliation effort.",
    role:
      "Designed update logic, implemented validation rules and DB consistency checks.",
    lessons:
      "Strong data contracts are critical in distributed systems."
  }
];