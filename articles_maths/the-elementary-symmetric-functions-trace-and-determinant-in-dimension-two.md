# __The Elementary Symmetric Functions: $\operatorname{tr}$ and $\det$ in Dimension Two__

## Introduction

**The trace and the determinant are the two elementary symmetric functions of the two eigenvalues, and at order two they generate every conjugation-invariant polynomial.**

The article proves the identification $e_1=\operatorname{tr}$, $e_2=\det$, derives Newton's identities and the power-sum recursion they obey at order two, shows that the invariant ring of $M_2(\mathbb{C})$ is the free polynomial ring $\mathbb{C}[\operatorname{tr},\det]$, computes the Jacobian of the pair and locates its rank drop exactly at the scalar matrices, and separates the additive function from the multiplicative one. It assumes *The Element: Rank, Trace, Determinant, Characteristic Polynomial at $n=2$* for the element and its invariants. It defers the four products built from the trace to *The Symmetric and Antisymmetric Parts of a Product at $n=2$*, and the four norms to *The Four Forms and Their Algebraic Norms at $n=2$*.

The general statement of the invariant ring is in *The Trace Form and Its Signature on the Two Halves of $M_2(\mathbb{R})$* only for the form; the invariant theory at general order is *The Element, the Coordinates and the Trace of $M_n(\mathbb{C})$*. At order two the theory is the classical theory of symmetric functions in two variables, and that is the point of the article.

## The Symmetric Functions of Two Numbers

**Definition.** For two numbers $\lambda_1,\lambda_2$ the elementary symmetric functions are

$$
e_1=\lambda_1+\lambda_2,\qquad e_2=\lambda_1\lambda_2 ,
$$

and the power sums are $p_k=\lambda_1^{k}+\lambda_2^{k}$ for $k\ge1$.

**Proposition.** The ring of symmetric polynomials in two variables is $\mathbb{C}[e_1,e_2]$, freely generated.

**Proof.** The polynomials $e_1,e_2$ are algebraically independent: if $P(e_1,e_2)=0$ as a polynomial in $\lambda_1,\lambda_2$, then setting $\lambda_1=\lambda_2=t$ gives $P(2t,t^{2})=0$ for all $t$, which forces $P=0$ by the substitution $t\mapsto(2t,t^{2})$, an injection on monomials of the same degree. Every symmetric polynomial is a polynomial in the two elementary ones by the fundamental theorem of symmetric functions.

**Corollary.** Every symmetric polynomial in two variables has a unique expression in $e_1$ and $e_2$, of degree equal to its degree in each variable.

**Only two functions are needed at order two.** In $n$ variables there are $n$ elementary symmetric functions; at $n=2$ there are two, and every symmetric function is a polynomial in them. That count is the reason the whole invariant theory of the matrix algebra collapses to a plane.

## The Two Coefficients of the Characteristic Polynomial

**Theorem.** For $A\in M_2(\mathbb{C})$ with eigenvalues $\lambda_1,\lambda_2$,

$$
\boxed{\;e_1(A)=\operatorname{tr}A,\qquad e_2(A)=\det A.\;}
$$

**Proof.** The characteristic polynomial is $\lambda^{2}-(\operatorname{tr}A)\lambda+\det A$ and also $(\lambda-\lambda_1)(\lambda-\lambda_2)=\lambda^{2}-(\lambda_1+\lambda_2)\lambda+\lambda_1\lambda_2$; comparing coefficients gives both identities. The comparison is legitimate because the roots are the eigenvalues and the polynomial is monic of degree two.

**The functions are polynomials in the entries.** In coordinates, $e_1=a+d$ and $e_2=ad-bc$; the first is linear and the second is quadratic. Both are invariant under conjugation, because similar matrices have the same characteristic polynomial.

**The pair separates the generic element from its spectrum.** Two elements with the same $e_1$ and the same $e_2$ have the same characteristic polynomial, hence the same unordered pair of eigenvalues. Conversely the unordered pair fixes the two functions. The information lost in passing from $A$ to $(e_1,e_2)$ is exactly the choice of basis, on the generic stratum.

## Newton's Identities at Order Two

**Theorem (Newton).** For $k\ge1$,

$$
p_k=e_1p_{k-1}-e_2p_{k-2},\qquad p_0=2,\quad p_1=e_1 .
$$

**Proof.** Each eigenvalue satisfies $\lambda^{2}=e_1\lambda-e_2$, so $\lambda^{k}=e_1\lambda^{k-1}-e_2\lambda^{k-2}$ for $k\ge2$; summing over the two eigenvalues gives the identity. For $k=1$ the identity is $p_1=e_1p_0-e_2p_{-1}$ with the convention $p_{-1}=0$, which is the definition of $e_1$.

**Corollary (the first three power sums).** In terms of the matrix,

$$
\operatorname{tr}(A^{2})=(\operatorname{tr}A)^{2}-2\det A,\qquad
\operatorname{tr}(A^{3})=(\operatorname{tr}A)^{3}-3(\operatorname{tr}A)(\det A).
$$

**Proof.** $p_2=e_1^{2}-2e_2$ and $p_3=e_1p_2-e_2p_1=e_1^{3}-3e_1e_2$. At order two the two identities are also direct consequences of Cayley–Hamilton, which reads $A^{2}=(\operatorname{tr}A)A-(\det A)I$ and turns every power into a linear combination of $A$ and $I$.

**Inversion.** The two functions are recovered from the power sums by

$$
e_1=p_1,\qquad e_2=\tfrac12\bigl(p_1^{2}-p_2\bigr),
$$

so the pair $(p_1,p_2)$ and the pair $(e_1,e_2)$ carry the same information. The inversion is the content of the identity $\operatorname{tr}(A^{2})=(\operatorname{tr}A)^{2}-2\det A$ read backwards.

**The power sums are the moments of a measure of two atoms.** The recursion is the recursion of the moments of the spectral measure $\delta_{\lambda_1}+\delta_{\lambda_2}$, and at order two the measure is determined by two moments. This reading is the one used for the trace of a function of a matrix in *The Analysis on $M_2(\mathbb{C})$*.

## The Ring of Invariants

**Theorem.** The conjugation-invariant polynomial functions on $M_2(\mathbb{C})$ form the polynomial ring $\mathbb{C}[\operatorname{tr},\det]$, freely generated by the two functions.

**Proof.** An invariant polynomial is constant on every conjugacy class, hence on the dense set of diagonalisable elements, where it is a symmetric polynomial in the two eigenvalues, hence a polynomial in $e_1,e_2$ by §*The Symmetric Functions of Two Numbers*. Independence holds because $e_1,e_2$ are algebraically independent as functions of the eigenvalues, and the diagonal matrices realise every pair of eigenvalues.

**Corollary (the quotient).** The categorical quotient of $M_2(\mathbb{C})$ by conjugation is the plane $\mathbb{C}^{2}$, with quotient map $A\mapsto(\operatorname{tr}A,\det A)$.

**The degeneration of the ring.** The invariant ring is polynomial, so the quotient is smooth; the fibres of the quotient map are not. The fibre over $(\tau,\delta)$ with discriminant $\tau^{2}-4\delta\neq0$ is a single conjugacy class, of dimension $3$; the fibre over the parabola $\tau^{2}=4\delta$ is the union of the scalars and the Jordan classes, and its structure is *The Minimal Polynomial and the Two Jordan Regimes of $M_2(\mathbb{C})$*.

**The degrees.** The two generators have degrees $1$ and $2$; the product of the degrees is $2$, the order of the Weyl group of $GL_2$, and the sum of the degrees minus the rank, $1+2-2=1$, is the number of positive roots. Those coincidences are the general Chevalley statement read at rank two.

## The Jacobian and the Two Strata

**The pair $(\operatorname{tr},\det)$ is a map to a plane, and its differential is computed by the two gradients.**

**Proposition.** At $A$ the differential is

$$
D(\operatorname{tr},\det)_{A}(H)=\bigl(\operatorname{tr}H,\ \operatorname{tr}(\operatorname{adj}A\,H)\bigr),
$$

with $\operatorname{adj}A=(\operatorname{tr}A)I-A$.

**Proof.** The trace is linear. The determinant is differentiable with derivative $\operatorname{tr}(\operatorname{adj}A\,H)$, the classical formula; at order two it is the direct computation $\det(A+tH)=\det A+t\operatorname{tr}(\operatorname{adj}A\,H)+t^{2}\det H$, and the coefficient of $t$ is $\operatorname{tr}(\operatorname{adj}A\,H)$.

**Theorem (the rank of the Jacobian).** The two linear forms are dependent exactly at the scalar matrices, and independent everywhere else. So the map is a submersion of rank $2$ off $\mathbb{C}I$ and of rank $1$ on $\mathbb{C}I$.

**Proof.** The forms $\operatorname{tr}$ and $\operatorname{tr}(\operatorname{adj}A\,\cdot)$ are dependent exactly when $\operatorname{adj}A$ is a scalar, since the trace pairing is nondegenerate: $\operatorname{adj}A=\mu I$ means $(\operatorname{tr}A)I-A=\mu I$, that is $A=(\operatorname{tr}A-\mu)I$. Conversely at $A=\lambda I$ one has $\operatorname{adj}A=\lambda I$ and the second form is $\lambda$ times the first.

**Corollary.** The generic fibre is a smooth submanifold of complex dimension $2$; the fibre over the discriminant parabola is singular along the scalars. The dimension count is $4-2=2$ off the scalars, and the conjugacy class inside that fibre has dimension $4-2=2$, the dimension of $GL_2$ minus that of a maximal torus.

## Additive and Multiplicative

**The trace is additive on the algebra and the determinant is multiplicative on the group; neither is both.**

**Proposition.** $\operatorname{tr}(A+C)=\operatorname{tr}A+\operatorname{tr}C$ for all $A,C$, and $\det(AC)=\det A\det C$ for all $A,C$. But $\det(A+C)\neq\det A+\det C$ in general and $\operatorname{tr}(AC)\neq\operatorname{tr}A\operatorname{tr}C$ in general.

**Proof.** The first two are the linearity of the trace and the multiplicativity of the determinant. For the failures: with $A=C=I$, $\det(2I)=4\neq2=\det I+\det I$; with $A=C=I$ one has $\operatorname{tr}(AC)=\operatorname{tr}I=2$ while $\operatorname{tr}A\operatorname{tr}C=4$.

**The trace is a homomorphism on the additive group and the determinant on the multiplicative group.** The logarithm of the absolute value of the determinant is the additive character that the exponential converts into the trace: near the identity, $\log\det e^{H}=\operatorname{tr}H$. That identity is the reason the trace is the infinitesimal form of the determinant, and it is used in *The Exponential and the Lie Group Structure of $\mathrm{GL}_2(\mathbb{C})$*.

**The two functions on the two halves.** Restricted to $\operatorname{Herm}_2$ the trace is real and the determinant is real but not of a fixed sign; restricted to $\operatorname{Skew}_2$ the trace vanishes identically, because the single antisymmetric matrix of order two is traceless. The restrictions are computed in *The Trace Form and Its Signature on the Two Halves of $M_2(\mathbb{R})$*.

## Summary

The trace and the determinant are the elementary symmetric functions $e_1$ and $e_2$ of the two eigenvalues, in coordinates $a+d$ and $ad-bc$. They generate the ring of symmetric polynomials in two variables and the ring of conjugation-invariant polynomials on the algebra, freely, so the quotient by conjugation is the plane. Newton's identities give $p_k=e_1p_{k-1}-e_2p_{k-2}$ with $p_0=2$, hence $\operatorname{tr}(A^{2})=(\operatorname{tr}A)^{2}-2\det A$ and $\operatorname{tr}(A^{3})=(\operatorname{tr}A)^{3}-3(\operatorname{tr}A)(\det A)$, and the pair is recovered from $(p_1,p_2)$ by $e_2=\tfrac12(p_1^{2}-p_2)$.

The Jacobian of the pair is $\bigl(\operatorname{tr}H,\operatorname{tr}(\operatorname{adj}A\,H)\bigr)$, of rank $2$ off the scalar matrices and of rank $1$ on them. The trace is additive and the determinant multiplicative, and the log-determinant is the primitive of the trace on the group of invertibles.

| Power sum | Value at order two |
|---|---|
| $p_0$ | $2$ |
| $p_1$ | $\operatorname{tr}A$ |
| $p_2$ | $(\operatorname{tr}A)^{2}-2\det A$ |
| $p_3$ | $(\operatorname{tr}A)^{3}-3(\operatorname{tr}A)(\det A)$ |
| $p_4$ | $(\operatorname{tr}A)^{4}-4(\operatorname{tr}A)^{2}(\det A)+2(\det A)^{2}$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e_1,e_2$ | the elementary symmetric functions of the two eigenvalues |
| $p_k$ | the power sum $\operatorname{tr}(A^{k})$ |
| $\operatorname{tr},\det$ | the trace and the determinant, equal to $e_1$ and $e_2$ |
| $\mathbb{C}[\operatorname{tr},\det]$ | the ring of conjugation-invariant polynomials |
| $\operatorname{adj}A$ | the adjugate, equal to $(\operatorname{tr}A)I-A$ |
| $\tau,\delta$ | the values $\operatorname{tr}A$ and $\det A$ |
| $D(\operatorname{tr},\det)_{A}$ | the Jacobian at $A$ |

## Further Reading

- I. G. Macdonald, *Symmetric Functions and Hall Polynomials* (Oxford University Press, 1995), for the elementary symmetric functions, Newton's identities and the fundamental theorem.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the derivative of the determinant and the power sums at order two.
- [The Element: Rank, Trace, Determinant, Characteristic Polynomial at $n=2$](the-element-rank-trace-determinant-characteristic-polynomial-at-n-2.html), for the element and the Cayley–Hamilton identity used here.
- [The Matrix Algebra $M_2(\mathbb{C})$](the-matrix-algebra-m2c.html), for the trace and the determinant on the algebra.
