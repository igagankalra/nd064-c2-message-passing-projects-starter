import event_coordinates_pb2
import event_coordinates_pb2_grpc
import grpc

# Simulates user device sending coordinates to gRPC

print("Sending coordinates......")

channel = grpc.insecure_channel("127.0.0.1:30003")
stub = event_coordinates_pb2_grpc.EventCoordinatesServiceStub(channel)

# Update this with desired payload
user_loc = event_coordinates_pb2.EventCoordinatesMessage(
    userId=2,
    latitude=-10,
    longitude=39
)

user_loc_1 = event_coordinates_pb2.EventCoordinatesMessage(
    userId=8,
    latitude=-10,
    longitude=40
)

response_1 = stub.Create(user_loc)
response_2 = stub.Create(user_loc_1)

print(user_loc, user_loc_1)
