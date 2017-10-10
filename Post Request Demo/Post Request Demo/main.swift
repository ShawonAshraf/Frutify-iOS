//
//  main.swift
//  Post Request Demo
//
//  Created by Shawon Ashraf on 10/10/17.
//  Copyright © 2017 Shawon Ashraf. All rights reserved.
//

import Foundation

let serverUrl = URL(string: "http://40.71.188.243:9999/api/v1_0")
//print("server hosted @\(serverUrl!)")

let imageFilePath = "IMG_6913.JPG"

let task = URLSession.shared.dataTask(with: serverUrl!) { (data, response, error) in
    if let data = data,
        let html = String(data: data, encoding: String.Encoding.utf8) {
        print(html)
    }
}

task.resume()
