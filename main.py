from Kursov import sample, data
size=data['X'].count()
print("Sample size: "+str(size))

min=data['X'].min()
print("Min of sample: "+str(min))

max=data['X'].max()
print("Max of sample: "+str(max))

print("Scope(PA3MAX) of sample: "+str(max-min))

average=data['X'].sum()/size
print("Sample average: "+str(round(average,2)))

dispersion_sum=0
for i in sample:
    dispersion_sum+=(i-average)**2
shift_dispersion=dispersion_sum/size
print("Sample shift dispersion: "+str(round(shift_dispersion,2)))

not_shift_dispersion=size/(size-1)*shift_dispersion
print("Sample not shift dispersion: "+str(round(not_shift_dispersion,2)))

variance=shift_dispersion**0.5
print("Стандартное отклонение выборки: "+str(round(variance,2)))

dispersion_sum=0
for i in sample:
    dispersion_sum+=(i-average)**3
skewness=dispersion_sum/(size*(variance**3))
print("Коэффициент асимметрии: "+str(round(skewness,2)))

sample.sort()
if (size-1)%2==0:
    mediana=sample[(size-1)/2+1]
else:
    mediana=(sample[(size-1)//2+1]+sample[(size-1)//2+2])/2
print("Медиана: "+str(mediana))









