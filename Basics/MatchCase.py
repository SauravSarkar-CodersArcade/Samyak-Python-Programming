server_code = 200

match server_code:
    case 200:
        print('Good request')
    case 500:
        print('Server Error')
    case 404:
        print('Bad request. Not Found')
    case default:
        print('Invalid Request')