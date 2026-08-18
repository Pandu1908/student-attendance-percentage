total = int(input("Enter total students: "))
present = int(input("Enter present students: "))

absent = total - present
percentage = (present / total) * 100

print("👨‍🎓 Present:", present)
print("❌ Absent:", absent)
print("📊 Attendance:", round(percentage, 2), "%")

if percentage < 75:
    print("⚠️ Attendance is below 75%.")
else:
    print("✅ Attendance is good.")
