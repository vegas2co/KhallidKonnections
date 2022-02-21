<?php declare(strict_types=1);
use PHPUnit\Framework\TestCase;

  final class StackTest extends TestCase {

    public function addToJob()  {
    
      if($this->request->is('put')) {
        $this->Validation->isEmpty('id', $this->request->getData('id'));
        $errors = $this->Validation->validationErrors();

        if (count($errors) > 0) {
          $response = ['status'=>400, 'code'=>'validation_error', 'msg'=>__('We encounter the validation error'), 'err'=>$errors];
          $this->Common->responseSend($response);
        }
                  
        $job = $this->Jobs->get($this->request->getData('id'), ['where'=>['company_code'=>$this->loggedUser['company_code']]]);

        if (isset($job) && !empty($job)) {            
          $data = [];
          $data['add_to_job'] = 2;
          $patchEntity = $this->Jobs->patchEntity($job, $data);

          if(empty($patchEntity->hasErrors())){
            if ($this->Jobs->save($patchEntity)) {
                $response = ['status'=>200, 'code'=>'success', 'msg'=>__('Job has been created successfully for requested service')];
                $this->Common->responseSend($response);
            }
            $response = ['status'=>400, 'code'=>'database_error', 'msg'=>__('Something went wrong while creating the job for requested service')];
            $this->Common->responseSend($response);
          }

          $error = $this->checkErrors($patchEntity->getErrors());
          $response = ['status'=>400, 'code'=>'database_error', 'msg'=>$error];
          $this->Common->responseSend($response);
        }

        $response = ['status'=>400, 'code'=>'requested_service_not_exist', 'msg'=>__('Requested service does not exist')];
        $this->Common->responseSend($response);
      }
    }
  }
?>