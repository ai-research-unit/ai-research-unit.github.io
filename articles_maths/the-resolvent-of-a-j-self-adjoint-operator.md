# __The Resolvent of a J-Self-Adjoint Operator__

## Introduction

The resolvent of an operator is the operator-valued function $z\mapsto(A-zI)^{-1}$ on the resolvent set, and for a self-adjoint operator on a Hilbert space it is the analytic carrier of the spectral theorem: it is bounded holomorphic off the real axis, satisfies $R(z)^*=R(\bar z)$, and obeys the sharp estimate $\|R(z)\|=1/\operatorname{dist}(z,\sigma(A))$ which makes the real line the only obstruction to its analyticity. For an operator that is self-adjoint in a Krein space, the resolvent keeps the algebraic structure and loses the metric one. The identity becomes $R(z)^{[*]}=R(\bar z)$ with the indefinite adjoint, so the resolvent set is symmetric under the reflection $z\mapsto\bar z$, and the spectrum is symmetric with respect to the real axis; but the norm estimate $\|R(z)\|=1/\operatorname{dist}(z,\sigma(A))$ fails in general, and the resolvent may grow as one approaches a real spectral point. The failure is not a defect of the theory but the trace of the negative directions of the form: it is measured by the negative spectral subspaces, and it disappears exactly in the definite case, where the indefinite metric is similar to a definite one and the Hilbert-space estimates return. The resolvent is also the device through which the indefinite spectral function is built, since the spectral projections are obtained from the boundary values of the resolvent in the definite case and from the local resolvent of Langer in the general case.

This article fixes the resolvent of a $J$-self-adjoint operator, its indefinite adjoint identity and the symmetry of the spectrum, the Cayley transform into the $J$-unitary group, the failure and the restoration of the norm estimates, and the role of the resolvent in constructing the spectral function. The Krein space and its fundamental symmetry are *Krein Spaces*; the $J$-self-adjoint operators, the finite-rank exceptional spectrum and the definite case are *The General Spectral Theorem on a Krein Space*; the indefinite adjoint used throughout is *The Signed Adjoint Sandwich on a Krein Space*; the Hilbert-space theory of the resolvent is *Self-Adjoint Operators and the Spectral Theorem*; the resolvent of a closed unbounded operator is *The Adjoint of an Unbounded Operator*.

Throughout, $K$ is a Krein space with fundamental symmetry $J$, indefinite inner product $[x,y]=\langle Jx,y\rangle$ and indefinite adjoint $A^{[*]}=JA^*J$; the operator $A\in B(K)$ is $J$-self-adjoint, $A^{[*]}=A$. The **resolvent set** is $\rho(A)=\{z\in\mathbb{C}:A-zI\ \text{is invertible in}\ B(K)\}$, the **spectrum** is $\sigma(A)=\mathbb{C}\setminus\rho(A)$, and the **resolvent** is

$$
R(z)=R(z,A)=(A-zI)^{-1}\qquad(z\in\rho(A)).
$$

## The Resolvent

**Proposition (analyticity and the identity).** The resolvent is holomorphic on the open set $\rho(A)$, and for $z,w\in\rho(A)$,

$$
R(z)-R(w)=(z-w)R(z)R(w)= (z-w)R(w)R(z),
$$

so the resolvent is a maximal analytic operator-valued function with values in $B(K)$; its derivative is $R'(z)=R(z)^2$, and $\sigma(A)$ is closed and compact.

*Proof.* The resolvent identity is the algebraic manipulation $(A-zI)^{-1}-(A-wI)^{-1}=(A-zI)^{-1}((A-wI)-(A-zI))(A-wI)^{-1}$; it gives the continuity of $z\mapsto R(z)$ and, with the power series $R(z)=\sum_n(z-w)^nR(w)^{n+1}$ for $|z-w|<\|R(w)\|^{-1}$, the analyticity; the derivative and the compactness of the spectrum are standard.

**Proposition (the indefinite adjoint identity).** For a $J$-self-adjoint $A$ and $z\in\rho(A)$ one has $\bar z\in\rho(A)$ and

$$
R(z)^{[*]}=R(\bar z),\qquad\text{that is}\qquad J\,R(z)^*\,J=R(\bar z),
$$

so the resolvent set is symmetric with respect to the real axis, the spectrum is symmetric, $\sigma(A)=\overline{\sigma(A)}$, and the resolvent satisfies the indefinite counterpart of the Hilbert-space identity.

*Proof.* Taking the indefinite adjoint of $(A-zI)^{-1}$ gives $((A-zI)^{[*]})^{-1}=(A^{[*]}-\bar zI)^{-1}=(A-\bar zI)^{-1}$, which is $R(\bar z)$; hence $z\in\rho(A)$ iff $\bar z\in\rho(A)$, and the spectrum is invariant under conjugation.

**Proposition (the resolvent as a form).** The resolvent satisfies the indefinite analogues of the quadratic identities: for $x,y\in K$ the function $z\mapsto[R(z)x,y]$ is holomorphic on $\rho(A)$, and for $z,\bar z\in\rho(A)$,

$$
[R(z)x,y]=\overline{[R(\bar z)y,x]} ,
$$

so the resolvent is a $J$-self-adjoint operator-valued function of $z$, and the scalar function $z\mapsto[R(z)x,x]$ is the Stieltjes transform of the spectral function when the latter exists.

*Proof.* The first statement is the analyticity of the resolvent composed with the bounded form; the identity is the indefinite adjoint identity evaluated on the pair and conjugated, and the Stieltjes statement is the integral representation of the resolvent in the definite case.

## The Spectrum and Its Symmetry

**Theorem (the spectrum of a $J$-self-adjoint operator).** For a bounded $J$-self-adjoint operator $A$:

(i) the spectrum is symmetric, $\sigma(A)=\overline{\sigma(A)}$;

(ii) the non-real part of the spectrum consists of eigenvalues, and the Jordan structure at $\bar\lambda$ is the indefinite adjoint of the Jordan structure at $\lambda$;

(iii) if $K$ is a Pontryagin space $\Pi_\kappa$ then the non-real spectrum has at most $\kappa$ points counted with algebraic multiplicity;

(iv) if $A$ is definite then the spectrum is real.

*Proof.* (i) is the adjoint identity. (ii): on a small circle separating $\lambda$ from the rest of the spectrum the spectral projection is the Rouché integral of the resolvent, and the indefinite adjoint identity transports the Jordan chain at $\lambda$ to a chain at $\bar\lambda$ with the same length, because $\dim\ker(A-\lambda I)^n=\dim\ker(A-\bar\lambda I)^n$ by the adjoint identity and the invertibility of $J$. (iii) is Pontryagin's theorem, and (iv) is Krein's similarity theorem, both from *The General Spectral Theorem on a Krein Space*.

**Proposition (real eigenvalues and the Krein form).** An eigenvalue $\lambda\in\mathbb{R}$ of a $J$-self-adjoint operator has eigenvectors whose mutual indefinite products are constrained: for two eigenvectors $x,y$ at real eigenvalues $\lambda,\mu$,

$$
(\lambda-\mu)\,[x,y]=0 ,
$$

so eigenvectors at distinct real eigenvalues are $J$-orthogonal, and the kernel of $A-\lambda I$ is a neutral or definite subspace according to the signs of the quadratic form on it.

*Proof.* $[Ax,y]=[x,Ay]$ gives $\lambda[x,y]=\mu[x,y]$, hence the orthogonality; the definiteness statement is the classification of subspaces of a Krein space by the sign of the form.

**Example (the shift of the metric).** The matrix $A=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ of the previous article is $J$-self-adjoint with $\sigma(A)=\{\pm i\}$; its resolvent is $(A-zI)^{-1}=\frac{1}{z^2+1}\begin{pmatrix}-z&-1\\1&-z\end{pmatrix}$ and satisfies $R(z)^{[*]}=R(\bar z)$, and the two poles at $\pm i$ are the conjugate pair of the statement.

## The Cayley Transform and the $J$-Unitary Group

**Theorem (the Cayley transform in the Krein space).** For a bounded $J$-self-adjoint $A$ the operator

$$
C(A)=(A-iI)(A+iI)^{-1}
$$

is $J$-unitary, $C(A)^{[*]}C(A)=C(A)C(A)^{[*]}=I$, and the assignment is a bijection from the $J$-self-adjoint operators onto the $J$-unitaries $U$ with $1\notin\sigma(U)$, with inverse $U\mapsto i(I+U)(I-U)^{-1}$; the map is continuous in the norm topology and its inverse is continuous.

*Proof.* Since $\pm i\in\rho(A)$ for a bounded $J$-self-adjoint operator by the symmetry of the spectrum, the transform is defined; writing $C(A)=(A+iI-2iI)(A+iI)^{-1}=I-2iR(-i)$ one computes $C(A)^{[*]}C(A)=I$ from $R(\bar z)^{[*]}=R(z)$; the inverse is the inverse Möbius transformation, and the continuity is the continuity of the resolvent and of the algebraic operations.

**Proposition (the spectrum on the circle).** The Cayley transform carries the spectrum of $A$ by the Möbius map $\lambda\mapsto(\lambda-i)/(\lambda+i)$, so the non-real spectrum of $A$ corresponds to the points of $\sigma(C(A))$ off the unit circle; in the definite case $\sigma(C(A))\subseteq\mathbb{T}$, and the group $e^{itA}$ is a $J$-unitary group whose generator is $A$.

*Proof.* The functional calculus in the definite metric gives the spectral mapping; the off-circle correspondence is the image of the real axis by a Möbius map when the metric is not definite, and the group statement is the computation of the exponential with the indefinite adjoint.

## Resolvent Estimates and the Definite Case

**Theorem (the sharp Hilbert estimate).** For a self-adjoint $A$ on a Hilbert space,

$$
\|R(z)\|=\frac1{\operatorname{dist}(z,\sigma(A))}\qquad(z\notin\sigma(A)),
$$

and the equality characterises the self-adjoint case among bounded operators up to similarity by a unitary.

*Proof.* The spectral theorem writes $R(z)=\int(\lambda-z)^{-1}dE(\lambda)$, and the norm of the multiplication by $(\lambda-z)^{-1}$ is the supremum of its modulus over the support, which is $1/\operatorname{dist}(z,\sigma(A))$; the converse is the standard characterisation.

**Theorem (failure in the indefinite metric).** A bounded $J$-self-adjoint operator satisfies the one-sided estimates

$$
\|R(z)\|\ge\frac1{\operatorname{dist}(z,\sigma(A))}\quad\text{and}\quad\|R(z)\|\le\frac{M}{\operatorname{dist}(z,\sigma(A))}
$$

for a constant $M$ depending on $A$ and the fundamental decomposition when $A$ is definite; in the general indefinite case no bound of the form $M/\operatorname{dist}(z,\sigma(A))$ need hold, and the resolvent may grow arbitrarily fast as the real spectrum is approached, the growth being governed by the negative spectral subspace.

*Proof.* The lower bound is the spectral radius estimate for any bounded operator, since the norm of the resolvent is at least the reciprocal of the distance to the spectrum. In the definite case $A=V^{-1}BV$ with a Hilbert-space self-adjoint $B$, so $R(z)=V^{-1}(B-zI)^{-1}V$ and the bound follows with $M=\|V\|\|V^{-1}\|$. In the indefinite case the similarity constant is infinite — there is no bounded $V$ making the metric definite — and the negative part of the form produces the unbounded growth; the Pontryagin case shows the growth is confined to finitely many directions.

**Remark (the sensitivity of the resolvent).** The resolvent is holomorphic, so its growth near the real axis is controlled by the distance to the non-real spectrum; a $J$-self-adjoint operator with non-real eigenvalues has a resolvent bounded away from the real axis and analytic there, so the failure of the estimate occurs at the real spectrum, and the local behaviour is the local spectral theory of *The General Spectral Theorem on a Krein Space*.

## The Resolvent and the Spectral Function

**Proposition (from the resolvent to the spectral function).** In the definite case the spectral function is obtained from the boundary values of the resolvent,

$$
E((a,b])=\lim_{\delta\downarrow0}\frac1{2\pi i}\int_a^b\bigl(R(\lambda-i\delta)-R(\lambda+i\delta)\bigr)\,d\lambda ,
$$

the integral converging in the strong operator topology; in the general Pontryagin case the same formula defines the spectral function on the real line outside the finite exceptional set, together with a finite-dimensional correction at the exceptional points.

*Proof.* The formula is the Stieltjes inversion of the integral representation $R(z)=\int(\lambda-z)^{-1}dE(\lambda)$; the strong convergence is the $L^2$ theory of the Poisson kernel, and the correction is the finite-dimensional part of the general spectral theorem.

**Proposition (the resolvent identity in the indefinite metric).** The second resolvent identity holds in the form

$$
R(z,A)-R(z,B)=R(z,A)\,(A-B)\,R(z,B),
$$

and its indefinite adjoint is the same identity with $A-B$ replaced by its indefinite adjoint; the identity is the algebraic engine of the perturbation theory in a Krein space, exactly as in the Hilbert-space case.

*Proof.* Expand the difference of the inverses and insert $I=(A-zI)R(z,A)=R(z,B)(B-zI)$ appropriately; the adjoint version follows by taking the indefinite adjoint and using $R(z)^{[*]}=R(\bar z)$.

## Summary

The resolvent $R(z)=(A-zI)^{-1}$ of a bounded $J$-self-adjoint operator is holomorphic on the open resolvent set, satisfies the resolvent identity $R(z)-R(w)=(z-w)R(z)R(w)$, and obeys the indefinite adjoint identity $R(z)^{[*]}=R(\bar z)$, equivalently $JR(z)^*J=R(\bar z)$; consequently the resolvent set and the spectrum are symmetric with respect to the real axis, and the Jordan structure at $\bar\lambda$ is the indefinite adjoint of that at $\lambda$. The non-real spectrum consists of eigenvalues, it has at most $\kappa$ points counted with algebraic multiplicity in a Pontryagin space $\Pi_\kappa$, and it is empty when $A$ is definite; eigenvectors at distinct real eigenvalues are $J$-orthogonal. The Cayley transform $C(A)=(A-iI)(A+iI)^{-1}$ is a $J$-unitary with $1\notin\sigma(C(A))$, giving a bijection between the $J$-self-adjoint operators and the $J$-unitaries avoiding the point $1$ and transporting the spectrum by a Möbius map. The sharp Hilbert estimate $\|R(z)\|=1/\operatorname{dist}(z,\sigma(A))$ fails in the indefinite metric; the lower bound always holds, the upper bound holds with a similarity constant in the definite case, and in general the resolvent may grow without a distance bound at the real spectrum, the growth being controlled by the negative spectral subspace. The spectral function is recovered from the boundary values of the resolvent by the Stieltjes inversion formula, and the second resolvent identity carries the perturbation theory of the Hilbert-space case into the Krein space.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho(A)$, $\sigma(A)$ | resolvent set and spectrum |
| $R(z)=(A-zI)^{-1}$ | the resolvent |
| $R(z)-R(w)=(z-w)R(z)R(w)$ | the resolvent identity |
| $R(z)^{[*]}=R(\bar z)$ | indefinite adjoint identity |
| $\sigma(A)=\overline{\sigma(A)}$ | symmetry of the spectrum |
| $C(A)=(A-iI)(A+iI)^{-1}$ | Cayley transform, a $J$-unitary |
| $\|R(z)\|=1/\operatorname{dist}(z,\sigma(A))$ | the Hilbert-space estimate |
| $\|R(z)\|\le M/\operatorname{dist}$ (definite) | restored estimate in the definite case |
| $E((a,b])=$ inversion of $R$ | spectral function from the resolvent |
| at most $\kappa$ non-real eigenvalues | Pontryagin case |

## Further Reading

- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for the resolvent, the spectrum and the Cayley transform in a Krein space.
- Mark G. Krein and Heinz Langer, "On the Spectral Function of a Self-Adjoint Operator in a Space with Indefinite Metric", *Soviet Mathematics Doklady* **3** (1962), 404–406, for the spectral function from the resolvent.
- Heinz Langer, "Spectral Functions of Definitizable Operators in Krein Spaces", in *Functional Analysis*, Lecture Notes in Mathematics 948 (Springer, 1982), 1–46, for the local resolvent and the spectral function.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the finite-dimensional resolvent and the Jordan structure.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for the second resolvent identity and the analytic perturbation theory.

