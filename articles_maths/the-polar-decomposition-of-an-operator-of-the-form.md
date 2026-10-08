# __The Polar Decomposition of an Operator of the Form__

## Introduction

Every operator of a definite form factors as a **modulus** and a **phase**, $T = U\lvert T\rvert$, where the modulus $\lvert T\rvert = (T^{\dagger}T)^{1/2}$ is self-adjoint and positive and the phase $U$ is an isometry from the range of the modulus onto the range of the operator. The decomposition is the operator form of the polar form $z = r e^{\mathrm{i}\theta}$ of a scalar: the modulus carries the size, the phase the direction, and the two are read off from the single positive operator $T^{\dagger}T$ by the square root of the spectral theorem. It is the sharpest illustration of the definite theory of *The Spectra of Self-Adjoint Operators of the Form*, because it uses the two properties that definiteness alone supplies: the positivity of $T^{\dagger}T$, which rests on $h(T^{\dagger}Tx,x) = h(Tx,Tx) \geq 0$, and the existence of the positive square root, which rests on the functional calculus.

Three facts organise the article. The **modulus exists and is unique**: the product $T^{\dagger}T$ is self-adjoint, it is positive in the definite case, and a positive self-adjoint operator has exactly one positive self-adjoint square root, so $\lvert T\rvert$ is that square root and it satisfies $\lVert \lvert T\rvert x\rVert = \lVert Tx\rVert$ and $\ker\lvert T\rvert = \ker T$. The **phase is an isometry of the ranges**: the assignment $U(\lvert T\rvert x) = Tx$ is well defined and isometric on the range of the modulus, extends by continuity to its closure, and is set to zero on the kernel, giving the relations $T = U\lvert T\rvert$, $\lvert T\rvert = U^{\dagger}T$, with $U^{\dagger}U$ the projection onto the closure of the range of $\lvert T\rvert$ and $UU^{\dagger}$ the projection onto the closure of the range of $T$. And the decomposition **fails in the indefinite case** for the same reason the spectral theorem does: $T^{\dagger}T$ is no longer positive, and the hyperbolic plane supplies an operator whose modulus would have to be $\mathrm{i}$ times the identity.

The article recalls the positive operators and defines the modulus, constructs the phase and proves the decomposition and its uniqueness, develops the invertible case in which the phase is unitary, states the indefinite obstruction, and works the field and the matrices. The completion-level companion, in which the decomposition is that of the Tomita operator and of the intertwiners of the representation, is *The Modular Structure of a Hermitian Algebra*. The positivity criterion and the square root are *The Spectra of Self-Adjoint Operators of the Form*, §*The Positivity Criterion*; the adjoint and its properties are *The Adjoint under a Hermitian Form*; the norm identity $\lVert Tx\rVert = \lVert \lvert T\rvert x\rVert$ is the norm of *The Norm Defined by a Form*; the indefinite transport is *The Fundamental Symmetry of the Form*; the bilinear counterpart is *Positivity and the Hermitian Cone of a Hermitian Algebra with Hermitian Adjoint*. Throughout, $A$ is a sesqualgebra with a form in the definite case over a base $(R,\varsigma)$ of one of the two classical kinds of *The Norm Defined by a Form*, with fixed field $k = R^{\varsigma}$ and $R$ complete, $A$ is free of finite rank over $k$ or $k(\mathrm{i})$, $h$ is Hermitian, compatible, nonsingular and **positive definite**, and the operators are the $R$-linear endomorphisms of $A$.

## The Positive Operators of the Form

A self-adjoint operator is **positive** when $h(Tx,x) \geq 0$ for every $x$, and **strictly positive** when $h(Tx,x) > 0$ for every $x \neq 0$; by the **positivity criterion** of *The Spectra of Self-Adjoint Operators of the Form*, §*The Positivity Criterion*, in the definite finite-dimensional case this is exactly the condition that the spectrum lies in $[0,\infty)$, and the positive operators are the operators whose diagonal is nonnegative.

### The Self-Adjoint Products

**Proposition (the two products).** For every operator $T$ the products $T^{\dagger}T$ and $TT^{\dagger}$ are self-adjoint, and they have the same spectrum away from zero.

*Proof.* The adjoint of $T^{\dagger}T$ is $T^{\dagger}(T^{\dagger})^{\dagger} = T^{\dagger}T$, and likewise for $TT^{\dagger}$. If $T^{\dagger}Tx = \lambda x$ with $\lambda \neq 0$, then $x = \lambda^{-1}T^{\dagger}Tx$ lies in the range of $T^{\dagger}$, and $T(T^{\dagger}Tx) = \lambda Tx$ shows that $\lambda$ is an eigenvalue of $TT^{\dagger}$ with eigenvector $Tx \neq 0$; the argument is symmetric in the two products. $\square$

**Proposition (the positivity).** Let $h$ be definite. Then $T^{\dagger}T$ is positive,

$$
h(T^{\dagger}Tx,x) = h(Tx,Tx) = \lVert Tx\rVert^{2} \geq 0 \qquad \text{for all } x ,
$$

and the kernel of $T^{\dagger}T$ is the kernel of $T$.

*Proof.* The identity is $h(T^{\dagger}Tx,x) = h(Tx,(T^{\dagger})^{\dagger}x) = h(Tx,Tx)$, by the defining relation of the adjoint. The kernel statement follows: $T^{\dagger}Tx = 0$ implies $\lVert Tx\rVert^{2} = h(T^{\dagger}Tx,x) = 0$, so $Tx = 0$ by the definiteness of the norm, and the converse is immediate. $\square$

### The Square Root

**Theorem (the positive square root).** Let $h$ be definite, $A$ finite-dimensional over $k$ or $k(\mathrm{i})$, and let $S$ be a positive self-adjoint operator. Then there is exactly one positive self-adjoint operator $S^{1/2}$ with $(S^{1/2})^{2} = S$, and it is a function of $S$ in the functional calculus of *The Spectra of Self-Adjoint Operators of the Form*, $S^{1/2} = \sum_{i}\lambda_{i}^{1/2}P_{i}$.

*Proof.* The eigenvalues $\lambda_{i}$ of the positive self-adjoint $S$ are real and nonnegative by the positivity criterion of *The Spectra of Self-Adjoint Operators of the Form*, §*The Positivity Criterion*, so their square roots $\lambda_{i}^{1/2}$ are real and nonnegative and $S^{1/2} = \sum_{i}\lambda_{i}^{1/2}P_{i}$ is positive self-adjoint with square $S$ by the orthogonality of the projections. If $R$ is positive self-adjoint with $R^{2} = S$, then $R$ commutes with $S = R^{2}$ and hence with every projection $P_{i}$ and with $S^{1/2}$; on the eigenspace of $\lambda_{i}$ the operator $R$ has square $\lambda_{i}$ and is positive, so its eigenvalue there is $\lambda_{i}^{1/2}$, and $R = S^{1/2}$. $\square$

### The Modulus

**Definition.** The **modulus** of $T$ is $\lvert T\rvert = (T^{\dagger}T)^{1/2}$, and the **absolute value** of the operator is the operator $\lvert T\rvert$ so defined.

**Proposition (the modulus is an isometry of norms).** For every $x$, $\lVert \lvert T\rvert x\rVert = \lVert Tx\rVert$; the kernel of $\lvert T\rvert$ is the kernel of $T$; and the closure of the range of $\lvert T\rvert$ is carried isometrically onto the closure of the range of $T$.

*Proof.* The first identity is $\lVert \lvert T\rvert x\rVert^{2} = h(\lvert T\rvert^{2}x,x) = h(T^{\dagger}Tx,x) = \lVert Tx\rVert^{2}$; the second is the kernel statement of the positivity proposition applied to $\lvert T\rvert$; the third is the construction of the phase in the next section, which is isometric on the range of $\lvert T\rvert$ and extends to the closures. $\square$

## The Polar Decomposition

### The Isometry on the Range

**Theorem (the phase is well defined and isometric).** The formula

$$
U(\lvert T\rvert x) = Tx \qquad x \in A ,
$$

defines an $R$-linear isometry from the range of $\lvert T\rvert$ onto the range of $T$, and it extends by continuity to an isometry from the closure of the range of $\lvert T\rvert$ onto the closure of the range of $T$; setting $U = 0$ on the kernel of $\lvert T\rvert$ gives an operator $U \in B(A)$.

*Proof.* If $\lvert T\rvert x = \lvert T\rvert x_{1}$ then $\lvert T\rvert(x - x_{1}) = 0$, so $T(x - x_{1}) = 0$ by the kernel proposition, and $Tx = Tx_{1}$: the formula is well defined. It is $R$-linear by the linearity of $\lvert T\rvert$ and of $T$, and it is isometric because $\lVert U(\lvert T\rvert x)\rVert = \lVert Tx\rVert = \lVert \lvert T\rvert x\rVert$. A uniformly continuous map on a dense subspace of a complete object extends uniquely to the closure, and the kernel is the $h$-orthogonal complement of the closure of the range, on which $U$ is set to zero. $\square$

### The Decomposition and Its Properties

**Theorem (the polar decomposition).** With $\lvert T\rvert$ the modulus and $U$ the phase of the theorem above,

$$
T = U\lvert T\rvert , \qquad \lvert T\rvert = U^{\dagger}T , \qquad U^{\dagger}U = P_{\mathrm{ran}\lvert T\rvert} , \qquad UU^{\dagger} = P_{\mathrm{ran}T} ,
$$

where $P_{\mathrm{ran}\lvert T\rvert}$ and $P_{\mathrm{ran}T}$ are the $h$-orthogonal projections onto the closures of the corresponding ranges. The pair $(\lvert T\rvert, U)$ is the unique pair with $\lvert T\rvert$ positive self-adjoint, $U$ an isometry on the range of $\lvert T\rvert$ and $U = 0$ on its kernel.

*Proof.* The identity $T = U\lvert T\rvert$ is the definition of $U$ on the range of $\lvert T\rvert$, and both sides vanish on the kernel. For the second, $U^{\dagger}U$ is the projection onto the closure of the range of $\lvert T\rvert$, so $U^{\dagger}T = U^{\dagger}U\lvert T\rvert = \lvert T\rvert$. The two projection relations are the two halves of the isometry statement, $U^{\dagger}U$ being the identity on the initial space and $UU^{\dagger}$ the identity on the final space. For the uniqueness, if $T = V S$ with $S$ positive self-adjoint and $V$ an isometry vanishing on $\ker S$, then $T^{\dagger}T = SV^{\dagger}VS = S^{2}$, so $S = (T^{\dagger}T)^{1/2} = \lvert T\rvert$ by the uniqueness of the square root, and $V = U$ on the range of $\lvert T\rvert$ and on its kernel, hence everywhere. $\square$

**Corollary (the isometry and the co-isometry).** The phase $U$ is an isometry, $U^{\dagger}U = 1$, exactly when $\lvert T\rvert$ is injective, that is when $T$ is injective; it is a co-isometry, $UU^{\dagger} = 1$, exactly when $T$ is surjective. In finite dimension the two conditions coincide.

*Proof.* The projection $P_{\mathrm{ran}\lvert T\rvert}$ is the identity exactly when the range of $\lvert T\rvert$ is all of $A$, which is the injectivity of $\lvert T\rvert$ in finite dimension, and the kernel of $\lvert T\rvert$ is the kernel of $T$; the second clause is the same for $UU^{\dagger}$. $\square$

### The Unitary Case

**Theorem (the invertible case).** Let $T$ be invertible. Then $\lvert T\rvert$ is invertible, $U = T\lvert T\rvert^{-1}$ is **unitary**, and the decomposition is the product of the unitary polar factor by the modulus.

*Proof.* The identity $\lVert \lvert T\rvert x\rVert = \lVert Tx\rVert$ makes $\lvert T\rvert$ injective exactly when $T$ is, and in finite dimension injective is invertible; then $U = T\lvert T\rvert^{-1}$ and $U^{\dagger}U = \lvert T\rvert^{-1}T^{\dagger}T\lvert T\rvert^{-1} = \lvert T\rvert^{-1}\lvert T\rvert^{2}\lvert T\rvert^{-1} = 1$, and symmetrically $UU^{\dagger} = 1$. $\square$

**Remark (the decomposition does not see the form once the phase is unitary).** In the invertible case the modulus is the unique positive factor and the phase is unitary, so the polar decomposition is the algebraic form of the polar form of a complex number; in the non-invertible case the phase is only a partial isometry and the two projections record the loss of injectivity and of surjectivity. The article keeps the partial-isometry form because the operators of the layer are not assumed invertible, and the decomposition of an operator that is not invertible is the partial-isometry one; the finite-rank operators of *The Completion of a Sesqualgebra with a Form*, §*The Finite-Rank Operators*, are the model in which the kernel and the cokernel of an operator are visible, and the invertible case is the corollary in which both projections are the identity.

## The Indefinite Case

### The Transport of the Products

Let the form be indefinite with symmetry $J$ and companion form, so that $T^{\dagger} = JT^{*}J$, as in *The Fundamental Symmetry of the Form*, §*The Adjoints under the Two Forms*. The product $T^{\dagger}T = JT^{*}JT$ is still self-adjoint for $h$, but it is no longer positive: the identity $h(T^{\dagger}Tx,x) = h(Tx,Tx)$ still holds, and the right side is the squared length of $Tx$ in the **indefinite** form, which can be negative.

**Proposition (the obstruction).** In the indefinite case $T^{\dagger}T$ can be negative definite, in which case it has no positive self-adjoint square root and the polar decomposition of $T$ does not exist for the form $h$.

*Proof.* The square root of a negative definite self-adjoint operator is purely imaginary and not positive, and the uniqueness of the positive square root fails because there is no positive square root at all. $\square$

**Example (the hyperbolic obstruction).** On $\mathbb{R}^{2}$ with $h(x,y) = x_{1}y_{1} - x_{2}y_{2}$ and $J = \operatorname{diag}(1,-1)$, the operator $T = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$ has $T^{\dagger} = T$ and $T^{2} = -\mathrm{id}$, so $T^{\dagger}T = -\mathrm{id}$ is negative definite and the modulus of $T$ for $h$ would have to be $\mathrm{i}$ times the identity, which is not positive self-adjoint. The operator does have a polar decomposition for the **companion** form, which is euclidean here, because $T$ is orthogonal: the companion modulus is $\mathrm{id}$ and the companion phase is $T$ itself. It has none for the form $h$. The example is the smallest witness that the polar decomposition, like the spectral theorem, is a definite-case statement.

### The $J$-Polar Decomposition

For an operator whose product $T^{\dagger}T$ is **definitizable** — some nonzero real polynomial in it is positive for the indefinite form — the functional calculus again supplies a square root and a phase, taken with respect to the companion form, and the result is the **$J$-polar decomposition** of the indefinite theory. The construction, its uniqueness and its relation to the $J$-unitary group are the content of *J-Self-Adjoint and J-Unitary Operators* and of *Definitizable Operators and the Krein–Naĭmark Theorem*; they are not developed here.

## Worked Cases

### The Field

**Example (the field).** Let $A = \mathbb{C}$ with $h(z,w) = z\overline{w}$ and let $T_{\lambda}$ be the multiplication by $\lambda$. Then $T_{\lambda}^{\dagger}T_{\lambda} = T_{\lvert\lambda\rvert^{2}}$, so $\lvert T_{\lambda}\rvert = T_{\lvert\lambda\rvert}$ and the phase is $U = T_{\lambda/\lvert\lambda\rvert}$ for $\lambda \neq 0$, of modulus one and unitary; for $\lambda = 0$ the modulus is zero and the phase is zero, so the decomposition reads $T_{0} = 0 \cdot T_{0}$. The example is the scalar polar form $z = r e^{\mathrm{i}\theta}$ read as an operator identity, and it is the smallest in which the modulus, the phase and the unitary case are visible at once.

### The Matrices

**Example (the matrices).** Let $A = M_{n}(\mathbb{C})$ with the trace form $h(X,Y) = \operatorname{tr}(XY^{*})$ and let $m_{Z}$ be the left multiplication by $Z$. Since $Z \mapsto m_{Z}$ is an algebra homomorphism and the functional calculus is multiplicative under a homomorphism, $\lvert m_{Z}\rvert = m_{\lvert Z\rvert}$ with $\lvert Z\rvert = (Z^{*}Z)^{1/2}$ the matrix modulus, and the phase is $m_{Z}\lvert m_{Z}\rvert^{-1} = m_{Z\lvert Z\rvert^{-1}}$ when $Z$ is invertible. The unitary polar factor $Z\lvert Z\rvert^{-1}$ is the unitary of the classical polar decomposition of the matrix $Z$, and the example is the model in which the operator polar decomposition is read on the algebra as the matrix one. The Cauchy–Schwarz identity $\operatorname{tr}(\lvert Z\rvert^{2}) = \operatorname{tr}(Z^{*}Z)$ is the norm identity of the modulus, and it is the Frobenius norm of *The Norm Defined by a Form*, §*The Matrix Algebra*.

## Summary

The **modulus** of an operator of a definite form is $\lvert T\rvert = (T^{\dagger}T)^{1/2}$, the unique positive self-adjoint square root of the positive self-adjoint product $T^{\dagger}T$, and it satisfies $\lVert \lvert T\rvert x\rVert = \lVert Tx\rVert$ and $\ker\lvert T\rvert = \ker T$. The **phase** is defined on the range of the modulus by $U(\lvert T\rvert x) = Tx$, it is isometric there, it extends by continuity to the closure and by zero on the kernel, and the **polar decomposition** $T = U\lvert T\rvert$ holds with $\lvert T\rvert = U^{\dagger}T$ and the two projection relations $U^{\dagger}U = P_{\mathrm{ran}\lvert T\rvert}$, $UU^{\dagger} = P_{\mathrm{ran}T}$; the pair is unique. The phase is an isometry exactly when $T$ is injective and a co-isometry exactly when $T$ is surjective, and if $T$ is **invertible** the phase $U = T\lvert T\rvert^{-1}$ is **unitary**. In the **indefinite** case the product $T^{\dagger}T$ is no longer positive — the hyperbolic plane gives $T^{\dagger}T = -\mathrm{id}$ — and the decomposition exists only for the definitizable operators, as the **$J$-polar decomposition** of the Krein layer.

## Summary of Notation

| symbol | meaning |
|---|---|
| $T^{\dagger}T$, $TT^{\dagger}$ | the two self-adjoint products of an operator and its adjoint |
| $h(T^{\dagger}Tx,x) = \lVert Tx\rVert^{2}$ | the positivity of the product, in the definite case |
| $\lvert T\rvert = (T^{\dagger}T)^{1/2}$ | the modulus, the positive self-adjoint square root |
| $S^{1/2} = \sum_{i}\lambda_{i}^{1/2}P_{i}$ | the positive square root by the functional calculus |
| $\lVert \lvert T\rvert x\rVert = \lVert Tx\rVert$ | the modulus is an isometry of norms |
| $U(\lvert T\rvert x) = Tx$ | the definition of the phase on the range of the modulus |
| $T = U\lvert T\rvert$ | the polar decomposition |
| $U^{\dagger}U = P_{\mathrm{ran}\lvert T\rvert}$, $UU^{\dagger} = P_{\mathrm{ran}T}$ | the two partial isometry projections |
| $U = T\lvert T\rvert^{-1}$ | the unitary phase in the invertible case |
| $T^{\dagger}T = -\mathrm{id}$ | the hyperbolic obstruction to the indefinite polar decomposition |

## Further Reading

- John B. Conway, *A Course in Functional Analysis* (2nd ed., Springer, 1990), for the positive square root of a self-adjoint operator and the polar decomposition.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the partial isometries and the polar decomposition in an algebra of operators.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed. (Cambridge University Press, 2013), for the matrix polar decomposition, the unitary polar factor and the singular values.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the $J$-polar decomposition and the definitizable operators.
- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for the obstruction to the polar decomposition of an operator of an indefinite inner product.
- Paul R. Halmos, *A Hilbert Space Problem Book* (2nd ed., Springer, 1982), for the partial isometries and their range and kernel projections.
