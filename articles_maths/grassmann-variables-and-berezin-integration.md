
# __Grassmann Variables and Berezin Integration__

## Introduction

A **Grassmann variable** is a generator of an exterior algebra, treated as a coordinate. An expression in such variables is a polynomial in anticommuting indeterminates, and the algebra of such expressions is the exterior algebra of the companion articles *Exterior Powers* and *The Exterior Algebra*. What makes the calculus of Grassmann variables distinctive is the **Berezin integral**: a linear functional that extracts the coefficient of the top monomial, defined for every element of a finite-dimensional exterior algebra, with no limit, no measure and no convergence. It is a purely algebraic operation, and it satisfies a change-of-variables formula in which the Jacobian is the inverse of an ordinary determinant. The resulting calculus produces the determinant and the Pfaffian as Gaussian integrals over odd variables.

This article develops the algebra of odd variables, the two derivatives — left and right — and the integral, the rules of Berezin integration, and the Gaussian integral with its two consequences: the Pfaffian appears as the integral of the exponential of an alternating quadratic form, and the determinant appears as the square of that integral, or as the super-Gaussian integral when even variables are present. The treatment is algebraic throughout; the analytic Gaussian over real variables is invoked only as the classical counterpart that supplies the normalising constants, and the super-determinant relation is stated in terms of the Berezinian of the superalgebra article *Superalgebras and Graded Structures*.

Throughout, $R$ is a commutative ring with identity $1 \neq 0$ in which $2$ is invertible, $K$ is a field of characteristic different from $2$, and $V$ is a free $R$-module of finite rank $n$ with basis $\theta_1, \ldots, \theta_n$ placed in odd parity. The exterior algebra $\Lambda(V)$ has the notation of *The Exterior Algebra*: the product is $\wedge$, its Koszul sign rule is $\theta_i \theta_j = -\theta_j \theta_i$, and the basis consists of the squarefree monomials $\theta_I$ indexed by subsets $I \subseteq \{1, \ldots, n\}$. The Pfaffian and the determinant are those of *The Determinant and Alternating Forms*. No physics is invoked.

## Odd Variables and the Grassmann Algebra

### Odd Generators

**Definition.** Let $\theta_1, \ldots, \theta_n$ be a basis of the free $R$-module $V$, placed in odd parity. The **Grassmann algebra** on these variables is the exterior algebra $\Lambda(\theta_1, \ldots, \theta_n) = \Lambda(V)$, the free graded-commutative algebra on the $\theta_i$, subject to

$$
\theta_i \theta_j = -\theta_j \theta_i, \qquad \theta_i^2 = 0, \qquad i, j = 1, \ldots, n.
$$

The **degree** of a monomial is the number of variables in it, and the **parity** of a monomial is its degree modulo $2$.

**Proposition.** The monomials

$$
\theta_I = \theta_{i_1}\theta_{i_2}\cdots\theta_{i_k}, \qquad I = \{i_1 < i_2 < \cdots < i_k\},
$$

together with the empty product $1 = \theta_\varnothing$, form a basis of $\Lambda(\theta_1, \ldots, \theta_n)$ over $R$; the algebra has rank $2^n$. If $\sigma$ is a permutation of the indices $i_1, \ldots, i_k$, then

$$
\theta_{i_{\sigma(1)}}\theta_{i_{\sigma(2)}}\cdots\theta_{i_{\sigma(k)}} = \operatorname{sgn}(\sigma)\, \theta_{i_1}\theta_{i_2}\cdots\theta_{i_k},
$$

and a monomial with a repeated index vanishes.

**Proof.** This is the basis theorem and the Koszul sign rule of *The Exterior Algebra*, read in parity one. $\square$

### Functions of Odd Variables

**Definition.** A **function of the odd variables** $\theta_1, \ldots, \theta_n$ is an element $f \in \Lambda(\theta_1, \ldots, \theta_n)$, written as

$$
f(\theta) = \sum_{I \subseteq \{1, \ldots, n\}} c_I\, \theta_I, \qquad c_I \in R.
$$

The coefficient $c_{\{1, \ldots, n\}}$ of the **top monomial** $\theta_1\theta_2\cdots\theta_n$ is the **top coefficient** of $f$.

**Remark.** Because each $\theta_i$ squares to zero, every function of odd variables is a polynomial of degree at most $n$; there are no nonzero functions of higher degree. This is the reason the Berezin integral below is a finite operation. The even part of $\Lambda(\theta)$ consists of the functions of even degree and the odd part of those of odd degree, and the two parts commute or anticommute according to the super sign rule.

**Example.** For a single odd variable $\theta$, the functions are $f(\theta) = a + b\theta$ with $a, b \in R$, and the product is $f g = ac + (ad + bc)\theta$; the algebra is the ring of dual numbers, two-dimensional over $R$. For two odd variables, $f = a + b\theta_1 + c\theta_2 + d\theta_1\theta_2$ with $\theta_1\theta_2 = -\theta_2\theta_1$; the algebra has rank $4$.

## Differentiation

### Left and Right Derivatives

**Definition.** The **left derivative** with respect to $\theta_i$ is the $R$-linear map $\dfrac{\partial}{\partial\theta_i} : \Lambda(V) \to \Lambda(V)$ that removes the first occurrence of $\theta_i$ from a monomial with the sign accumulated from the transpositions needed to bring it to the front:

$$
\frac{\partial}{\partial\theta_i}\bigl(\theta_{i_1}\cdots\theta_{i_k}\bigr) = \sum_{j=1}^{k} (-1)^{j-1}\, \delta_{i, i_j}\, \theta_{i_1}\cdots\widehat{\theta_{i_j}}\cdots\theta_{i_k},
$$

where the hat denotes omission and the sum is over the positions at which $\theta_i$ occurs.

**Definition.** The **right derivative** $\dfrac{\overleftarrow{\partial}}{\partial\theta_i}$ is defined by bringing the $\theta_i$ to the end of the monomial and removing it, with the sign of the transpositions used.

**Proposition.** For a monomial of degree $k$,

$$
\frac{\overleftarrow{\partial}}{\partial\theta_i} = (-1)^{k-1}\, \frac{\partial}{\partial\theta_i}.
$$

Consequently the two derivatives agree on monomials of odd degree and differ by a sign on monomials of even degree, and for a general element $f$ one has $\overleftarrow{\partial}_i f = \sum_k (-1)^{k-1} (\partial_i f)_k$ where $(\partial_i f)_k$ is the degree-$k$ component of $\partial_i f$.

**Proof.** In a monomial of degree $k$ containing $\theta_i$ at position $j$, its removal by the left derivative gives the sign $(-1)^{j-1}$ and its removal by the right derivative gives the sign $(-1)^{k-j}$, since $\theta_i$ must pass the $k-j$ factors to its right. The ratio is $(-1)^{k-j-j+1} = (-1)^{k+1} = (-1)^{k-1}$. $\square$

### Properties of the Derivatives

**Proposition.** The left derivatives satisfy the following.

**(a) Anticommutativity.** $\dfrac{\partial}{\partial\theta_i}\dfrac{\partial}{\partial\theta_j} = -\dfrac{\partial}{\partial\theta_j}\dfrac{\partial}{\partial\theta_i}$; in particular $\left(\dfrac{\partial}{\partial\theta_i}\right)^2 = 0$.

**(b) Leibniz rule.** For homogeneous $f, g$,

$$
\frac{\partial}{\partial\theta_i}(fg) = \frac{\partial f}{\partial\theta_i}\, g + (-1)^{|f|}\, f\, \frac{\partial g}{\partial\theta_i},
$$

where $|f|$ is the parity of $f$; the right derivative obeys the same rule with the sign on the other factor.

**(c) Degree lowering.** A left or right derivative lowers the degree by one, and it is a derivation of parity one of the graded-commutative algebra.

**Proof.** (a) Both sides are determined on monomials, where the removal of $\theta_j$ and then $\theta_i$ differs from the removal of $\theta_i$ and then $\theta_j$ by one transposition, giving the sign; applying the operator twice with $i = j$ means removing the same variable twice, which is zero. (b) is checked on monomials by removing $\theta_i$ from the product and tracking the sign. (c) is immediate from the definition. $\square$

**Remark.** The left derivatives are the odd derivations of the exterior algebra; the algebra of all such operators is a Clifford algebra, as is the algebra generated by the $\theta_i$ and the $\partial/\partial\theta_i$ under the anticommutator. This is the algebraic skeleton of the calculus.

## The Berezin Integral

### Definition

**Definition.** The **Berezin integral** is the $R$-linear functional

$$
\int \cdot \; d\theta : \Lambda(\theta_1, \ldots, \theta_n) \longrightarrow R, \qquad \int f\, d\theta = c_{\{1, \ldots, n\}},
$$

the top coefficient of $f$, where $d\theta = d\theta_1\cdots d\theta_n$ is a formal symbol. Equivalently,

$$
\int f\, d\theta = \frac{\partial}{\partial\theta_n} \cdots \frac{\partial}{\partial\theta_2} \frac{\partial}{\partial\theta_1} f,
$$

the composition of the left derivatives in the reverse order of the variables.

**Proposition.** The Berezin integral is the unique $R$-linear functional $I$ on $\Lambda(\theta_1, \ldots, \theta_n)$ with

$$
I(\theta_1\theta_2\cdots\theta_n) = 1, \qquad I\left(\frac{\partial f}{\partial\theta_i}\right) = 0 \ \text{for all } f \text{ and all } i.
$$

**Proof.** The first condition fixes $I$ on the top monomial and hence, by linearity and the basis theorem, the functional is determined by its values on the basis; the second condition forces $I(\theta_I) = 0$ unless $I$ is the full set, because $\theta_I = \partial_{\theta_i}\theta_{I \cup \{i\}}$ up to sign whenever $i \notin I$. $\square$

**Definition.** The integral over a subset of the variables, written $\int f\, d\theta_{i_1}\cdots d\theta_{i_k}$, is the composition of the corresponding partial integrations; it is a function of the remaining odd variables.

**Example.** For $f = \theta_1\theta_2 + 3\theta_2 + 5$, the integral over both variables is $\int f\, d\theta_1 d\theta_2 = 1$, the top coefficient. The integral over $\theta_1$ alone is $\int f\, d\theta_1 = \theta_2$, and the integral over $\theta_2$ alone is $\int f\, d\theta_2 = 3 - \theta_1$: the constant term contributes nothing, the linear term contributes its coefficient, and the top monomial contributes with the sign of the transposition needed to bring $\theta_2$ to the front.

### Rules of the Integral

**Proposition.** The Berezin integral has the following properties.

**(a) Linearity.** $\int (\alpha f + \beta g)\, d\theta = \alpha \int f\, d\theta + \beta \int g\, d\theta$.

**(b) Translation invariance.** For a constant odd shift $\eta \in \Lambda^1$,

$$
\int f(\theta + \eta)\, d\theta = \int f(\theta)\, d\theta.
$$

**(c) Integration by parts.** $\displaystyle\int \frac{\partial f}{\partial\theta_i}\, d\theta = 0$, and for homogeneous $f$,

$$
\int \left(\frac{\partial f}{\partial\theta_i} g\right) d\theta = -(-1)^{|f|} \int \left( f\, \frac{\partial g}{\partial\theta_i} \right) d\theta.
$$

**Proof.** (a) is linearity of the coefficient extraction. For (b), both $\theta$ and $\theta + \eta$ have the same linear span and the same top monomial, and the coefficient of the top monomial is unchanged by the translation, since the shift contributes only lower-degree terms after expansion: expanding $f(\theta+\eta)$ by the Leibniz rule, the extra terms each contain a factor $\eta$ and a product in which some $\theta_i$ is missing, hence have degree less than $n$ and top coefficient zero. For (c), the first identity is the characterisation of the integral; the second follows from (b) of the Leibniz proposition applied to $\int \partial_i(fg)\,d\theta = 0$. $\square$

### Change of Variables

**Theorem (Berezinian change of variables).** Let $N = (N_{ij})$ be an invertible $n \times n$ matrix over $R$ and let $\theta_i = \sum_j N_{ij}\eta_j$ be a linear change of odd variables. Then for every $f \in \Lambda(\eta_1, \ldots, \eta_n)$,

$$
\int f(\theta)\, d\theta = \det(N)^{-1} \int f(N\eta)\, d\eta,
$$

or, in the equivalent form $d\theta = \det(N)^{-1} d\eta$. The Jacobian factor is the **inverse** of the determinant of the change of variables.

**Proof.** Both sides are $R$-linear in $f$, so it suffices to check the identity on the basis elements $f = \theta_I$. If $I$ is a proper subset of $\{1, \ldots, n\}$ then $\theta_I$ has degree less than $n$ and both integrals vanish. If $I = \{1, \ldots, n\}$ then the left side is $1$ by the normalisation, while $\theta_1(\eta)\cdots\theta_n(\eta) = \det(N)\,\eta_1\cdots\eta_n$ by the antisymmetry of the exterior product, the wedge of the $n$ linear forms $\theta_i(\eta)$ being $\det(N)$ times the top form; hence the right side is $\det(N)^{-1}\det(N) = 1$. The identity follows by linearity. $\square$

**Corollary.** The Berezin integral is invariant under a change of odd variables with $\det(N) = 1$, and it scales by $\det(N)^{-1}$ in general, in contrast with the bosonic case, where the Jacobian is the determinant itself. For a single change of sign, $\theta_i \mapsto -\theta_i$, the Jacobian is $-1$, so that $\int f(\theta)\, d\theta = -\int f(N\eta)\, d\eta$: the sign produced by the substitution is absorbed by the Jacobian determinant.

### The Constant Term and Fubini

**Proposition (Fubini).** For $f \in \Lambda(\theta_1, \ldots, \theta_n)$ and a splitting of the variables into two sets,

$$
\int f\, d\theta = \int \left(\int f\, d\theta^{(1)}\right) d\theta^{(2)},
$$

where the inner integral is over the first set and the outer over the second. The iterated integral is independent of the order of integration.

**Proof.** The two iterated integrals both compute the top coefficient: the inner integral produces the coefficient of the top monomial of the first set, as an element of the algebra on the remaining variables, and the outer integral extracts its top coefficient. $\square$

## The Gaussian Integral

### The Odd Gaussian

**Theorem (the odd Gaussian integral).** Let $n = 2m$ be even and let $A = (A_{ij})$ be an alternating $2m \times 2m$ matrix over $R$. Then the Berezin integral of the exponential

$$
\exp\left(\frac{1}{2}\sum_{i,j} A_{ij}\, \theta_i\theta_j\right) = \exp\left(\sum_{i<j} A_{ij}\,\theta_i\theta_j\right)
$$

is the Pfaffian:

$$
\int \exp\left(\frac{1}{2}\sum_{i,j} A_{ij}\theta_i\theta_j\right) d\theta = \operatorname{Pf}(A).
$$

**Proof.** Expanding the exponential, only the term of degree $m$ in the quadratic form can contribute to the top coefficient. That term is

$$
\frac{1}{m!}\left(\sum_{i<j} A_{ij}\theta_i\theta_j\right)^m,
$$

and by the definition of the Pfaffian as the coefficient of $\theta_1\theta_2\cdots\theta_{2m}$ in $\frac{1}{2^m m!}\left(\sum_{i,j}A_{ij}\theta_i\theta_j\right)^m$ — the standard expression of the Pfaffian of *The Determinant and Alternating Forms* — its Berezin integral is $\operatorname{Pf}(A)$. $\square$

**Example.** For $m = 1$ and $A = \begin{pmatrix} 0 & a \\ -a & 0\end{pmatrix}$, the exponent is $a\theta_1\theta_2$ and the exponential is $1 + a\theta_1\theta_2$; the integral is $a = \operatorname{Pf}(A)$. For $m = 2$ the Pfaffian of a $4 \times 4$ alternating matrix is $A_{12}A_{34} - A_{13}A_{24} + A_{14}A_{23}$, the coefficient of $\theta_1\theta_2\theta_3\theta_4$ in the exponential.

### The Determinant

**Corollary.** For an alternating $2m \times 2m$ matrix $A$, the square of the Gaussian integral is the determinant:

$$
\left(\int \exp\left(\tfrac{1}{2}\theta^{T} A \theta\right) d\theta \right)^{2} = \operatorname{Pf}(A)^2 = \det(A).
$$

Equivalently, with two independent sets of odd variables $\theta$ and $\eta$,

$$
\det(A) = \int \exp\left(\tfrac{1}{2}\theta^{T}A\theta + \tfrac{1}{2}\eta^{T}A\eta\right) d\theta\, d\eta.
$$

This is the algebraic form of the statement that a determinant is a square of a Gaussian integral over odd variables, in contrast with the bosonic Gaussian, whose value is the inverse square root of the determinant.

### The Super-Gaussian

The two Gaussian integrals combine into one over a super vector space. Let $B$ be a symmetric positive definite $p \times p$ matrix of even variables $x = (x_1, \ldots, x_p)$ and let $A$ be an alternating $2m \times 2m$ matrix of odd variables $\theta = (\theta_1, \ldots, \theta_{2m})$. Formally,

$$
\int_{\mathbb{R}^p} \int \exp\left(-\tfrac{1}{2} x^{T} B x + \tfrac{1}{2}\theta^{T} A \theta\right) dx\, d\theta = (2\pi)^{p/2} (\det B)^{-1/2} \operatorname{Pf}(A).
$$

The right-hand side is, up to the factor $(2\pi)^{p/2}$, the inverse square root of the Berezinian of the block diagonal supermatrix $\operatorname{diag}(B, A)$:

$$
\operatorname{Ber}\begin{pmatrix} B & 0 \\ 0 & A\end{pmatrix} = \frac{\det B}{\det A} = \frac{\det B}{\operatorname{Pf}(A)^2},
$$

so that $(2\pi)^{p/2}\operatorname{Ber}(\operatorname{diag}(B,A))^{-1/2} = (2\pi)^{p/2}(\det B)^{-1/2}\operatorname{Pf}(A)$. This is the sense in which the odd Gaussian converts the Pfaffian into the square root of a determinant, and it is the origin of the Berezinian in the superalgebra article *Superalgebras and Graded Structures*.

**Remark.** The bosonic Gaussian $\int_{\mathbb{R}^p} e^{-\frac12 x^TBx}dx = (2\pi)^{p/2}(\det B)^{-1/2}$ is an analytic statement, and it is quoted here as the classical counterpart of the algebraic odd Gaussian; the odd integral requires no analysis, and its value is an integral polynomial in the entries of $A$.

## Properties and Structural Remarks

### The Integral as a Top-Degree Projection

**Proposition.** The Berezin integral is a morphism of $\Lambda(V)$-modules in the following sense: for $g \in \Lambda(V)$ not containing the variable $\theta_i$, $\int g f\, d\theta_i = g \int f\, d\theta_i$. Consequently the full integral is the projection onto the top-degree component composed with the identification $\Lambda^n(V) \cong R$ given by the basis element $\theta_1\cdots\theta_n$.

**Proof.** Multiplication by $g$ does not involve $\theta_i$, so it commutes with the coefficient extraction in $\theta_i$; the second statement is the definition. $\square$

### The Top-Degree Component and Duality

**Proposition.** The pairing $\Lambda^k(V) \times \Lambda^{n-k}(V) \to R$, $(f, g) \mapsto \int fg\, d\theta$, is perfect when $V$ is free of finite rank $n$: it identifies $\Lambda^{n-k}(V)$ with the dual of $\Lambda^k(V)$.

**Proof.** The pairing sends a basis monomial $\theta_I$ of degree $k$ and a basis monomial $\theta_J$ of degree $n-k$ to the top coefficient of $\theta_I\theta_J$, which is $\pm 1$ when $J$ is the complement of $I$ and $0$ otherwise. The resulting matrix is invertible over $R$, its entries being $\pm 1$; hence the pairing is perfect. $\square$

**Corollary.** The Berezin integral is the algebraic form of the integration of a top-degree differential form: in the exterior algebra of a free module of finite rank, the top-degree component is one-dimensional, and the choice of a basis trivialises it, while the integral is the resulting linear functional. This is the point of contact with the differential forms.

## Summary

The Grassmann algebra on $n$ odd generators is the exterior algebra of an $n$-dimensional odd module, with basis the squarefree monomials and rank $2^n$; a function of odd variables is a polynomial of degree at most $n$. Differentiation with respect to an odd variable is the removal of that variable with the sign of the transpositions required, left and right derivatives differing by $(-1)^{k-1}$ on a monomial of degree $k$, and the derivatives anticommute and satisfy a graded Leibniz rule.

The Berezin integral is the linear functional extracting the top coefficient, equivalently the composition $\partial_{\theta_n}\cdots\partial_{\theta_1}$ of left derivatives. It is linear, invariant under odd translations, satisfies integration by parts, and obeys the Fubini rule for iterated integration. Under a linear change of odd variables $\theta = N\eta$ it scales by $\det(N)^{-1}$, the inverse of the determinant of the change of variables, in contrast with the bosonic Jacobian.

The Gaussian integral over odd variables gives the Pfaffian, $\int e^{\frac12\theta^TA\theta}d\theta = \operatorname{Pf}(A)$ for an alternating matrix $A$, whose square is the determinant; the conjunction of the odd Gaussian with an ordinary Gaussian over even variables gives, up to $(2\pi)^{p/2}$, the inverse square root of the Berezinian, and the top-degree pairing of complementary exterior powers is perfect. The whole calculus is finite and algebraic.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity in which $2$ is invertible |
| $K$ | Field of characteristic different from $2$ |
| $\theta_1, \ldots, \theta_n$ | Odd generators; $\theta_i\theta_j = -\theta_j\theta_i$, $\theta_i^2 = 0$ |
| $\Lambda(\theta_1, \ldots, \theta_n)$ | Grassmann algebra, the exterior algebra on the odd generators |
| $\theta_I$, $I = \{i_1 < \cdots < i_k\}$ | Squarefree monomial; basis of $\Lambda(V)$, rank $2^n$ |
| $c_{\{1,\ldots,n\}}$ | Top coefficient of $f(\theta) = \sum_I c_I\theta_I$ |
| $\dfrac{\partial}{\partial\theta_i}$, $\dfrac{\overleftarrow{\partial}}{\partial\theta_i}$ | Left and right derivatives; differ by $(-1)^{k-1}$ in degree $k$ |
| $\int f\, d\theta = c_{\{1,\ldots,n\}} = \partial_{\theta_n}\cdots\partial_{\theta_1} f$ | Berezin integral |
| $\int f(\theta+\eta)\,d\theta = \int f(\theta)\,d\theta$ | Translation invariance for a constant odd shift $\eta$ |
| $\theta = N\eta \Rightarrow \int f\,d\theta = \det(N)^{-1}\int f(N\eta)\,d\eta$ | Berezinian change of variables; Jacobian factor is an inverse determinant |
| $\int e^{\frac12\theta^T A\theta}d\theta = \operatorname{Pf}(A)$ | Odd Gaussian integral |
| $\operatorname{Pf}(A)^2 = \det(A)$ | Determinant from the odd Gaussian |
| $(2\pi)^{p/2}(\det B)^{-1/2}\operatorname{Pf}(A)$ | Super-Gaussian; $(2\pi)^{p/2}\operatorname{Ber}(\operatorname{diag}(B,A))^{-1/2}$ |
| $\operatorname{Ber}\operatorname{diag}(B,A) = \det B/\operatorname{Pf}(A)^2$ | Berezinian of a block diagonal supermatrix |
| $\Lambda^k(V) \times \Lambda^{n-k}(V) \to R$, $(f,g)\mapsto \int fg\,d\theta$ | Perfect top-degree pairing |



## Further Reading

- F. A. Berezin, *The Method of Second Quantization* (Academic Press, 1966), for the original development of the Grassmann calculus and its integral.
- F. A. Berezin, *Introduction to Superanalysis* (Reidel, 1987), for Berezin differentiation and integration and the change-of-variables formula.
- Pierre Deligne and John W. Morgan, "Notes on Supersymmetry (following Joseph Bernstein)" (in *Quantum Fields and Strings: A Course for Mathematicians*, AMS, 1999), for the algebraic foundations of the odd calculus.
- V. S. Varadarajan, *Supersymmetry for Mathematicians: An Introduction* (AMS, 2004), for Berezin integration, the Pfaffian, and the Berezinian.
- Manfred Scheunert, *The Theory of Lie Superalgebras* (Springer, 1979), for the Grassmann algebra in the setting of superalgebra.
- Werner Greub, *Multilinear Algebra* (Springer, 2nd ed. 1978), for the exterior algebra, the Pfaffian, and the top-degree pairing used here.
- Yvonne Choquet-Bruhat and Cecile DeWitt-Morette, *Analysis, Manifolds and Physics, Part II* (North-Holland, 1989), for the Gaussian integral and the super-determinant with the analytic normalisations.
