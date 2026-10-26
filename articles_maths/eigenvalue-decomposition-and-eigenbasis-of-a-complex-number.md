# __Eigenvalue Decomposition and Eigenbasis of a Complex Number__

## Introduction

The complex algebra $\mathbb{C}=\mathbb{R}[i]/(i^2+1)$ is a field, so an element of $\mathbb{C}$ alone cannot be split into two idempotents: the only idempotents of a field are $0$ and $1$. The splitting appears after complexification. The algebra

$$
A_{\mathbb{C}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}
$$

is a two-dimensional complex algebra isomorphic to $\mathbb{C}\oplus\mathbb{C}$, and in it every complex number has a two-term spectral decomposition. Off the real axis the decomposition is unique, the two spectral idempotents are the two minimal idempotents of $A_{\mathbb{C}}$, and the eigenvectors are proportional to the two idempotents themselves.

This article constructs that decomposition. It gives the eigenbasis $(1,-i),(1,i)$ of the regular representation, the diagonal form of the Cayley matrix, the idempotents $e_\pm$ and the isomorphism $A_{\mathbb{C}}\cong\mathbb{C}\oplus\mathbb{C}$, the degenerate case of the real axis, the matrix picture and the relation to the polar decomposition. It is the companion of *Spectral Regularity and Degeneracy in the Complex Algebra*, which proves the criterion $b\neq0$, and of *The Three Sectors of the Complex Algebra*, which counts the cells.

**Conventions.** The element is $z=t+bi$ with $t,b\in\mathbb{R}$, the conjugation is $\bar z=t-bi$, the modulus squared is $|z|^2=z\bar z=t^2+b^2$, and the modulus is $|z|=\sqrt{t^2+b^2}$. The regular representation is $L_z(v)=zv$ on $\mathbb{C}$, with matrix $A=\begin{pmatrix}t&-b\\ b&t\end{pmatrix}=tI+bJ$, $J^2=-I$, in the basis $1,i$. The complexification is $V_{\mathbb{C}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$, with scalars acting on the first factor. The companion articles write the same element $Q=q+iq'$ and the same norm $\langle Q\rangle_*=Q\bar Q$; the translation is $t=q$, $b=q'$, $|z|^2=\langle Q\rangle_*$. The eigenvalue criterion, the discriminant and semisimplicity are those of *Spectral Regularity and Degeneracy in the Complex Algebra*; the polar decomposition is *Modulus–Unit Polar Decomposition of Complex Numbers*.

## The Eigenbasis Off the Real Axis

**Theorem (the eigenvectors).** Let $b\neq0$ and $\lambda_\pm=t\pm ib$. Then

$$
v_+=\begin{pmatrix}1\\ -i\end{pmatrix},\qquad v_-=\begin{pmatrix}1\\ i\end{pmatrix}
$$

satisfy $Av_+=\lambda_+v_+$ and $Av_-=\lambda_-v_-$, and the pair $(v_+,v_-)$ is a complex basis of $V_{\mathbb{C}}$.

*Proof.* For $v_+$, the first component of $Av_+$ is $t+(-b)(-i)=t+bi=\lambda_+$, and the second is $b+t(-i)=b-ti=-i(t+bi)=\lambda_+(-i)$. The computation for $v_-$ is the same with $i$ replaced by $-i$. The determinant of the matrix of the two vectors is $i+i=2i\neq0$, so they form a basis.

**Corollary (the diagonal form).** Let

$$
P=\begin{pmatrix}1&1\\ -i&i\end{pmatrix},\qquad P^{-1}=\frac{1}{2i}\begin{pmatrix}i&-1\\ i&1\end{pmatrix}.
$$

Then

$$
P^{-1}AP=\begin{pmatrix}\lambda_+&0\\ 0&\lambda_-\end{pmatrix}.
$$

*Proof.* The columns of $P$ are the eigenvectors, so $AP=PD$ with $D=\operatorname{diag}(\lambda_+,\lambda_-)$; multiplying by $P^{-1}$ gives the display. The inverse is verified by $P^{-1}P=I$.

**Remark (one eigenbasis for every non-real element).** The matrix is $A=tI+bJ$. The eigenvectors are the eigenvectors of $J$, which do not depend on $t$, on $b$ or on the sign of $b$. Every element off the real axis therefore has the same eigenbasis, and the eigenbasis is the basis of the complexified algebra supplied by its two minimal idempotents. This is the exact analogue of the two standard idempotents of the split-complex algebra, which are also independent of the element; the difference is that they exist only after complexification.

**Remark (no real eigenbasis off the axis).** If $b\neq0$ the eigenvalues $t\pm ib$ are not real, so $A$ has no real eigenvector: a real eigenvector would have a real eigenvalue. The diagonal form is complex, and the passage from the real basis to the eigenbasis is a complex change of coordinates. On the real axis the eigenvalues are real and every real basis is an eigenbasis.

## The Spectral Idempotents

**Definition (the complexified algebra and its generator).** Let

$$
\iota=1\otimes i\in A_{\mathbb{C}},\qquad \iota^2=-1.
$$

The element $\iota$ is the algebra generator of the second factor. The scalar $i$ of the complex structure is $i\otimes1$; it is a different element of $A_{\mathbb{C}}$, and both square to $-1$. Put

$$
e_+=\frac{1}{2}\left(1-i\iota\right),\qquad e_-=\frac{1}{2}\left(1+i\iota\right).
$$

**Proposition (the idempotents).** The elements $e_+,e_-$ satisfy

$$
e_+^2=e_+,\qquad e_-^2=e_-,\qquad e_+e_-=e_-e_+=0,\qquad e_++e_-=1,
$$

and $\iota=i(e_+-e_-)$.

*Proof.* Since $(i\iota)^2=i^2\iota^2=1$, one has $e_+^2=\frac14(1-2i\iota+1)=e_+$, and the computation for $e_-$ is the same with $i$ replaced by $-i$. The product is $e_+e_-=\frac14(1-(i\iota)^2)=0$, and the sum is $1$. Finally $e_+-e_-=-i\iota$, so $i(e_+-e_-)=\iota$.

**Theorem (the splitting of the complexified algebra).** The map

$$
\phi:A_{\mathbb{C}}\longrightarrow\mathbb{C}\oplus\mathbb{C},\qquad \phi(a\otimes\alpha)=(a\alpha,a\bar\alpha)
$$

is an isomorphism of rings, with inverse $(u,v)\mapsto\frac{u+v}{2}\otimes1+\frac{u-v}{2i}\otimes i$. It sends

$$
\phi(e_+)=(1,0),\qquad \phi(e_-)=(0,1),\qquad \phi(1\otimes z)=(z,\bar z).
$$

*Proof.* Multiplicativity is $\phi((a\otimes\alpha)(b\otimes\beta))=(ab\alpha\beta,ab\bar\alpha\bar\beta)=\phi(a\otimes\alpha)\phi(b\otimes\beta)$. The inverse is checked by $(a+ci,a-ci)=(u,v)$ with $a=(u+v)/2$ and $c=(u-v)/(2i)$. For $e_+$, one has $i\iota=i\otimes i\mapsto(-1,1)$, so $e_+\mapsto\frac12((1,1)-(-1,1))=(1,0)$, and similarly $e_-\mapsto(0,1)$. For $1\otimes z$ with $z=t+bi$, the image is $(z,\bar z)$.

**Theorem (the spectral decomposition).** For $z=t+bi$ with $b\neq0$,

$$
z\,e_+=\lambda_+e_+,\qquad z\,e_-=\lambda_-e_-,\qquad z=\lambda_+e_++\lambda_-e_-,
$$

with $\lambda_\pm=t\pm ib$. The decomposition is unique.

*Proof.* Under $\phi$, the element $z$ is $(z,\bar z)$ and $e_+$ is $(1,0)$, so $z e_+$ is $(z,0)=\lambda_+(1,0)=\lambda_+e_+$. Similarly $z e_-$ is $(0,\bar z)=\lambda_-(0,1)=\lambda_-e_-$. Adding gives $(z,\bar z)$, which is the image of $z$. For uniqueness, two decompositions $z=\lambda_+e_++\lambda_-e_-=\mu_+e_++\mu_-e_-$ with $\lambda_+\neq\lambda_-$ give $(\lambda_+-\mu_+)e_+=(\mu_--\lambda_-)e_-$; the two sides lie in complementary direct summands, so both vanish and the coefficients agree.

**Corollary (the spectral projectors).** The left multiplications $L_{e_+}$ and $L_{e_-}$ are the spectral projectors of $L_z$:

$$
L_{e_+}+L_{e_-}=\mathrm{id},\qquad L_{e_+}L_{e_-}=0,\qquad L_z=\lambda_+L_{e_+}+\lambda_-L_{e_-}.
$$

In the eigenbasis $(v_+,v_-)$ their matrices are $\operatorname{diag}(1,0)$ and $\operatorname{diag}(0,1)$.

*Proof.* The identities are the idempotent identities of the proposition, read under left multiplication; the last is the spectral decomposition. In the eigenbasis, $L_{e_+}$ fixes $e_+$ and kills $e_-$, and $e_\pm=\frac12v_\pm$.

**Corollary (the Lagrange form).** In matrices,

$$
E_+=\frac{A-\lambda_-I}{\lambda_+-\lambda_-}=\frac12\begin{pmatrix}1&i\\ -i&1\end{pmatrix},\qquad E_-=\frac{A-\lambda_+I}{\lambda_--\lambda_+}=\frac12\begin{pmatrix}1&-i\\ i&1\end{pmatrix},
$$

and $E_\pm$ are the matrices of $L_{e_\pm}$ in the complex basis $1,\iota$ of $V_{\mathbb{C}}$.

*Proof.* Substituting $A=tI+bJ$, $\lambda_\pm=t\pm ib$ gives the displays; the identification with $L_{e_\pm}$ is the previous corollary.

**Remark (uniqueness and dependence).** The idempotents $e_\pm$ are unique because the eigenvalues are distinct. They do not depend on $z$: they are the two minimal idempotents of the complexified algebra, and every non-real element is a complex linear combination of them. This is the sense in which the complex case is simpler than the biquaternion case, where the spectral idempotents depend on the element and are not unique on the degenerate cone.

## The Degenerate Case

**Proposition (the real axis).** Let $b=0$ and $z=t$. Then $A=tI$, the spectrum is the singleton $\{t\}$, every non-zero vector of $V_{\mathbb{C}}$ is an eigenvector, and every basis is an eigenbasis. The two-term writing

$$
z=t\,e_++t\,e_-
$$

holds but has equal coefficients; it does not separate the two terms, and the choice of splitting is not unique. The canonical spectral decomposition is the one-term writing $z=t\cdot1$. The Lagrange formulas are undefined, because $\lambda_+-\lambda_-=0$.

*Proof.* With $b=0$, $A=tI$ and $\lambda_+=\lambda_-=t$. The identity $z=t(e_++e_-)$ is the decomposition of the unit. Every idempotent $e$ satisfies $ze=te$, so every idempotent is spectral and the two-term decomposition can be made with any complementary pair. The Lagrange denominators vanish.

**Remark (the projectors degenerate).** On the real axis $E_\pm$ still satisfy $AE_\pm=tE_\pm$, but they are not the spectral projector of $A$: the spectral projector is $I$, and $E_++E_-=I$ is a non-unique splitting of it. The one-term decomposition is the only one that uses no choice of idempotent.

## The Matrix Picture

**Proposition (normality and the orthogonal factor).** For every $z$,

$$
A^{\mathsf{T}}A=AA^{\mathsf{T}}=(t^2+b^2)I=|z|^2I,
$$

so $A$ is normal. If $z\neq0$, then $A/|z|$ is orthogonal with determinant $+1$, that is, a rotation.

*Proof.* $A^{\mathsf{T}}=tI-bJ$, so $A^{\mathsf{T}}A=(tI-bJ)(tI+bJ)=t^2I-b^2J^2=(t^2+b^2)I$; the product in the other order is the same because $A$ and $A^{\mathsf{T}}$ commute. The determinant is $t^2+b^2=|z|^2$, so $\det(A/|z|)=1$, and orthogonality is $A^{\mathsf{T}}A=|z|^2I$.

**Remark.** For $z\neq0$, the matrices $A$ are the conformal matrices $tI+bJ$: each is a positive scalar times a rotation. The eigenbasis $(v_+,v_-)$ is orthogonal, with squared Hermitian norm $2$, so the diagonal form is unitary, as normality requires.

## The Relation to the Polar Decomposition

**Theorem (the polar reading).** Let $z\neq0$, $r=|z|$ and $u=z/r$. Then $z=ru$, $|u|=1$, and

$$
A=rR_\theta,\qquad R_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix},\qquad \cos\theta=\frac{t}{r},\quad \sin\theta=\frac{b}{r}.
$$

The eigenvalues are $\lambda_\pm=re^{\pm i\theta}$, and $u$ has eigenvalues $e^{\pm i\theta}$.

*Proof.* The modulus is $r=\sqrt{t^2+b^2}$ and $u=(t+bi)/r=\cos\theta+i\sin\theta$ with the displayed cosine and sine. The matrix is $r(\cos\theta I+\sin\theta J)=rR_\theta$. Its eigenvalues are $r$ times those of $R_\theta$, namely $re^{\pm i\theta}$, and $u$ is the scalar $\cos\theta+i\sin\theta$.

**Corollary (the polar factors in the eigenbasis).** In the basis $(v_+,v_-)$,

$$
L_z=\operatorname{diag}\left(re^{i\theta},re^{-i\theta}\right),\qquad L_u=\operatorname{diag}\left(e^{i\theta},e^{-i\theta}\right).
$$

The eigenbasis diagonalises the scale and the rotation at once, and it is the same basis for every nonzero element.

*Proof.* The eigenvalues of $L_z$ are $\lambda_\pm=re^{\pm i\theta}$ and those of $L_u$ are $e^{\pm i\theta}$; the eigenvectors are $v_\pm$ in both cases.

**Corollary (the spectral condition in polar form).** For $z\neq0$, the following are equivalent: $b\neq0$; $\sin\theta\neq0$; $\theta\notin\pi\mathbb{Z}$; $u\neq\pm1$; the two eigenvalues of $L_u$ are distinct.

*Proof.* $b=r\sin\theta$ and $r>0$, so $b\neq0$ is $\sin\theta\neq0$; this is $\theta\notin\pi\mathbb{Z}$, which is $u=e^{i\theta}\neq\pm1$. The eigenvalues $e^{\pm i\theta}$ coincide exactly when $e^{2i\theta}=1$, that is, at $\theta\in\pi\mathbb{Z}$.

**Remark (the two real points of the unit circle).** The polar form shows that the spectral degeneration of a unit is exactly its coincidence with one of the two real units $\pm1$. The doubly regular points of the unit circle are the other points, on which $\theta$ is not a multiple of $\pi$ and the two eigenvalues $e^{\pm i\theta}$ are distinct. *Relations between the Modulus and Spectral Regularity and Degeneracy* develops this comparison.

## Summary

The complex algebra is a field, and its complexification $A_{\mathbb{C}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$ is the algebra in which the eigenvalue decomposition lives. Off the real axis, $z=t+bi$ with $b\neq0$ has the distinct eigenvalues $\lambda_\pm=t\pm ib$, the eigenvectors $v_+=(1,-i)$ and $v_-=(1,i)$, and the diagonal form $P^{-1}AP=\operatorname{diag}(\lambda_+,\lambda_-)$ with $P$ the matrix of the two eigenvectors. The same eigenbasis serves every non-real element, because it is the eigenbasis of $J$.

The spectral idempotents are

$$
e_+=\frac12(1-i\iota),\qquad e_-=\frac12(1+i\iota),\qquad \iota=1\otimes i.
$$

They are the two minimal idempotents of $A_{\mathbb{C}}$, they satisfy $e_+^2=e_+$, $e_-^2=e_-$, $e_+e_-=0$, $e_++e_-=1$, and they give the decomposition $z=\lambda_+e_++\lambda_-e_-$. Under the isomorphism $\phi(a\otimes\alpha)=(a\alpha,a\bar\alpha)$ they are the two standard idempotents $(1,0)$ and $(0,1)$ of $\mathbb{C}\oplus\mathbb{C}$, and $z$ is $(z,\bar z)$. The left multiplications $L_{e_\pm}$ are the spectral projectors, with matrices $E_\pm=(A-\lambda_\mp I)/(\lambda_\pm-\lambda_\mp)$.

On the real axis the two eigenvalues coalesce at $t$. The operator is $tI$, every vector is an eigenvector, every basis is an eigenbasis, and the two-term writing has equal coefficients; the choice of splitting is not unique. The canonical decomposition is the one-term $z=t\cdot1$, and the spectral projector is $I$.

The matrix $A=tI+bJ$ is normal, $A^{\mathsf{T}}A=|z|^2I$, and, for $z\neq0$, $A/|z|$ is a rotation. The polar decomposition $z=ru$ reads $A=rR_\theta$ with $r=|z|$ and $u=e^{i\theta}$, and in the eigenbasis both factors are diagonal, with entries $re^{\pm i\theta}$ and $e^{\pm i\theta}$. The spectral condition is $\theta\notin\pi\mathbb{Z}$, equivalently $u\neq\pm1$: a unit is spectrally degenerate exactly when it is real.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}=\mathbb{R}[i]/(i^2+1)$ | the complex algebra, basis $1,i$ |
| $z=t+bi$ | a complex number |
| $A=\begin{pmatrix}t&-b\\ b&t\end{pmatrix}=tI+bJ$ | the Cayley matrix, $J^2=-I$ |
| $\lambda_\pm=t\pm ib$ | the eigenvalues |
| $v_+=(1,-i),\ v_-=(1,i)$ | the eigenvectors |
| $P=\begin{pmatrix}1&1\\ -i&i\end{pmatrix}$ | the eigenbasis matrix, $\det P=2i$ |
| $A_{\mathbb{C}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ | the complexified algebra, isomorphic to $\mathbb{C}\oplus\mathbb{C}$ |
| $\iota=1\otimes i$ | the algebra generator, $\iota^2=-1$ |
| $e_\pm=\frac12(1\mp i\iota)$ | the spectral idempotents |
| $\phi(a\otimes\alpha)=(a\alpha,a\bar\alpha)$ | the isomorphism $A_{\mathbb{C}}\to\mathbb{C}\oplus\mathbb{C}$ |
| $E_\pm=\frac{A-\lambda_\mp I}{\lambda_\pm-\lambda_\mp}$ | the spectral projectors, matrices of $L_{e_\pm}$ |
| $r=\lvert z\rvert=\sqrt{t^2+b^2}$ | the modulus |
| $u=z/r=e^{i\theta}$ | the unit factor, $\cos\theta=t/r$, $\sin\theta=b/r$ |
| $R_\theta=\cos\theta I+\sin\theta J$ | the rotation, $A=rR_\theta$ |

## Further Reading

- [Spectral Regularity and Degeneracy in the Complex Algebra](spectral-regularity-and-degeneracy-in-the-complex-algebra.html), for the eigenvalue criterion, the discriminant, the eigenspaces and semisimplicity.
- [Relations between the Modulus and Spectral Regularity and Degeneracy](relations-between-the-modulus-and-spectral-regularity-and-degeneracy.html), for the comparison of $|z|^2$ and $b^2$ and the place of the unit circle.
- [The Three Sectors of the Complex Algebra](the-three-sectors-of-the-complex-algebra.html), for the partition into $\Sigma_{11},\Sigma_{10},\Sigma_{00}$ and the empty $\Sigma_{01}$.
- [Complex Algebra](complex-algebra.html), for the algebra, its conjugation and its two distinguished subspaces.
- [Complex Regular Element Representation](complex-regular-element-representation.html), for the Cayley matrix, its multiplicativity and its determinant.
- [Modulus–Unit Polar Decomposition of Complex Numbers](modulus-unit-polar-decomposition-of-complex-numbers.html), for the polar decomposition, the unit circle and the modulus.
- [Complex Exponential and Lie Group Structure](complex-exponential-and-lie-group-structure.html), for the exponential $u=e^{i\theta}$ and the identification of the unit circle with $SO(2)$.
- [The Eigenvalue Decomposition of an Element](the-eigenvalue-decomposition-of-an-element.html), for the general existence and uniqueness theorems.
- [The Lagrange–Sylvester Eigenprojector Formula](the-lagrange-sylvester-eigenprojector-formula.html), for the interpolating projectors.
