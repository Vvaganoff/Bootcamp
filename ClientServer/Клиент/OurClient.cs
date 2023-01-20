using System.Net.Sockets;
using System.Text;

namespace Client
{
    class OurClient
    {
        private TcpClient client;
        private StreamWriter sWriter; 
        public OurClient()
        {
            client = new TcpClient("127.0.0.1", 555);
            sWriter = new StreamWriter(client.GetStream(), Encoding.UTF8);
            
            HandleCommunication();
        }
        public void HandleCommunication()
        {
            StreamReader sReader = new StreamReader(client.GetStream(), Encoding.UTF8);
            while (true)
            {
                Console.Write("> ");
                string message = Console.ReadLine();
                sWriter.WriteLine(message);
                sWriter.Flush();

                string incomingMessage = sReader.ReadLine();
                Console.WriteLine($"Сообщение от сервера: {incomingMessage}");
            }
        }

    }

    
}
