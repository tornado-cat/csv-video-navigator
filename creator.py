import csv
import os

def append_to_csv(csv_path, fieldnames, rows):
    folder = os.path.dirname(csv_path)
    if folder:
        os.makedirs(folder, exist_ok=True)

    file_exists = os.path.isfile(csv_path)
    is_empty = (not file_exists) or os.path.getsize(csv_path) == 0

    with open(csv_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if is_empty:
            writer.writeheader()
        for row in rows:
            writer.writerow(row)

if __name__ == "__main__":
    path = "videos.csv"
    cols = ["url"]
    yeni_kayitlar = [
        {"url": "https://files2.heygen.ai/aws_pacific/avatar_tmp/3fef605076384742b9e2c3cb7db49a2c/e449e45d4d964cadb54d4d0a66a35bdd.mp4?Expires=1761296972&Signature=VDgf-oG-1dQwtnYHdigiBJb-sIicB66hrjqmdWYZCXs6L8N1Z8uk9Awys~zgzsc2Vpcb8DBnjAromgv8OVP3qpKKlXIeFxufNkc255UvYgAM4-mcf1QRGrgtfQDYd8JLuHu78bPwGU6d~VFUa5kv9whr-dFL~eI0-YR3D25E6vVWoNs-yPecnGcHgf0zMNdqQcT49zHqjoSFMd1GNEKGC-knZhtijmx0O-UQ5SpdG66y84mV06dGWh-ofXXJR45DvHGTEoSvLpswnwsPBD44jUAdEd87CquiySG~taFBnSY72MVppA0S1jV5YCEOV9mZtbwEBsj4sB7b40uXxo7FIA__&Key-Pair-Id=K38HBHX5LX3X2H"},
    ]
    append_to_csv(path, cols, yeni_kayitlar)
    print("✅ Kayıtlar eklendi:", path)
