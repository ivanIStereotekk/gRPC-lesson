import grpc
from concurrent import futures
import calc_pb2
import calc_pb2_grpc

class CalcServicer(calc_pb2_grpc.CalcServicer):
    def Add(self, request, context):
        result = request.val_one + request.val_two
        return calc_pb2.AddResponse(result=result)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calc_pb2_grpc.add_CalcServicer_to_server(CalcServicer(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    
    
if __name__ == '__main__':
    serve()