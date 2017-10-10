//: Playground - noun: a place where people can play

import UIKit
import Foundation
import PlaygroundSupport

let url:URL = URL(string: "http://40.71.188.243:9999/api/v1_0")!
let session = URLSession.shared

let imageURL = "IMG_6913.JPG"

var request = URLRequest(url: url)
request.httpMethod = "PUT"
request.cachePolicy = NSURLRequest.CachePolicy.reloadIgnoringCacheData

let paramString = "image=" + imageURL
request.httpBody = paramString.data(using: String.Encoding.utf8)

let task = session.dataTask(with: request as URLRequest) {
    (
    data, response, error) in
    
    guard let data = data else {
        print(error)
        return
    }
    
    let dataString =  String(data: data, encoding: String.Encoding.utf8)
    print(dataString)
    
}

task.resume()

PlaygroundPage.current.needsIndefiniteExecution = true
