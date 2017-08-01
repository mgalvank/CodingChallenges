package com.sensorhound.calculator.Controller;

import com.sensorhound.calculator.Model.CalculatorModel;
import com.sensorhound.calculator.Service.CalculatorService;

import java.io.*;
import java.util.*;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/calculator")
public class CalculatorController {

	@Autowired 
	private CalculatorService calculatorService;
	
	
	@RequestMapping(method = RequestMethod.GET)
	public Collection<CalculatorModel> getAllResults(){
		return calculatorService.getAllResults();
	}
	
	
	@RequestMapping(value="/operation", method = RequestMethod.POST)
	public Collection<CalculatorModel> insertAdd(@RequestBody CalculatorModel c){
		int operand1 = c.getOperand1();
		int operand2 = c.getOperand2();
		String operation = c.getOperation();
		int result;
		if(operation.equals("add")){
			result = operand1 + operand2;
		}else if(operation.equals("sub")){
			result = operand1 - operand2;
		}else if (operation.equals("mul")){
			result = operand1 * operand2;
		}else {
			result = operand1 / operand2;
		}
		
		c.setResult(result);
		
		calculatorService.insertResult(c);
		
		return calculatorService.getAllResults();
		
	}
	
	
	


}

