import grpc
import calc_pb2
import calc_pb2_grpc

def run(val_one,val_two):
    with grpc.insecure_channel('localhost:50051') as conn:
        stub = calc_pb2_grpc.CalcStub(conn)
        response = stub.Add(calc_pb2.AddRequest(val_one=val_one,val_two=val_two)) 
        print(f"|>> gRPC Response is : {response.result}")
        
if __name__ == '__main__':
    val_one = int(input("Type Numbers Bro ! :"))
    val_two = int(input("Type Numbers Bro ! :"))
    run(val_one,val_two)