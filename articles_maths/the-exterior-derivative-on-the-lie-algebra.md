
# __The Exterior Derivative on the Lie Algebra__

## Introduction

The Chevalley–Eilenberg differential $d$ is the operator on the graded space of cochains of a Lie algebra that turns the Lie bracket into a differential: on $n$-cochains it is given by the **Cartan formula**

$$
(df)(x_1,\dots,x_{n+1})=\sum_{i=1}^{n+1}(-1)^{i+1}x_i\cdot f(x_1,\dots,\widehat{x_i},\dots,x_{n+1})
+\sum_{i<j}(-1)^{i+j}f([x_i,x_j],x_1,\dots,\widehat{x_i},\dots,\widehat{x_j},\dots,x_{n+1}),
$$

and its square is zero. The complex, the cohomology and the interpretation of the low degrees are the subject of *Lie Algebra Cohomology*, where the differential is defined and the cohomology is computed; this article treats the differential as an **operator**. It presents the Cartan formula and its equivalence with the alternating-sum form, the derivation property of $d$ for the cup product that makes the cochains a differential graded algebra, the contraction by a vector and the Lie derivative with the **Cartan magic formula** $L_x=d\iota_x+\iota_x d$, and the algebra of commutation relations these operators satisfy. The exterior algebra and its products are *The Exterior Algebra*; the cochain complex and its cohomology are *Lie Algebra Cohomology*.

The article stays inside Part I and reasons with no smooth structure: the exterior derivative of a smooth manifold, the de Rham complex and the Cartan formula of differential geometry are named at the end and deferred to a later Part, and nothing of them is used. The base is a field $K$, the Lie algebra is written $\mathrm{G}$, the module of coefficients is $M$, the cochains are $C^n(\mathrm{G};M)=\operatorname{Hom}_K(\Lambda^n\mathrm{G},M)$, and the contraction and Lie derivative operators are written $\iota_x$ and $L_x$.

## The Cochain Complex and the Differential

### The Complex, Recalled

**Definition.** Let $\mathrm{G}$ be a Lie algebra over $K$ and let $M$ be a $\mathrm{G}$-module. The **cochains** are $C^n(\mathrm{G};M)=\operatorname{Hom}_K(\Lambda^n\mathrm{G},M)$, and the **differential** $d:C^n(\mathrm{G};M)\to C^{n+1}(\mathrm{G};M)$ is the operator displayed in the introduction, the module structure entering through the terms $x_i\cdot f(\dots)$.

The complex $(C^\bullet(\mathrm{G};M),d)$ and the cohomology $H^\bullet(\mathrm{G};M)$ are *Lie Algebra Cohomology*; the fact that $d$ is well defined on alternating maps, that $d^2=0$, and that the cohomology computes the extension groups are proved or recorded there.

### The Cartan Formula

**Proposition.** The differential is given by the **Cartan formula**

$$
(df)(x_1,\dots,x_{n+1})=\sum_{i=1}^{n+1}(-1)^{i+1}x_i\cdot f(x_1,\dots,\widehat{x_i},\dots,x_{n+1})
+\sum_{i<j}(-1)^{i+j}f([x_i,x_j],x_1,\dots,\widehat{x_i},\dots,\widehat{x_j},\dots,x_{n+1}),
$$

the hats omitting the argument; this is the sign convention fixed in *Lie Algebra Cohomology*.

**Corollary (trivial coefficients).** For the trivial module $M=K$ the first sum vanishes and $C^n(\mathrm{G};K)\cong\Lambda^n\mathrm{G}^*$; the differential is the transpose of the bracket, $(df)(x,y)=-f([x,y])$ on $\mathrm{G}^*$, extended as the graded derivation of the next section.

**Proof.** The vanishing of the action terms is immediate; the transposition statement is the definition read in degree one, and its extension is the derivation property proved below. $\square$

### The Square of the Differential

**Theorem.** $d\circ d=0$.

**Proof.** This is the proposition of *Lie Algebra Cohomology*; in the operator reading it is the statement that the differential is a differential, and its proof is the Jacobi identity applied to the bracket terms, the action terms cancelling between the two sums. $\square$

**Verified.** For $\mathrm{SL}(2,K)$ with basis $e,h,f$ and trivial coefficients, the differential was built on the basis cochains of degrees $0,1,2$ and $d^2=0$ was confirmed by exact Gaussian elimination over $\mathbb{Q}$; the ranks are $0,3,0$ in degrees $0,1,2$, so $H^1=H^2=0$ and $H^0,H^3$ are one-dimensional, in agreement with the computation recorded in *Lie Algebra Cohomology*.

## The Differential as a Derivation of the Cup Product

### The Cup Product

**Definition.** The **cup product** of cochains $\alpha\in C^p(\mathrm{G};K)$ and $\beta\in C^q(\mathrm{G};K)$ with trivial coefficients is the cochain

$$
(\alpha\smile\beta)(x_1,\dots,x_{p+q})=\sum_{\sigma}\operatorname{sgn}(\sigma)\,\alpha(x_{\sigma(1)},\dots,x_{\sigma(p)})\,\beta(x_{\sigma(p+1)},\dots,x_{\sigma(p+q)}),
$$

the sum over the $(p,q)$-shuffles of the symmetric group. Under the identification $C^\bullet(\mathrm{G};K)=\Lambda^\bullet\mathrm{G}^*$ the cup product is the wedge product of *The Exterior Algebra*.

### The Derivation Property

**Theorem.** The differential is a graded derivation of degree one for the cup product:

$$
d(\alpha\smile\beta)=d\alpha\smile\beta+(-1)^{p}\,\alpha\smile d\beta,\qquad \alpha\in C^p(\mathrm{G};K).
$$

**Proof.** With trivial coefficients the statement is the product rule for the differential on the exterior algebra of $\mathrm{G}^*$; both sides are alternating and bilinear, so it suffices to check on basis cochains, where the two sums over the pairs of a $(p+q+1)$-tuple split according to whether the pair meets the first $\alpha$-block or the second. $\square$

**Corollary.** With trivial coefficients the cochains form a **differential graded algebra**: a graded associative algebra with a degree-one derivation of square zero. The cohomology $H^\bullet(\mathrm{G};K)$ inherits the product, which is graded-commutative, and is the subject of *Lie Algebra Cohomology*.

## Contraction, Lie Derivative and the Magic Formula

### Contraction by a Vector

**Definition.** For $x\in\mathrm{G}$ the **contraction** is the operator

$$
\iota_x:C^n(\mathrm{G};M)\longrightarrow C^{n-1}(\mathrm{G};M),\qquad (\iota_x f)(x_1,\dots,x_{n-1})=f(x,x_1,\dots,x_{n-1}).
$$

It lowers the degree by one and satisfies $\iota_x\circ\iota_x=0$; it is a graded derivation of degree $-1$ for the cup product.

### The Lie Derivative and the Magic Formula

**Definition.** The **Lie derivative** along $x$ is the degree-zero operator

$$
L_x=d\,\iota_x+\iota_x\,d .
$$

**Theorem (Cartan magic formula).** The Lie derivative is the operator induced by the adjoint action: for a cochain $f$ and the action of $x$ on the coefficients,

$$
L_x f = x\cdot f,
$$

and it satisfies the operator identities

$$
L_x=d\iota_x+\iota_x d,\qquad [L_x,d]=0,\qquad [L_x,\iota_y]=\iota_{[x,y]},\qquad [L_x,L_y]=L_{[x,y]},\qquad [\iota_x,\iota_y]=0 .
$$

**Proof.** The magic formula is the definition of $L_x$; the remaining identities are the standard consequences of $d^2=0$ and of the derivation property, each checked by expanding the commutators of the operators $d,\iota_x,\iota_y$ acting on a cochain and using the Jacobi identity. $\square$

**Corollary.** The operators $d,\iota_x,L_x$ form the **Cartan calculus** of the cochain complex: $d$ raises the degree, the contractions lower it,$L_x$ preserves it, and the contraction and Lie derivative give a representation of the Lie algebra $\mathrm{G}$ together with the differential.

## Coefficients in the Adjoint Module

**Proposition.** For the adjoint module $M=\mathrm{G}$ the differential has the same Cartan form with the action $x\cdot m=[x,m]$, and the contraction and Lie derivative are formed with the same formulas; the degree-one cochains are the operators $\mathrm{G}\to\mathrm{G}$, the closed ones are the derivations of *Derivations of a Lie Algebra*, and the exact ones are the inner derivations.

**Proof.** This is the identification recorded in *Lie Algebra Cohomology*: the cocycle condition $d\delta=0$ is the Leibniz rule for the bracket, and the coboundaries are the operators $\operatorname{ad}_x$; the operator reading is the one given above. $\square$

## The Exterior Derivative of a Manifold, Named

**Remark (forward reference).** On a smooth manifold the sign rule and the square-zero property of the above differential are the algebraic part of the exterior derivative of differential forms, and the identities of the Cartan calculus are the same operator identities with $x$ a vector field and $\iota_x$ the interior product; the smooth structure, the de Rham complex and the integration theory belong to a later Part and are not used here. The exterior derivative of the Lie algebra is the algebraic prototype, and the whole of the Cartan calculus is a theorem about operators on a graded space.

## Summary

The **Chevalley–Eilenberg differential** is the operator $d:C^n(\mathrm{G};M)\to C^{n+1}(\mathrm{G};M)$ given by the Cartan formula, the sum of the action terms and the bracket terms with alternating signs; its square is zero and the complex it defines is owned by *Lie Algebra Cohomology*. With trivial coefficients the cochains are the exterior algebra on the dual, the differential is the transpose of the bracket, and the differential is a graded derivation of degree one for the cup product, so the cochains form a differential graded algebra. The contraction $\iota_x$ lowers the degree, is square-zero and is a graded derivation, and the Lie derivative $L_x=d\iota_x+\iota_x d$ is the operator of the adjoint action; the two, with $d$, satisfy the Cartan calculus $[L_x,d]=0$, $[L_x,\iota_y]=\iota_{[x,y]}$, $[L_x,L_y]=L_{[x,y]}$ and $[\iota_x,\iota_y]=0$. With coefficients in the adjoint module the closed one-cochains are the derivations and the exact ones the inner derivations. For $\mathrm{SL}(2,K)$ the differential has ranks $0,3,0$ in degrees $0,1,2$ with trivial coefficients, so $H^1=H^2=0$. The exterior derivative of a smooth manifold is the same operator with a smooth structure added, and is deferred.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | the base field |
| $\mathrm{G}$ | a Lie algebra over $K$ |
| $M$ | a $\mathrm{G}$-module of coefficients |
| $C^n(\mathrm{G};M)=\operatorname{Hom}_K(\Lambda^n\mathrm{G},M)$ | the $n$-cochains |
| $d$ | the Chevalley–Eilenberg differential, the exterior derivative |
| $\iota_x$ | contraction by $x\in\mathrm{G}$ |
| $L_x=d\iota_x+\iota_x d$ | the Lie derivative along $x$ |
| $\smile$ | the cup product, the wedge product on $\Lambda^\bullet\mathrm{G}^*$ |
| $H^\bullet(\mathrm{G};M)$ | the cohomology (owned by *Lie Algebra Cohomology*) |

## Further Reading

- Claude Chevalley and Samuel Eilenberg, "Cohomology theory of Lie groups and Lie algebras", *Transactions of the American Mathematical Society* 63 (1948), 85–124, for the complex and the differential.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the cochain complex and the Cartan calculus of a Lie algebra.
- Jean-Pierre Serre, *Lie Algebras and Lie Groups*, Lecture Notes in Mathematics 1500 (Springer, 1992), for the differential and the low-degree identifications.
- Charles A. Weibel, *An Introduction to Homological Algebra*, Cambridge Studies in Advanced Mathematics 38 (Cambridge University Press, 1994), for the differential graded algebra structure.
- Werner Greub, Stephen Halperin and Ray Vanstone, *Connections, Curvature and Cohomology*, Volume I (Academic Press, 1972), for the Cartan calculus and its relation to the manifold theory.
