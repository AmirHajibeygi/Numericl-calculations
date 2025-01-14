clc
clear
disp("****************In the name of God******************")
disp("please enter Data to start calculation process")
n=(input("please enter the dimension of matrix..."));
matrix_cofficient=zeros(n);
for i=1:n
    for j=1:n
        matrix_cofficient(i,j)=(input("please enter the array..."));
    end
end
matrix_cofficient_real=matrix_cofficient;
disp(matrix_cofficient)
matrix_constants=zeros(n,1);
for o=1:n
    for s=1
        matrix_constants(o,s)=(input("please enter the array..."));
    end
end
matrix_constant_second=matrix_constants;
matrix_gues=zeros(n,1);
for d=1:n
    matrix_gues(d,1)=(input("please enter the array...."));
end
X=matrix_cofficient;
matrix_gues_second=matrix_gues;
for e=1:n
    for y=2:n
        if matrix_cofficient(e,e)==0
            v=matrix_cofficient(:,e);
            matrix_cofficient(:,e)=matrix_cofficient(:,y);
            matrix_cofficient(:,y)=v;
        else
            break
        end
    end
end
disp(matrix_cofficient)
matrix_new=horzcat(matrix_cofficient,matrix_constants);
for g=1:n
    for p=g+1:n
        matrix_new(p,g:end)=(-matrix_new(p,g)/matrix_new(g,g))*matrix_new(g,g:end)+matrix_new(p,g:end);
    end
end
disp(matrix_new)
%%Now we should calculate determinant
sam=1;
for w=1:n
    sam=matrix_new(w,w)*sam;
end
disp("Determinant is:"+sam)
if sam~=0
    disp("We have answers because determinant isnt equal to zero...")
else
    disp("We have not answers...")
end
x=matrix_gues;
x(n)=matrix_new(n,n+1)/matrix_new(n,n);
if sam~=0
    for t=n-1:-1:1
       x(t)=matrix_constants(t,1);
       for h=t+1:-1:n
           x(t)=x(t)-matrix_new(t,h)*x(h);
       end
       x(t)=x(t)/matrix_new(t,t);
    end
end
disp(x)
answer=zeros(n,2*n);
percentage=zeros(n,n);
h=zeros(n,1);
q=0;
vc=0;
s = 0;
summ_group=zeros(n,1);
answer_list=zeros(n,2);
for f=1:2
    for aa=1:n
        for t=1:n
            if t~=aa
                s=matrix_cofficient(aa,t)*matrix_gues(t)+s;
            end
        end
        h(aa,1)=(matrix_constants(aa,1)/matrix_cofficient(aa,aa))-(s/matrix_cofficient(aa,aa));
        q=q+2;
        for u=0.1:0.1:2
            vc=vc+1;
            b=u*h(aa,1)+(1-u)*matrix_gues(aa);
            answer(vc,q-1)=b;
            answer(vc,q)=u;
        end
    %now we should calculate errors
        for kj=1:length(answer)
            percentage(kj,aa)=abs((((answer(kj,2*aa-1)-x(aa))/x(aa))*100));
        end
        if vc~=0
            vc=0;
        end
        if s~=0
            s=0;
        end
    end
    summ=0;
    %now sum errors
    if q~=0
        q=0;
    end
    for fg=1:length(percentage)
         for kh=1:n
             summ=percentage(fg,kh)+summ;
         end
         summ_group(fg,1)=summ;
         if summ~=0
             summ=0;
         end
     end
     for i=1:length(summ_group)
          if summ_group(i)==min(summ_group)
              for y=1:length(matrix_gues)
                  matrix_gues(y,1)=answer(i,2*y-1);
              end
          end
      end
      for po=1:n
          answer_list(po,f)=matrix_gues(po,1);
      end
end
    %Now we show the answers to user
    for j=1:2
        for k=1:n
     %Now we should use "formatspec" function to show answers better
            formatSpec="x(%d) for step %d= %d \n";
            fprintf(formatSpec,k,j,answer_list(k,j))
        end
    end
for j=1:2
     if percentage(1,j)==sort(percentage(1,j))
         disp("error:your gues is unsuitable for this case.please enter new gues:"+matrix_gues_second(j))
     end
 end