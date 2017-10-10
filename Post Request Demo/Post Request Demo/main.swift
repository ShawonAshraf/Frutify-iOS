//
//  main.swift
//  Post Request Demo
//
//  Created by Shawon Ashraf on 10/10/17.
//  Copyright © 2017 Shawon Ashraf. All rights reserved.
//

import Foundation

let serverUrl = URL(string: "http://40.71.188.243:9999/api/v1_0")
let imageFilePath = "IMG_6913.JPG"
var urlRequest = URLRequest(url: serverUrl!)

var ret:Data = "".data(using: String.Encoding.utf8)!

urlRequest.httpMethod = "PUT"
urlRequest.httpBody = "image: \(imageFilePath)".data(using: String.Encoding.utf8)


let task = URLSession.shared.dataTask(with: serverUrl!) {
    (data, response, error) in
    guard let _ = data else {
        print(error!)
        return
    }
    
    print(response!)
//    ret = response!
}
task.resume()

//print(ret)

