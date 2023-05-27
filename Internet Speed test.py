import speedtest

def test_speed():
    st = speedtest.Speedtest()
    print("Loading server list...")
    st.get_servers()
    print("Choosing best server...")
    best_server = st.get_best_server()
    print(f"Found: {best_server['host']} located in {best_server['country']}")

    print("Performing download test...")
    download_speed = st.download()
    print(f"Download speed: {round(download_speed / 1_000_000, 2)} Mbps")

    print("Performing upload test...")
    upload_speed = st.upload()
    print(f"Upload speed: {round(upload_speed / 1_000_000, 2)} Mbps")

if __name__ == '__main__':
    test_speed()





