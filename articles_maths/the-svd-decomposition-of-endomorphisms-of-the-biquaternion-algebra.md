# __The SVD Decomposition of Endomorphisms of the Biquaternion Algebra__

## Introduction

**The question.** An endomorphism of the biquaternion algebra is a complex-linear map $F:\mathbb{B}\to\mathbb{B}$, with no condition of preserving the product. The algebra has complex dimension four, so the endomorphisms form the complex vector space $\operatorname{End}(\mathbb{B})=\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ of complex dimension sixteen. The question of this article is the following. *What is the shortest way to write an endomorphism as a sum of endomorphisms of rank one, and what are the weights of the terms?*

**The answer.** Four terms at most, and the weights are the square roots of the eigenvalues of $F^{*}F$:

$$
F=\sum_{k=1}^{4}\rho_k\,\mathcal P_{\tilde U_k,\tilde V_k},
\qquad
\rho_1\geq\rho_2\geq\rho_3\geq\rho_4\geq0,
\qquad
F(\tilde V_k)=\rho_k\tilde U_k ,
$$

with the two families $\tilde U_1,\dots,\tilde U_4$ and $\tilde V_1,\dots,\tilde V_4$ orthonormal for the Hermitian form, and $\mathcal P_{\tilde U_1,\tilde U_2}(\tilde X)=\tilde U_1\langle\tilde X,\tilde U_2\rangle_{*}$. Four is the complex dimension of the algebra, so the bound is the dimension and not a property of the map; the content is that four terms always suffice and that the weights and the two families can be chosen at once.

**Three things the algebra contributes.** The decomposition above is the singular value decomposition of a linear map of a four-dimensional complex space with a scalar product into itself, and as such it holds in $\mathbb{C}^{4}$ as well. What follows is what the biquaternion algebra adds to it, and it is the reason the article is written on $\mathbb{B}$ and not on $\mathbb{C}^{4}$. First, the algebra carries **two** distinguished real quadratic forms and only one of them can carry weights: the Hermitian norm is definite and the quaternionic norm is multiplicative, so the weights measure the element twice, their squares summing to the first and their product giving the modulus of the second (§*The Two Norms of an Element*, §*The Weights of One Multiplier*). Second, the product meets the decomposition on the zero-divisor cone and not on the whole cone of the atoms: a two-sided operator $L_{\tilde Q_1}R_{\tilde Q_2}$ with two zero-divisor multipliers has rank one, but an elementary endomorphism is a two-sided operator only when both of its vectors are zero divisors, so the generic atom of a decomposition is not a product (§*The Rank-One Endomorphisms and the Products*). Third, the weights of a two-sided operator are the four products of two pairs, one pair from each multiplier, and this is why no two-sided operator has rank three (§*The Weights of Two Multipliers*).

**The method.** The article proceeds in two stages, and the order matters. The first stage is the analysis of $\mathbb{B}$ as a complex Hilbert space of dimension four: the Hermitian form, the adjoint of an endomorphism, the spectral theorem for the self-adjoint positive semidefinite operators, the decomposition into rank-one terms and its operator form with two unitaries and a scale, the weights, the truncation. The multiplication of the algebra does not enter this stage, and the stage would read the same on any four-dimensional complex Hilbert space. The second stage brings the multiplication in, and it is the stage that makes the article a chapter of the biquaternion theory: the rank-one endomorphisms that are products are identified with the pairs of degenerate multipliers, the two-sided operators are read through the weights of their two multipliers, and the pattern of the weights is explained in the $2\times2$ model.

**The letters.** $F$ and $G$ are endomorphisms and $F^{*}$ is the adjoint of $F$; the elements are $\tilde Q$, $\tilde Q_1$, $\tilde Q_2$, $\tilde X$, $\tilde Y$, and the multipliers of a two-sided operator keep the tilde, $L_{\tilde Q_1}R_{\tilde Q_2}$. The elementary endomorphisms carry $\mathcal P$; the two unitary operators of the operator form carry $\mathcal U$ and $\mathcal V$ and the scale carries $\Sigma$, with $\Pi_i$ its spectral projectors, and the caligraphic letters keep the operators apart from the unit elements $U$ of *Norm and Unitary Conventions* and from the families $\tilde U_k$. The Hermitian factors of the polar decomposition of an element carry $\tilde H$, with a subscript when the two multipliers are distinguished. The weights carry $\rho$ with the object in the parenthesis, $\rho_k(F)$ for an endomorphism and $\rho_1(\tilde Q),\rho_2(\tilde Q)$ for an element, $\mathrm{I}_4$ is the identity operator, $\operatorname{Sc}$ the scalar part, $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$ the Hermitian form and $N$ the quaternionic algebraic norm. The letters of the four operator families are those of *Operator Family Conventions*: $L$, $R$, $LR$ and $\Theta$. The two families of the decomposition carry $\tilde U_k$ and $\tilde V_k$, and the letters assert only that the element belongs to a family orthonormal for the Hermitian form: they say nothing of its multiplicative character, which is the distinction drawn in §*The Two Norms of an Element*.

**The order of the article.** The carrier and its Hermitian form come first, with the two norms and the Riesz identification (§*The Carrier*). The endomorphisms follow, with their adjoints and with the two-sided family (§*The Endomorphisms*). The spectral theorem is stated and proved, because the article uses it and does not import it (§*The Spectral Theorem*). The decomposition is then stated and proved, with its operator form, the elementary endomorphisms and their normalisation (§*The Decomposition*). The weights are examined in their own section, with the rank cases, the three identities, the geometric reading, the non-uniqueness and the truncation (§*The Weights*). The multiplication enters last, and it rewrites the result: which atoms are products, the one-sided weights, the two-sided weights, the two-sided operator, and the sixteen basis operators, and it closes by naming what the decomposition is not (§*The Multiplication's Share*).

**Boundaries.** The algebra, its units and its multiplication are *The Biquaternion Algebra*; the element, its coefficients and its four conjugations are *The Element, the Coordinates and the Conjugations in the Biquaternion Algebra*; the endomorphisms as a space are *The Endomorphisms of the Biquaternion Algebra*; the two-sided operators as a family, with their composition law and their plain adjoint, are *Operators Acting on Two Sides*; the $2\times2$ model is *Matrix Representations Conventions* and *$M_2(\mathbb{C})$ Pauli Representation*; the forms and the norms are *Product and Form Conventions* and *Norm and Unitary Conventions*. The article is self-contained in what it proves: the Hermitian form is defined in §*The Carrier*, the spectral theorem is proved in §*The Spectral Theorem*, and the two-sided family is defined in §*The Two-Sided Operators and Their Adjoints* before it is used. The matrix model appears once, in §*The Weights Are Products in the Model*, and only to explain a pattern that the element level has already stated.

## The Carrier

### The Element and Its Two Conjugations

**The units.** The algebra $\mathbb{B}$ is the complex algebra with unit $e_t$ and three further units $\vec e_x,\vec e_y,\vec e_z$ subject to

$$
\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t,\qquad
\vec e_x\vec e_y=\vec e_z,\quad \vec e_y\vec e_z=\vec e_x,\quad \vec e_z\vec e_x=\vec e_y ,
$$

the products read cyclically and the reversed products being the negatives. An element is $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ with complex coefficients $Q_\mu=q_\mu+iq'_\mu$, and the four units are a complex basis. The algebra is $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, hence $M_2(\mathbb{C})$, and its complex dimension is four.

**The two conjugations.** The **quaternion conjugation** is $\tilde Q^{\natural}=Q_te_t-Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z$, complex-linear, involutive and an involution of the algebra, $(\tilde Q_1\tilde Q_2)^{\natural}=\tilde Q_2^{\natural}\tilde Q_1^{\natural}$. The **Hermitian conjugation** is $\tilde Q^{*}=\bar Q_te_t-\bar Q_x\vec e_x-\bar Q_y\vec e_y-\bar Q_z\vec e_z$, the coefficient conjugation of the quaternion conjugation, conjugate-linear, involutive and also order-reversing, $(\tilde Q_1\tilde Q_2)^{*}=\tilde Q_2^{*}\tilde Q_1^{*}$. The two agree on the elements with real coefficients, and the star is the one that pairs with a definite form, which is why the whole article is written with it.

**The scalar part.** Expanding a product and keeping the unit term,

$$
\operatorname{Sc}(\tilde Q_1\tilde Q_2)=Q_{1t}Q_{2t}-Q_{1x}Q_{2x}-Q_{1y}Q_{2y}-Q_{1z}Q_{2z},
$$

and with $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ the complex square of the vector part. The scalar part is central and cyclic, $\operatorname{Sc}(\tilde Q_1\tilde Q_2\tilde Q_3)=\operatorname{Sc}(\tilde Q_2\tilde Q_3\tilde Q_1)$, and it is invariant under the quaternion conjugation, $\operatorname{Sc}(\tilde Q^{\natural})=\operatorname{Sc}(\tilde Q)$. The two facts are used in every computation that follows, and the cyclicity is what makes the adjoint of a two-sided operator computable in one line.

### The Hermitian Form

**The form.** The algebra carries the **Hermitian form**

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\operatorname{Sc}(\tilde Q_1\tilde Q_2^{*})=\sum_{\mu}Q_{1\mu}\overline{Q_{2\mu}} ,
$$

the sum running over $\mu=t,x,y,z$, linear in the first argument, conjugate-linear in the second, and definite:

$$
\langle\tilde Q,\tilde Q\rangle_{*}=\lvert Q_t\rvert^{2}+\lvert Q_x\rvert^{2}+\lvert Q_y\rvert^{2}+\lvert Q_z\rvert^{2},
$$

which vanishes only at $\tilde Q=0$. The **Hermitian norm** is $\lVert\tilde Q\rVert^{2}=\langle\tilde Q,\tilde Q\rangle_{*}$, and $\mathbb{B}$ with it is a complex Hilbert space of dimension four, the space of four complex coordinates with the standard form.

**The units are orthonormal.** For two units $\langle e_\mu,e_\nu\rangle_{*}=\delta_{\mu\nu}$, because $e_\mu e_\nu^{*}$ has scalar part one at $\mu=\nu$ and no scalar part otherwise. The coefficient basis is therefore orthonormal, and the four units are a good basis for every expansion below. The orthonormality is a property of the coefficient basis alone: another frame need not be orthonormal, and every display of this article that uses a basis declares the coefficient basis.

**The projection.** In an orthonormal basis an element is the sum of its projections,

$$
\tilde Q=\sum_{\mu}\langle\tilde Q,e_\mu\rangle_{*}\,e_\mu ,
\qquad
\lVert\tilde Q\rVert^{2}=\sum_{\mu}\bigl\lvert\langle\tilde Q,e_\mu\rangle_{*}\bigr\rvert^{2},
$$

and the only use made of the basis is the statement that the four projections sum to the identity.

**The Riesz identification.** Every linear functional on the algebra is $\tilde X\mapsto\langle\tilde X,\tilde Q\rangle_{*}$ for one and only one element $\tilde Q$. The identification is used twice: once to define the adjoint of an endomorphism, once to name the second element of an elementary endomorphism.

### The Two Norms of an Element

**The quaternionic norm.** Besides the plain algebraic norm $Q_t^{2}-B^{2}$, the algebra carries the **quaternionic algebraic norm**

$$
N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}=Q_t^{2}+B^{2},
$$

the algebraic norm of the quaternionic form. It is multiplicative, $N(\tilde Q_1\tilde Q_2)=N(\tilde Q_1)N(\tilde Q_2)$, and it vanishes exactly at $0$ and on the zero divisors, so it decides invertibility: $\tilde Q$ is a unit exactly when $N(\tilde Q)\neq0$, with $\tilde Q^{-1}=\tilde Q^{\natural}/N(\tilde Q)$.

**It cannot carry weights.** The quaternionic norm takes complex values, and its realified form has signature $(4,4)$: it is indefinite, and the zero-divisor cone is its isotropic cone. So it is not a norm in the sense of a Hilbert space, and no weight can be read from it. The Hermitian norm is definite and is the one the decomposition uses. The algebra therefore has two norms of different character — one definite and not multiplicative, one multiplicative and not definite — and no single form is both; the whole structure of this article comes from that split.

**The two normalisations differ.** A singular vector of the decomposition is an element of Hermitian norm one, $\lVert\tilde U\rVert=1$, and that is **not** the unit condition $N(\tilde U)=1$ of *Norm and Unitary Conventions*. The gap is not small: the four units are orthonormal, and $N(\vec e_x)=-1$. An element of Hermitian norm one is a unit exactly when $N(\tilde U)\neq0$, and its two weights obey $\lvert N(\tilde U)\rvert\leq1$ with equality exactly when they agree, as §*The Weights of One Multiplier* shows. Orthonormality therefore says nothing about the multiplicative character of an element: the four units are orthonormal and their quaternionic norms are $1,-1,-1,-1$. This is the first place where the decomposition and the algebra part company, and it is not a defect of the decomposition: the weights are the numbers that carry the multiplicative information the normalisation drops.

## The Endomorphisms

### The Ambient Space

**The space.** An **endomorphism** is a complex-linear map $F:\mathbb{B}\to\mathbb{B}$. The endomorphisms form the complex algebra $\operatorname{End}(\mathbb{B})$ under composition, of complex dimension sixteen, with identity $\mathrm{I}_4$. Every endomorphism is determined by its four values on the four units, and its matrix in the coefficient basis is the array of those values, $[F]_{\mathcal{E}}$ with $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$.

**The scalar product of operators.** The corresponding form on $\operatorname{End}(\mathbb{B})$ is

$$
\langle\!\langle F,G\rangle\!\rangle=\sum_{\mu}\langle F(e_\mu),G(e_\mu)\rangle_{*} ,
$$

Hermitian and definite, and it makes $\operatorname{End}(\mathbb{B})$ a Hilbert space of complex dimension sixteen. The **Hilbert–Schmidt norm** is $\lVert F\rVert^{2}=\langle\!\langle F,F\rangle\!\rangle$, the sum of the squares of the images of the four units, the same for every orthonormal basis. The two norms of an operator are

$$
\lVert F\rVert_{\mathrm{op}}=\sup_{\lVert\tilde X\rVert=1}\lVert F(\tilde X)\rVert ,
\qquad
\lVert F\rVert^{2}=\sum_{\mu}\lVert F(e_\mu)\rVert^{2},
$$

and $\lVert\mathrm{I}_4\rVert^{2}=4$.

**The determinant.** The endomorphism $F$ acts on the top exterior power $\Lambda^{4}\mathbb{B}$, a complex line, by multiplication by a scalar, and that scalar is $\det F$. It is multiplicative, $\det(FG)=\det F\det G$, and it is nonzero exactly when $F$ is invertible.

### The Adjoint

**The definition.** For each $\tilde Y$ the assignment $\tilde X\mapsto\langle F(\tilde X),\tilde Y\rangle_{*}$ is a linear functional of $\tilde X$, so by the Riesz identification there is one element $F^{*}(\tilde Y)$ with

$$
\langle F(\tilde X),\tilde Y\rangle_{*}=\langle \tilde X,F^{*}(\tilde Y)\rangle_{*}
\qquad\text{for every }\tilde X .
$$

The assignment $\tilde Y\mapsto F^{*}(\tilde Y)$ is linear and defines the **adjoint** $F^{*}$ of $F$: the Hermitian adjoint of *Operator Family Conventions*, the sign ${}^{*}$ written on the operator and never on an element.

**The rules.** From the characterisation,

$$
(F+G)^{*}=F^{*}+G^{*},\qquad
(\lambda F)^{*}=\bar\lambda F^{*},\qquad
(FG)^{*}=G^{*}F^{*},\qquad
(F^{*})^{*}=F ,
$$

the reversal in the third being the reversal of the composition and not of the product of the algebra. The adjoint of $\mathrm{I}_4$ is $\mathrm{I}_4$. So far nothing distinguishes $\mathbb{B}$ from $\mathbb{C}^{4}$; the next subsection is where the multiplication begins to be visible.

### The Two-Sided Operators and Their Adjoints

**The family.** For two elements the **two-sided operator** is

$$
L_{\tilde Q_1}R_{\tilde Q_2}:\mathbb{B}\longrightarrow\mathbb{B},
\qquad
L_{\tilde Q_1}R_{\tilde Q_2}(\tilde X)=\tilde Q_1\tilde X\tilde Q_2 ,
$$

with the left multiplier first, as in *Operator Family Conventions*. At $\tilde Q_2=e_t$ it is the left multiplier $L_{\tilde Q_1}$, at $\tilde Q_1=e_t$ the right multiplier $R_{\tilde Q_2}$, and at the pair $(e_t,e_t)$ the identity. The composition is

$$
\bigl(L_{\tilde Q_1}R_{\tilde Q_2}\bigr)\bigl(L_{\tilde Q_3}R_{\tilde Q_4}\bigr)
=L_{\tilde Q_1\tilde Q_3}R_{\tilde Q_4\tilde Q_2},
$$

the right slot reversed, because the right multiplier runs backwards.

**The adjoint keeps the order.** The adjoint of a two-sided operator is two-sided, with the same order and both parameters conjugated,

$$
\bigl(L_{\tilde Q_1}R_{\tilde Q_2}\bigr)^{*}=L_{\tilde Q_1^{*}}R_{\tilde Q_2^{*}} .
$$

*Proof.* By the characterisation it is enough to verify the defining relation. The left side is $\operatorname{Sc}(\tilde Q_1\tilde X\tilde Q_2\tilde Y^{*})$, and the right side is $\operatorname{Sc}\bigl(\tilde X(\tilde Q_1^{*}\tilde Y\tilde Q_2^{*})^{*}\bigr)=\operatorname{Sc}(\tilde X\tilde Q_2\tilde Y^{*}\tilde Q_1)$, which is the same number by the cyclicity of the scalar part. The assignment is linear and the element that represents a functional is unique, so the two operators agree.

**The star keeps the order, the plain adjoint reverses it.** The plain adjoint of the same family, taken with respect to the plain form $\operatorname{Sc}(\tilde Q_1\tilde Q_2)$ and written ${}^{\approx}$, is $L_{\tilde Q_1}R_{\tilde Q_2}^{\approx}=L_{\tilde Q_2}R_{\tilde Q_1}$, the two slots exchanged, as *Operators Acting on Two Sides* states. The contrast is the reason the star is the conjugation of this article: the star reverses the order of the product, so conjugating the operator twice reverses and un-reverses, and the order survives. The plain form conjugates nothing, so its adjoint has to exchange the slots itself. Both computations are of the same length and they disagree, which is why the form in view is always named.

**The positive model case.** For any $F$ the product $F^{*}F$ is self-adjoint, $(F^{*}F)^{*}=F^{*}F$, and positive:

$$
\langle F^{*}F(\tilde X),\tilde X\rangle_{*}=\langle F(\tilde X),F(\tilde X)\rangle_{*}=\lVert F(\tilde X)\rVert^{2}\geq0 ,
$$

with $F^{*}F=0$ exactly when $F=0$. For a one-sided operator this reads $L_{\tilde Q}^{*}L_{\tilde Q}=L_{\tilde Q^{*}\tilde Q}$, so the positive operator attached to an element is the left multiplication by the Hermitian element $\tilde Q^{*}\tilde Q$; this is where the two weights of an element come from.

## The Spectral Theorem

### The Statement

**Theorem.** Let $H$ be a self-adjoint endomorphism of $\mathbb{B}$, $H^{*}=H$, and suppose $H$ positive semidefinite,

$$
\langle H(\tilde X),\tilde X\rangle_{*}\geq0
\qquad\text{for every }\tilde X .
$$

Then the algebra has an orthonormal basis $\tilde V_1,\dots,\tilde V_4$ of eigenvectors of $H$,

$$
H(\tilde V_k)=\lambda_k\tilde V_k,\qquad \lambda_k\geq0 ,
$$

and the eigenvalues can be ordered $\lambda_1\geq\lambda_2\geq\lambda_3\geq\lambda_4\geq0$.

The theorem is the engine of the article: the decomposition is this theorem applied to $H=F^{*}F$. It is proved here, in four steps, and the proof uses only the compactness of the unit sphere of a finite-dimensional complex space with a definite form and the defining relation of the adjoint.

### The Proof of the Spectral Theorem

**First step: the maximum exists.** The unit sphere $S=\{\tilde X:\lVert\tilde X\rVert=1\}$ is closed and bounded in $\mathbb{C}^{4}$, hence compact, and $\tilde X\mapsto\langle H(\tilde X),\tilde X\rangle_{*}$ is continuous and real-valued on it, because $H$ is self-adjoint. So the function attains a maximum $\lambda$, and the positivity of $H$ makes $\lambda$ non-negative. Fix a point $\tilde V$ of the sphere at which the maximum is attained.

**Second step: a maximising point is an eigenvector.** Let $\tilde Y$ be an element and $t$ real and small, and put

$$
\boldsymbol{x}(t)=\frac{\tilde V+t\tilde Y}{\lVert \tilde V+t\tilde Y\rVert},
\qquad
\varphi(t)=\frac{\langle H(\tilde V+t\tilde Y),\tilde V+t\tilde Y\rangle_{*}}{\lVert \tilde V+t\tilde Y\rVert^{2}} .
$$

The point $\boldsymbol{x}(t)$ lies on the sphere, so $\varphi$ has a maximum at $t=0$ and $\varphi'(0)=0$. The numerator is $\lambda+2t\operatorname{Re}\langle H(\tilde V),\tilde Y\rangle_{*}+t^{2}\langle H(\tilde Y),\tilde Y\rangle_{*}$ and the denominator $1+2t\operatorname{Re}\langle\tilde V,\tilde Y\rangle_{*}+t^{2}\lVert\tilde Y\rVert^{2}$, since $\lVert\tilde V\rVert=1$ and $\langle H(\tilde V),\tilde V\rangle_{*}=\lambda$. Differentiating the quotient at $t=0$ and using $\varphi'(0)=0$,

$$
\operatorname{Re}\bigl\langle H(\tilde V)-\lambda\tilde V,\ \tilde Y\bigr\rangle_{*}=0 .
$$

The relation holds for every $\tilde Y$; replacing $\tilde Y$ by $i\tilde Y$ turns the real part of $i$ times a number into minus its imaginary part, so the imaginary part vanishes too, and $H(\tilde V)=\lambda\tilde V$. The maximising point is an eigenvector with the real eigenvalue $\lambda\geq0$.

**Third step: the orthogonal complement is invariant.** If $\tilde X$ is orthogonal to $\tilde V$ then

$$
\langle H(\tilde X),\tilde V\rangle_{*}=\langle \tilde X,H(\tilde V)\rangle_{*}=\lambda\langle \tilde X,\tilde V\rangle_{*}=0 ,
$$

so $H$ carries $\tilde V^{\perp}$ into itself, and that complement has dimension three.

**Fourth step: induction.** The restriction of $H$ to $\tilde V^{\perp}$ is self-adjoint and positive for the restricted form: self-adjoint because $H$ preserves the complement and is self-adjoint on the whole space, positive because the inequality holds on a subspace. The first three steps apply again and give a unit eigenvector $\tilde V_2$ in $\tilde V^{\perp}$ with $\lambda_2\geq0$, then a third in the complement of the first two, then a fourth. Four orthonormal elements of a space of dimension four are a basis, and ordering the eigenvalues decreasingly gives the statement.

### What Follows

**The diagonal form and the square root.** In the eigenbasis the operator is diagonal,

$$
H=\sum_{k}\lambda_k\,\tilde V_k\langle\cdot,\tilde V_k\rangle_{*} ,
\qquad
\lVert H\rVert^{2}=\sum_{k}\lambda_k^{2},
$$

the second because the Hilbert–Schmidt norm of a diagonal operator is the sum of the squares of its diagonal values. A positive semidefinite operator has a positive semidefinite square root, the operator with the same eigenvectors and the eigenvalues $\sqrt{\lambda_k}$; it is unique, it commutes with $H$, and its square is $H$.

**The kernel.** The kernel of a positive semidefinite operator is spanned by the eigenvectors of eigenvalue zero, since $\langle H(\tilde X),\tilde X\rangle_{*}=\sum_{k}\lambda_k\lvert\langle \tilde X,\tilde V_k\rangle_{*}\rvert^{2}$ vanishes only when every component on an eigenvector of positive eigenvalue vanishes.

## The Decomposition

### The Theorem

**Theorem.** Let $F$ be an endomorphism of $\mathbb{B}$. There are orthonormal families $\tilde U_1,\dots,\tilde U_4$ and $\tilde V_1,\dots,\tilde V_4$ of the algebra and real numbers $\rho_1\geq\rho_2\geq\rho_3\geq\rho_4\geq0$ such that

$$
F(\tilde V_k)=\rho_k\tilde U_k\qquad\text{for }k=1,2,3,4 ,
$$

equivalently

$$
F=\sum_{k=1}^{4}\rho_k\,\mathcal P_{\tilde U_k,\tilde V_k},
\qquad\text{that is}\qquad
F(\tilde X)=\sum_{k=1}^{4}\rho_k\,\tilde U_k\langle\tilde X,\tilde V_k\rangle_{*}
\quad\text{for every }\tilde X .
$$

The numbers $\rho_k(F)$ are the **weights** of $F$, the $\tilde U_k$ its **left** and the $\tilde V_k$ its **right singular vectors**.

### The Proof of the Decomposition

**The operator $F^{*}F$.** It is self-adjoint and positive semidefinite, so by the spectral theorem it has an orthonormal eigenbasis $\tilde V_1,\dots,\tilde V_4$ with real eigenvalues $\lambda_k\geq0$; relabel so that $\lambda_1\geq\cdots\geq\lambda_4$, and put $\rho_k=\sqrt{\lambda_k}$.

**The images are orthogonal and of the right length.** For each $k$,

$$
\lVert F(\tilde V_k)\rVert^{2}=\langle F(\tilde V_k),F(\tilde V_k)\rangle_{*}
=\langle F^{*}F(\tilde V_k),\tilde V_k\rangle_{*}
=\lambda_k\langle \tilde V_k,\tilde V_k\rangle_{*}=\rho_k^{2},
$$

and $\langle F(\tilde V_i),F(\tilde V_j)\rangle_{*}=\lambda_i\langle \tilde V_i,\tilde V_j\rangle_{*}=0$ for $i\neq j$. For the indices with $\rho_k>0$ put $\tilde U_k=F(\tilde V_k)/\rho_k$; these are orthonormal, since $\langle \tilde U_i,\tilde U_j\rangle_{*}=\delta_{ij}$ by the two displays. They are at most four, and the indices they occupy are the first ones, because the weights are ordered; completing them to an orthonormal family $\tilde U_1,\dots,\tilde U_4$ in that order gives the two families of the statement. Then $F(\tilde V_k)=\rho_k\tilde U_k$ for every $k$: by construction where $\rho_k>0$, and where $\rho_k=0$ because then $F(\tilde V_k)=0$ and $\rho_k\tilde U_k=0$.

**The extension to the whole algebra.** Since the $\tilde V_k$ are an orthonormal basis, $\tilde X=\sum_k\langle \tilde X,\tilde V_k\rangle_{*}\tilde V_k$, and by linearity

$$
F(\tilde X)=\sum_k\langle \tilde X,\tilde V_k\rangle_{*}\,F(\tilde V_k)
=\sum_k\rho_k\langle \tilde X,\tilde V_k\rangle_{*}\,\tilde U_k ,
$$

which is the statement, with $\mathcal P_{\tilde U,\tilde V}(\tilde X)=\tilde U\langle \tilde X,\tilde V\rangle_{*}$ for the elementary endomorphism.

**The compact form.** The terms of weight zero contribute nothing, so writing $r$ for the number of positive weights,

$$
F=\sum_{k=1}^{r}\rho_k\,\mathcal P_{\tilde U_k,\tilde V_k},
\qquad
\rho_1\geq\cdots\geq\rho_r>0 ,
$$

and the convention $\rho_k=0$ beyond $r$ keeps the four-index form without loss.

### The Operator Form

**The statement.** Read the coefficient basis $\mathcal{E}=(e_t,\vec e_x,\vec e_y,\vec e_z)$ in the order written, and let $e_k$ be its $k$-th member. There are two unitary operators $\mathcal U,\mathcal V$ and a self-adjoint, positive semidefinite operator $\Sigma$ with

$$
F=\mathcal U\,\Sigma\,\mathcal V^{*},
\qquad
\Sigma(e_k)=\rho_k\,e_k,\qquad
\mathcal V(e_k)=\tilde V_k,\qquad
\mathcal U(e_k)=\tilde U_k .
$$

The operator $\Sigma$ is the **scale**, and $\mathcal U$ and $\mathcal V$ are the two **unitaries of the decomposition**, one on each side of it.

**It is the same theorem.** Expanding the product along the basis,

$$
\mathcal U\Sigma\mathcal V^{*}(\tilde X)
=\sum_{k}\rho_k\,\mathcal U(e_k)\bigl\langle \tilde X,\mathcal V(e_k)\bigr\rangle_{*}
=\sum_{k}\rho_k\,\tilde U_k\langle \tilde X,\tilde V_k\rangle_{*} ,
$$

which is the sum form of §*The Decomposition*. The passage is reversible, because both families are orthonormal bases and the assignment $e_k\mapsto\tilde V_k$ determines $\mathcal V$. The theorem therefore has two faces: the sum of four atoms with weights, and the product of a symmetry of the source, a scale along four axes, and a symmetry of the target.

**The scale and the modulus.** Multiplying the factorization by its adjoint gives $F^{*}F=\mathcal V\Sigma^{2}\mathcal V^{*}$, the crossed terms canceling because $\mathcal U$ is unitary. So $\Sigma$ is the modulus $\lvert F\rvert=(F^{*}F)^{1/2}$ carried into the basis $\mathcal E$ by $\mathcal V$, and its four diagonal entries are the weights. The modulus is intrinsic and the scale is the same operator written in a chosen basis; the two coincide when $\mathcal V$ is the identity.

**The spectral decomposition of the scale.** Let the distinct positive weights be $\sigma_1>\cdots>\sigma_m$, and let $\Pi_i$ be the orthogonal projector onto the eigenspace of $\Sigma$ for $\sigma_i$, an operator and not an element. The projectors are mutually orthogonal and

$$
\Sigma=\sum_{i=1}^{m}\sigma_i\,\Pi_i ,
\qquad
\Pi_i\Pi_j=\delta_{ij}\Pi_i ,
\qquad
\sum_{i=1}^{m}\Pi_i=\mathrm I_4-\Pi_{\ker F} ,
$$

the last projector being the one onto the kernel of $F$, because the weights that vanish are exactly the directions that $F$ kills. The decomposition then reads

$$
F=\sum_{i=1}^{m}\sigma_i\,\mathcal U\Pi_i\mathcal V^{*} ,
$$

and each term of this sum is the group of the terms of the sum form whose weights are equal. This grouping is the reason the weights of a repeated value move together, which is the freedom of §*The Non-Uniqueness*.

**What is intrinsic.** The spectrum of $\Sigma$ is the spectrum of $\lvert F\rvert$, so the multiset of the weights, the multiplicity of each, and the filtration of $\mathbb{B}$ by the subspaces spanned by the right vectors of the largest weights depend on $F$ alone. The scale itself is determined by $F$ and by $\mathcal V$, so it is unique once the right family is chosen and unique up to the ordering of the equal weights when it is not. The two unitaries are not intrinsic: they carry the chosen basis to the two families, and a different choice of families is a different pair.

**The residual freedom.** Suppose $F=\mathcal U\Sigma\mathcal V^{*}=\mathcal U'\Sigma\mathcal V'^{*}$, and write $\mathcal U'=\mathcal U W$ and $\mathcal V'=\mathcal V Z$ with $W$ and $Z$ unitary. The equality is $W\Sigma Z^{*}=\Sigma$, that is

$$
W\Sigma=\Sigma Z .
$$

With $W=Z$ the condition is that a unitary operator commute with $\Sigma$, so it acts inside each eigenspace and nowhere else: this is the phase per term of §*The Non-Uniqueness* when the eigenspace is a line, and the unitary mixing of the equal weights when it is larger. When $\Sigma$ is singular the kernel adds a second freedom: on the range of $\Sigma$ the two operators agree and act inside the eigenspaces, while on the kernel they are independent of one another, and that independence is the arbitrary completion of the left family on the vanishing terms.

**The invertibility.** $F$ is invertible exactly when $\Sigma$ is, that is when all four weights are positive, and this is the row of rank four in §*The Rank Cases*.

**The order inside the bracket.** A common statement of the Hermitian form is $\operatorname{Sc}(X^{*}Y)$, linear in the second argument, where this article writes $\langle X,Y\rangle_{*}=\operatorname{Sc}(XY^{*})$, linear in the first (§*The Hermitian Form*). The two are conjugate and transposed, $\operatorname{Sc}(X^{*}Y)=\overline{\langle Y,X\rangle_{*}}$, and an operator is self-adjoint or unitary for the one exactly when it is for the other, so the factorization above is unaffected and only the order inside a bracket changes.

### The Three Factors in the Algebra

**The product, written in the algebra.** The operator form names its three factors by what they do to a basis, and the basis to use is the one the algebra already carries: the four units, which are orthonormal, $\langle e_\mu,e_\nu\rangle_{*}=\delta_{\mu\nu}$. Written in that basis each factor is a sum of four atoms, and the identity reads

$$
\boxed{\;
F=\Bigl(\sum_{k\le4}\mathcal P_{\tilde U_k,e_k}\Bigr)
\Bigl(\sum_{k\le4}\rho_k\,\mathcal P_{e_k,e_k}\Bigr)
\Bigl(\sum_{k\le4}\mathcal P_{e_k,\tilde V_k}\Bigr)
\;}
$$

with no array anywhere. The first factor sends the unit $e_k$ to the $k$-th left vector, the third sends it to the $k$-th right vector, and the middle multiplies that unit by the weight. The two outer factors are unitary operators; the middle is self-adjoint and positive, and its trace is the sum of the weights, because each $\mathcal P_{e_k,e_k}$ is a projector of rank one. The middle factor is the **scale in the basis of the units**, and $\sum_k\mathcal P_{e_k,e_k}=\mathrm I_4$, so the four projectors split the identity.

**The units are the natural middle.** Any orthonormal family serves as the middle family, with the two outer factors changed accordingly, so the choice is not forced by the theorem. The units are the one family that needs no preparation, and the one that the multiplication permutes, up to a sign and a factor $i$. The display therefore reads the form and the multiplication in the same basis, which is what a factorisation written in the algebra should do.

**Why the middle is a sum and not an element.** The four weights of a two-sided operator are the four products $\rho_i(\tilde Q_1)\rho_j(\tilde Q_2)$ of the weights of its two multipliers (§*The Weights of Two Multipliers*), and every such rectangle satisfies

$$
\rho_1\rho_4=\rho_2\rho_3 ,
$$

because both sides are $\rho_1(\tilde Q_1)\rho_1(\tilde Q_2)\rho_2(\tilde Q_1)\rho_2(\tilde Q_2)$. A left multiplier is the case $\tilde Q_2=e_t$ and a two-sided operator the case $\tilde Q_2=\tilde Q_1^{*}$, so the identity holds all through the four families, the two-sided operator adding $\rho_2=\rho_3$ on top of it. A generic endomorphism satisfies no such equation: at the weights $4,3,2,1$ the two products are $4$ and $6$. The scale of a generic endomorphism is therefore not a two-sided operator, hence not a product of elements in any of the four families, and it must be written as a sum of four atoms. This is the precise sense in which the general statement belongs to the form: the product carries a scale of its own shape and of no other, and the general scale is outside that shape.

**The two-sided family pays nothing.** For that family the three factors are elements, and the collapse is the polar decomposition of an element. Every element is

$$
\tilde Q=\tilde U\tilde H,
\qquad
\tilde U\tilde U^{*}=e_t,
\qquad
\tilde H^{*}=\tilde H,
\qquad
\tilde H^{2}=\tilde Q^{*}\tilde Q,
$$

with $\tilde H$ of nonnegative spectrum, the positive square root of $\tilde Q^{*}\tilde Q$. The same element is also $\tilde Q=\tilde H_2\tilde U_2$, with $\tilde H_2$ the positive square root of $\tilde Q\tilde Q^{*}$ and the unitary on the other side. The two-sided operator wants the two unitaries at its two ends:

$$
\boxed{\;
L_{\tilde Q_1}R_{\tilde Q_2}=L_{\tilde U_1}R_{\tilde U_2}\;L_{\tilde H_1}R_{\tilde H_2},
\qquad
\bigl\lvert L_{\tilde Q_1}R_{\tilde Q_2}\bigr\rvert=L_{\tilde H_1}R_{\tilde H_2}
\;}
$$

**The dictum.** Each multiplier is decomposed with its unitary away from the middle: the left one as $\tilde U_1\tilde H_1$, the right one as $\tilde H_2\tilde U_2$. The two unitaries then multiply to a unitary operator and the two Hermitian factors to a positive one, so a two-sided operator is the product of a unitary two-sided operator and a positive one, and the second factor is its modulus. The modulus is a two-sided operator again, of the two moduli of the two multipliers: its weights are the four products of §*The Weights of Two Multipliers*, which is what the collapse to elements must give, the weight pattern of the family being a rectangle from the start. The middle factor of this display is the modulus itself, where the middle factor of the first display is the modulus read in the basis of the units, $\Sigma=\mathcal V^{*}\lvert F\rvert\mathcal V$; the two differ by the unitary that carries one basis to the other.

**The one-multiplier case.** At $\tilde Q_2=e_t$ the second pair is the identity and the same display reads

$$
L_{\tilde Q}=L_{\tilde U}L_{\tilde H},
\qquad
\tilde Q=\tilde U\tilde H,
$$

two factors, one unitary and one Hermitian positive, and the weights $\rho_1,\rho_1,\rho_2,\rho_2$ are the two eigenvalues of $\tilde H$. There is no third factor because a left multiplier acts on one side only, and a source that is not turned needs no unitary of the source.

**Existence and the degenerate case.** $\tilde H$ exists and is unique, $\tilde Q^{*}\tilde Q$ being Hermitian of nonnegative spectrum and such an element having a unique square root of the same kind. When $\tilde Q$ is a zero divisor, $\tilde H$ is singular and $\tilde U$ is fixed only on the range of $\tilde H$; on the kernel it is free, any unitary completion of the partial isometry doing, because $\tilde H$ kills the kernel and $\tilde U\tilde H$ does not see the choice. The weights are untouched, a zero divisor contributing a zero to the pair.

### The Elementary Endomorphisms

**The definition.** An **elementary endomorphism** is a map $\mathcal P_{\tilde U_1,\tilde U_2}(\tilde X)=\tilde U_1\langle \tilde X,\tilde U_2\rangle_{*}$ with two nonzero elements. Its image is the line $\mathbb{C}\tilde U_1$, so it has rank one; and conversely every endomorphism of rank one is elementary, with $\tilde U_1$ the element of Hermitian norm one along the image and $\tilde U_2$ the element that the Riesz identification assigns to the functional $\tilde X\mapsto$ the coordinate of $F(\tilde X)$ along $\tilde U_1$. The elementary endomorphisms are therefore exactly the endomorphisms of rank one, and the theorem writes $F$ as a sum of $r$ of them with the weights as coefficients.

**The normalisation.** The Hilbert–Schmidt norm of an elementary endomorphism is

$$
\bigl\lVert\mathcal P_{\tilde U_1,\tilde U_2}\bigr\rVert^{2}
=\sum_{\mu}\bigl\lVert \tilde U_1\langle e_\mu,\tilde U_2\rangle_{*}\bigr\rVert^{2}
=\lVert \tilde U_1\rVert^{2}\lVert \tilde U_2\rVert^{2},
$$

because $\sum_\mu\lvert\langle e_\mu,\tilde U_2\rangle_{*}\rvert^{2}=\lVert \tilde U_2\rVert^{2}$. With orthonormal parameters the norm is one, so the weights carry the whole size of the operator; this is why the terms are ordered by weight and not by any other quantity.

## The Weights

### The Rank Cases

**The number of nonzero weights is the rank.** The image of $F$ is spanned by the left vectors of the positive weights, and conversely a space of image of dimension $r$ gives exactly $r$ positive weights. Hence the number of positive weights is $\operatorname{rank}F$, and the five cases are:

| $\operatorname{rank}F$ | the weights | the decomposition |
|---|---|---|
| $4$ | $\rho_1\geq\rho_2\geq\rho_3\geq\rho_4>0$ | four terms, $F$ invertible |
| $3$ | $\rho_4=0$ | three terms, image of dimension three |
| $2$ | $\rho_3=\rho_4=0$ | two terms, image of dimension two |
| $1$ | $\rho_2=\rho_3=\rho_4=0$ | one term, $F=\rho_1\mathcal P_{\tilde U_1,\tilde V_1}$ |
| $0$ | all zero | $F=0$ |

The rank is not an extra invariant: it is the number of terms, and the number of terms is the number of nonzero weights. The generic endomorphism has four distinct positive weights, because a coincidence of two weights is the vanishing of a discriminant and therefore a closed condition with no interior.

### The Three Identities

**The product is the determinant.** Multiplying the four weights,

$$
\rho_1\rho_2\rho_3\rho_4=\lvert\det F\rvert ,
$$

because $\det(F^{*}F)=\lvert\det F\rvert^{2}$ and the determinant of $F^{*}F$ is the product of its eigenvalues $\lambda_k=\rho_k^{2}$.

**The sum of squares is the norm.** Summing the squares,

$$
\rho_1^{2}+\rho_2^{2}+\rho_3^{2}+\rho_4^{2}=\lVert F\rVert^{2}=\sum_{\mu}\lVert F(e_\mu)\rVert^{2},
$$

the Pythagorean theorem for the decomposition: the terms are orthogonal in the operator form, so the weight vector carries the whole size of the operator and a truncation that discards small weights loses exactly their squares.

**The largest weight is the operator norm.** The first weight is $\lVert F\rVert_{\mathrm{op}}$, because $\lVert F(\tilde X)\rVert^{2}=\sum_k\rho_k^{2}\lvert\langle \tilde X,\tilde V_k\rangle_{*}\rvert^{2}\leq\rho_1^{2}\lVert \tilde X\rVert^{2}$ with equality at $\tilde V_1$. The last weight, when the rank is four, is the reciprocal of the operator norm of the inverse. The four weights thus bound the action from above, the action of the inverse from below, and the volume change exactly.

### The Geometric Reading

**The ellipsoid.** The image of the unit sphere of $\mathbb{B}$ is the ellipsoid whose semi-axes are the segments of length $\rho_k$ along the directions $\tilde U_k$. The weights are the lengths, the left vectors the directions of the image, and the right vectors the directions of the sphere carried onto them.

**The two unitaries and the scale.** The map is a unitary operator, then a scaling of the four coordinates, then a second unitary operator, in that order: this is the factorization $\mathcal U\Sigma\mathcal V^{*}$ of §*The Operator Form* read as a motion of the sphere, the source turned by $\mathcal V$, the axes stretched by the weights, and the result turned into place by $\mathcal U$. The unitary operators are those of the Hermitian form, and they include the two regular copies of the unitary group of the algebra: $L_{\tilde U}$ and $R_{\tilde U}$ are unitary exactly when $\tilde U\tilde U^{*}=e_t$, that is when $\tilde U$ is unitary in the sense of *Norm and Unitary Conventions*. The unitary factors are the operators that preserve the form, the two-sided ones among them are the $L_{\tilde U_1}R_{\tilde U_2}$ with $\tilde U_1$ and $\tilde U_2$ unitary, and the weights are the only part of the decomposition that is not a symmetry of the form.

### The Non-Uniqueness

**Where the freedom is.** The weights are determined by $F$, being the square roots of the eigenvalues of $F^{*}F$. The two families are not, and the freedom has three regimes.

**Distinct positive weights.** The right vectors are eigenvectors of $F^{*}F$ for distinct eigenvalues, hence determined up to a phase each, and the left vectors follow from $\tilde U_k=F(\tilde V_k)/\rho_k$. The freedom is

$$
\tilde U_k\mapsto e^{i\theta_k}\tilde U_k ,
\qquad
\tilde V_k\mapsto e^{i\theta_k}\tilde V_k ,
$$

one arbitrary phase per term, and the phases do not mix the terms.

**Coincident weights.** If some weights coincide, the eigenvectors of a common eigenvalue span a subspace of that dimension, any orthonormal basis of it is admissible, and the left vectors move with it by the same unitary mixing. The mixing respects the groups: weights of different value are never mixed.

**Vanishing weights.** If some weights vanish, the corresponding right vectors span the kernel and the corresponding left vectors are unconstrained by $F$: any orthonormal family completing the nonzero left vectors is admissible, and it is chosen by a convention. This is the freedom that the compact form removes, since it drops the vanishing terms.

**The freedom in one line.** In the language of §*The Operator Form* the three regimes are one condition: the pair of unitary operators $W,Z$ with $W\Sigma=\Sigma Z$, acting inside the eigenspaces of the scale and nowhere else, the two sides being independent on the kernel of $\Sigma$.

**The invariant summary.** What the decomposition determines intrinsically is the multiset of the four weights, the filtration of the algebra by the subspaces spanned by the right vectors of the largest weights, and the corresponding subspaces on the left. Everything else is a choice of basis inside a subspace.

### The Truncation

**The nearest operator of smaller rank.** Let $s$ be an integer between $0$ and $4$ and $F_s=\sum_{k\leq s}\rho_k\mathcal P_{\tilde U_k,\tilde V_k}$ the sum of the $s$ heaviest terms, of rank at most $s$. Then

$$
\lVert F-F_s\rVert^{2}=\rho_{s+1}^{2}+\cdots+\rho_4^{2},
$$

because the difference is the sum of the discarded terms and those are orthogonal to the kept ones. Moreover no endomorphism of rank at most $s$ is closer:

$$
\lVert F-G\rVert\ \geq\ \Bigl(\rho_{s+1}^{2}+\cdots+\rho_4^{2}\Bigr)^{1/2}
\qquad\text{whenever }\operatorname{rank}G\leq s .
$$

This is the Eckart–Young theorem: the best approximation by a map of smaller rank keeps the largest weights and discards the rest, and the error is the discarded weight.

**The min-max characterisation.** The proof rests on one lemma, which is a consequence of the decomposition. For $k=1,\dots,4$,

$$
\rho_k=\min_{\dim W=5-k}\ \max_{0\neq\tilde X\in W}\frac{\lVert F(\tilde X)\rVert}{\lVert \tilde X\rVert} .
$$

*Proof.* Take $W=\operatorname{span}\{\tilde V_k,\dots,\tilde V_4\}$, of dimension $5-k$. On it the ratio is at most $\rho_k$, because $\lVert F(\tilde X)\rVert^{2}=\sum_{i\geq k}\rho_i^{2}\lvert\langle \tilde X,\tilde V_i\rangle_{*}\rvert^{2}\leq\rho_k^{2}\lVert \tilde X\rVert^{2}$. Conversely let $W$ be any subspace of dimension $5-k$. It meets $\operatorname{span}\{\tilde V_1,\dots,\tilde V_k\}$ in a nonzero element, since the two dimensions sum to five and the algebra has dimension four, and there the ratio is at least $\rho_k$, because on that span $\lVert F(\tilde X)\rVert^{2}=\sum_{i\leq k}\rho_i^{2}\lvert\langle \tilde X,\tilde V_i\rangle_{*}\rvert^{2}\geq\rho_k^{2}\lVert \tilde X\rVert^{2}$. The minimum over $W$ is therefore $\rho_k$.

**The interlacing.** The lemma gives $\rho_k(F)\leq\rho_{k-s}(F-G)$ for $k>s$ whenever $G$ has rank at most $s$, and the argument is three lines. Let $W$ be a subspace of dimension $5-k+s$ on which $F-G$ is bounded by $\rho_{k-s}(F-G)$, which exists by the lemma applied to $F-G$. The kernel of $G$ has dimension at least $4-s$, so $W\cap\ker G$ has dimension at least $(5-k+s)+(4-s)-4=5-k$. On that intersection $G$ vanishes, so

$$
\lVert F(\tilde X)\rVert=\lVert(F-G)(\tilde X)\rVert\ \leq\ \rho_{k-s}(F-G)\,\lVert \tilde X\rVert ,
$$

and the min-max formula for $\rho_k(F)$, a minimum over subspaces of dimension $5-k$ of which $W\cap\ker G$ is one, gives the inequality. Summing the squares over $k>s$ and using the second identity gives the theorem.

## The Multiplication's Share

### The Rank-One Endomorphisms and the Products

**The inclusion.** Let $\tilde Q_1$ and $\tilde Q_2$ be nonzero zero divisors, and read the operator in the $2\times2$ model: it becomes $A\mapsto A_1AA_2$ with $A_1=\mathsf M_2(\tilde Q_1)$ and $A_2=\mathsf M_2(\tilde Q_2)$, both of matrix rank one, since a nonzero zero divisor has $N=0$ and $N$ is the determinant of its matrix. Its array, in the model and read row by row, is $A_1\otimes A_2^{\mathsf T}$, of rank $\operatorname{rank}A_1\operatorname{rank}A_2=1$, because $\mathrm{vec}(A_1AA_2)=(A_1\otimes A_2^{\mathsf T})\,\mathrm{vec}(A)$ for that reading. So $L_{\tilde Q_1}R_{\tilde Q_2}$ has rank one. Its image is the line $\mathbb{C}\tilde Q_1\tilde Q_2$ when $\tilde Q_1\tilde Q_2\neq0$, because at the level of the model
$$
A_1AA_2=u\,(v^{\mathsf H}Aw)\,z^{\mathsf H},
\qquad
A_1=uv^{\mathsf H},\quad A_2=wz^{\mathsf H},
$$
and $v^{\mathsf H}Aw$ is a linear functional of $A$.

**The converse fails, and one example settles it.** The projection onto the line $\mathbb{C}e_t$,
$$
\mathcal P_{e_t,e_t}(\tilde X)=\langle\tilde X,e_t\rangle_{*}e_t ,
$$
is a rank-one endomorphism, and it is no product. Its array in the same reading is $\tfrac12\mathrm{vec}(I_2)\mathrm{vec}(I_2)^{\mathsf T}$, that is, up to the factor, the array with $1$ in the four corners and $0$ elsewhere, and that array is not a Kronecker product. In $A_1\otimes A_2^{\mathsf T}$ every one of the four blocks is a multiple of the single array $A_2^{\mathsf T}$, whereas the four blocks of this array are the four distinct matrix units $E_{11},E_{12},E_{21},E_{22}$, and no array has all four as multiples. So the single term of the decomposition of this endomorphism is not a two-sided operator.

**The criterion.** An elementary endomorphism is a two-sided operator exactly when both of its vectors are zero divisors. *Proof.* In the model the elementary endomorphism has the array
$$
\tfrac12\,\mathrm{vec}(A_{\tilde U_1})\,\overline{\mathrm{vec}(A_{\tilde U_2})}^{\mathsf T},
$$
a rank-one array, and the two-sided family has the matrices $A_1\otimes A_2^{\mathsf T}$. A rank-one array is a Kronecker product of two $2\times2$ arrays exactly when each of its two vectors is a single tensor, because $\mathrm{vec}(A_1)$ is a single tensor exactly when $A_1$ has rank one, and the Kronecker factorisation is unique up to the rescaling $(A_1,A_2)\mapsto(\lambda A_1,\lambda^{-1}A_2)$. The condition is therefore that $A_{\tilde U_1}$ and $A_{\tilde U_2}$ both have rank one, that is $N(\tilde U_1)=N(\tilde U_2)=0$.

**The count.** A rank-one endomorphism is a line in $\mathbb{B}$ together with a nonzero functional, which is six complex parameters; a product of two zero divisors is a pair of projective points of the zero-divisor cone, two parameters each, which is four. The products are therefore a proper subvariety of the rank-one endomorphisms, of codimension two, and the generic atom of a decomposition is not a product: the singular vectors of a generic endomorphism are units, and the criterion then excludes it. What the product gives is not the atom but the weights, the rank pattern and the two-sided operator, which are the subject of the rest of this section.

**Two normalisations of one atom, when the atom is a product.** Such an atom is written both as $\mathcal P_{\tilde U_1,\tilde U_2}$ and as $L_{\tilde Q_1}R_{\tilde Q_2}$, and the two writings normalise differently: the first by the Hermitian norm, the second by the product, in which the multipliers are recovered from the operator up to the rescaling $(\tilde Q_1,\tilde Q_2)\mapsto(\lambda\tilde Q_1,\lambda^{-1}\tilde Q_2)$ and each of them has one weight zero. The first presentation depends on the form, the second on the multiplication, and the weights are the letters that translate between them: by the product rule of the next subsection the four weights of the atom are $\rho_1(\tilde Q_1)\rho_1(\tilde Q_2)$ and three zeros, so an atom that is a product carries exactly one positive weight.

### The Weights of One Multiplier

**The two weights of an element.** For the left multiplier $L_{\tilde Q}$ the positive operator is $L_{\tilde Q}^{*}L_{\tilde Q}=L_{\tilde Q^{*}\tilde Q}$, so the weights of the operator are the square roots of the eigenvalues of the left multiplication by the Hermitian element $\tilde Q^{*}\tilde Q$. That multiplication has four eigenvalues and they come in two pairs, because in the $2\times2$ model the matrix $\mathsf M_2(\tilde Q)\mathsf M_2(\tilde Q)^{\mathsf H}$ has two eigenvalues and each is repeated. The two numbers, counted once each, are the **weights of the element**, written $\rho_1(\tilde Q)\geq\rho_2(\tilde Q)\geq0$, and the weights of the operator are

$$
\rho_{2k-1}(L_{\tilde Q})=\rho_{2k}(L_{\tilde Q})=\rho_k(\tilde Q),
\qquad k=1,2 .
$$

A left multiplier therefore never has a weight of odd multiplicity: its four weights are two pairs, and a value that appears appears twice, at two consecutive ranks.

**They are the two algebraic norms.** The pair of weights carries the two norms of §*The Two Norms of an Element*, and nothing else:

$$
\rho_1(\tilde Q)^{2}+\rho_2(\tilde Q)^{2}=2\langle\tilde Q,\tilde Q\rangle_{*} ,
\qquad
\rho_1(\tilde Q)\,\rho_2(\tilde Q)=\bigl\lvert N(\tilde Q)\bigr\rvert .
$$

The first is the Hilbert–Schmidt norm of $L_{\tilde Q}$, which is $4\langle\tilde Q,\tilde Q\rangle_{*}$ and also $2(\rho_1^{2}+\rho_2^{2})$; the second comes from the determinant of $L_{\tilde Q}$: the eigenvalues of the left multiplier are $Q_t+iB$ and $Q_t-iB$, each twice, so its determinant is $N(\tilde Q)^{2}$, and the product of the four weights is $\rho_1^{2}\rho_2^{2}$. The two displays solve for the weights:

$$
\rho_{1,2}(\tilde Q)=\sqrt{\ \langle\tilde Q,\tilde Q\rangle_{*}\pm\sqrt{\langle\tilde Q,\tilde Q\rangle_{*}^{2}-\bigl\lvert N(\tilde Q)\bigr\rvert^{2}}\ } ,
$$

so the pair of weights is the pair of the two norms rewritten, the sum of the squares reading the definite norm and the product the multiplicative one. The radicand is non-negative because the numbers $\rho_1^{2}$ and $\rho_2^{2}$ have the sum and the product displayed.

**The three cases.** An element is a unit, a zero divisor, or zero, and the weights say which:

| the element | the weights of the element | the weights of $L_{\tilde Q}$ | the rank |
|---|---|---|---|
| a unit, $N\neq0$ | $\rho_1\geq\rho_2>0$ | $\rho_1,\rho_1,\rho_2,\rho_2$ | $4$ |
| a zero divisor, $N=0$ | $\rho_1=\sqrt{2\langle\tilde Q,\tilde Q\rangle_{*}}$, $\rho_2=0$ | $\rho_1,\rho_1,0,0$ | $2$ |
| $0$ | $0,0$ | $0,0,0,0$ | $0$ |

The middle row is the reason the two normalisations differ: a zero divisor has a positive Hermitian norm and a vanishing multiplicative norm, so it is a good singular vector and not a unit. The degeneracy of the weights is exactly the vanishing of $N$, and the invertibility of the element and the invertibility of its left multiplier are one condition, which is a coincidence of the form and the product and not a tautology.

**Three worked elements.** At $\tilde Q=e_t+\vec e_x+i\vec e_y$ the two norms are $\langle\tilde Q,\tilde Q\rangle_{*}=3$ and $N(\tilde Q)=1$, the radicand is $9-1=8$, and

$$
\rho_1(\tilde Q)=1+\sqrt2 ,\qquad \rho_2(\tilde Q)=\sqrt2-1 ,
$$

whose squares sum to $6$ and whose product is $1$. At $\tilde Q=\vec e_x+i\vec e_y$ the Hermitian norm is $2$ and $N=0$, so the weights are $2$ and $0$: the element is a zero divisor, its left multiplier has rank two, and $\rho_1=\sqrt{2\cdot2}=2$. At $\tilde Q=e_t+2\vec e_x$ the two norms are both $5$, the radicand vanishes and the two weights are equal, $\rho_1=\rho_2=\sqrt5$: the equality of the weights is the equality of the two norms, the condition under which the element is a scalar multiple of a unitary one.

### The Weights of Two Multipliers

**The four products.** Let $L_{\tilde Q_1}R_{\tilde Q_2}$ be a two-sided operator. Its weights are the four pairwise products of the weights of the two multipliers,

$$
\bigl\{\rho_i(\tilde Q_1)\,\rho_j(\tilde Q_2):\ i,j=1,2\bigr\},
$$

ordered decreasingly. Two consequences follow at once. The **rank multiplies**,

$$
\operatorname{rank}\bigl(L_{\tilde Q_1}R_{\tilde Q_2}\bigr)
=\tfrac14\operatorname{rank}\bigl(L_{\tilde Q_1}\bigr)\operatorname{rank}\bigl(L_{\tilde Q_2}\bigr),
$$

the factor four being the doubling of the weights of one multiplier; and in the language of the elements the cases are these.

| $\tilde Q_1$ | $\tilde Q_2$ | the weights of $L_{\tilde Q_1}R_{\tilde Q_2}$ | the rank |
|---|---|---|---|
| a unit | a unit | four positive | $4$ |
| a unit | a zero divisor | two positive, two zero | $2$ |
| a zero divisor | a unit | two positive, two zero | $2$ |
| a zero divisor | a zero divisor | one positive, three zero | $1$ |
| zero | anything | all zero | $0$ |

**No two-sided operator has rank three.** The ranks of the table are $0$, $1$, $2$ and $4$, and the value $3$ is absent. A two-sided operator therefore never has rank three, whatever its two multipliers: the pattern of the weights is a rectangle of products, and a rectangle of two by two cannot have exactly three nonzero entries. So the decomposition of a two-sided operator has one, two or four terms and never three (the zero operator has none), and an endomorphism of rank three is not a product. This is the sharpest statement of the section, and it is not a statement of dimension: it holds because the algebra is a $2\times2$ and its two-sided operators are products of two maps of a $2\times2$.

**The ordering of the products.** With $\rho_1(\tilde Q_1)\geq\rho_2(\tilde Q_1)$ and $\rho_1(\tilde Q_2)\geq\rho_2(\tilde Q_2)$, the largest product is $\rho_1(\tilde Q_1)\rho_1(\tilde Q_2)$ and the smallest is $\rho_2(\tilde Q_1)\rho_2(\tilde Q_2)$. The first weight of the two-sided operator is the product of the first weights of the two multipliers and the last is the product of the last, so the operator norm of the product is the product of the operator norms, and the same holds for the reciprocal of the norm of the inverse. The weights of a product are read from the weights of the factors without further computation.

### The Two-Sided Operator

**The weights of the two-sided operator.** The two-sided operator $\mathrm{Sd}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ is the two-sided operator of the pair $(\tilde Q,\tilde Q^{*})$, and the two elements have the same weights, since the star conjugates the coefficients and the weights are moduli. Its weights are therefore

$$
\rho_1^{2}\ \geq\ \rho_1\rho_2\ \geq\ \rho_1\rho_2\ \geq\ \rho_2^{2},
$$

with $\rho_k=\rho_k(\tilde Q)$: the extremes are the squares, the two middle weights are equal, and the repeated middle weight is the geometric mean of the extremes. The two-sided operator is the member of the two-sided family whose weight pattern is a geometric progression, and the pattern records that the second multiplier is the star of the first.

**It is not self-adjoint.** Its adjoint is $L_{\tilde Q^{*}}R_{\tilde Q}$, a different operator unless the two multipliers coincide, so the two-sided operator is not self-adjoint in general and its weights are not its eigenvalues. The distinction is visible at $\tilde Q=\vec e_x$, where the two-sided operator is minus the conjugation by $\vec e_x$, $\mathrm{Sd}_{\vec e_x}(X)=-\vec e_xX\vec e_x$, and has eigenvalues $1,1,-1,-1$ with all four weights equal to one: an operator can be an isometry and carry a negative eigenvalue at the same time, and the weights do not see the sign.

### The Weights Are Products in the Model

**The reduction.** The $2\times2$ isomorphism $\mathsf M_2:\mathbb{B}\to M_2(\mathbb{C})$ of *Matrix Representations Conventions* turns the element into a matrix and the two-sided operator into

$$
\mathsf M_2\bigl(L_{\tilde Q_1}R_{\tilde Q_2}(\tilde X)\bigr)
=\mathsf M_2(\tilde Q_1)\,\mathsf M_2(\tilde X)\,\mathsf M_2(\tilde Q_2),
$$

and in the reading of the model row by row that map is the Kronecker product $\mathsf M_2(\tilde Q_1)\otimes\mathsf M_2(\tilde Q_2)^{\mathsf T}$. The weights of a Kronecker product are the pairwise products of the weights of the factors, which is §*The Weights of Two Multipliers*, and its rank is the product of the ranks, which is the table of that subsection. The Hermitian form is carried to half the Frobenius form,

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\tfrac12\operatorname{tr}\bigl(\mathsf M_2(\tilde Q_1)\mathsf M_2(\tilde Q_2)^{\mathsf H}\bigr),
$$

so the weights of the element are the singular values of its matrix, and the two identities of §*The Weights of One Multiplier* are the two symmetric functions of the singular values of a $2\times2$ matrix: the trace of $\mathsf M_2(\tilde Q^{*}\tilde Q)$ and the modulus of its determinant $N(\tilde Q)$.

### The Sixteen Basis Operators

**A multiplicative basis.** The four left and the four right multipliers of the units combine into the sixteen basis operators $L_{e_\mu}R_{e_\nu}$. They are mutually orthogonal for the operator form, of norm two,

$$
\bigl\langle\!\bigl\langle L_{e_\mu}R_{e_\nu},L_{e_\rho}R_{e_\kappa}\bigr\rangle\!\bigr\rangle=4\,\delta_{\mu\rho}\delta_{\nu\kappa},
$$

because in the model the basis operators are the sixteen Kronecker products $\mathsf M_2(e_\mu)\otimes\mathsf M_2(e_\nu)^{\mathsf T}$, the four $\mathsf M_2(e_\mu)$ are mutually orthogonal with $\operatorname{tr}\bigl(\mathsf M_2(e_\mu)\mathsf M_2(e_\rho)^{\mathsf H}\bigr)=2\delta_{\mu\rho}$, and a Kronecker product of two orthogonal families is orthogonal, with the product of the two normalisations. Sixteen mutually orthogonal operators of norm two in a space of dimension sixteen are a basis, and each of them has rank four, since both multipliers are units.

**Two facts that coexist.** The ambient space has an orthogonal basis all of whose members are invertible, while the cone on which the decomposition lives is made of rank-one operators and is nowhere near a subspace. The two facts do not contradict one another, a basis of a space being rarely a set of rank-one elements, and their coexistence is what makes the biquaternion algebra a good place to read a decomposition: it has a multiplicative basis and a rank-one cone at the same time, and the weights of an element are read from the weights of its multipliers.

### What the Decomposition Is Not

**Not a decomposition of an element.** The four terms are operators and the weights are numbers attached to a map: the decomposition is of an endomorphism. The Peirce decomposition is of an element, into the four corners cut by a pair of complementary idempotents, and it carries idempotents and no weights (*The Peirce Basis of a Peirce Decomposition of the Biquaternion Algebra*). The number four appears in both and does not mean the same thing: here it is the complex dimension of the space, which bounds the number of terms; there it is the number of corners, which comes from the algebra being a $2\times2$.

**Not an eigen-decomposition of left multiplication.** The weights of $L_{\tilde Q}$ need not be the moduli of its eigenvalues. At $\tilde Q=\vec e_x+i\vec e_y$ one has $Q_t=0$ and $B^{2}=0$, so the eigenvalues $Q_t\pm iB$ are both zero and $L_{\tilde Q}$ is nilpotent of square zero, since $\tilde Q^{2}=0$; yet its two weights are $2$ and $0$, read from $\langle\tilde Q,\tilde Q\rangle_{*}=2$ and $N(\tilde Q)=0$. Its spectrum is the single point $0$ and its operator norm is two: the weights report the norm and not the spectrum. The eigen-decomposition is the subject of *The Eigenbasis of a Spectrally Regular Biquaternion*, and it asks for distinct eigenvalues, a condition that the decomposition never asks for and does not need.

**Not a pair of multipliers.** $\mathcal U$ and $\mathcal V$ are unitary operators and not elements. The unitary operators form $\mathrm{U}(4)$, of real dimension sixteen; the unitary elements form $\mathrm{U}(\mathbb{B})$, isomorphic to $\mathrm{U}(2)$ and of real dimension four; and the two-sided operators whose two multipliers are unitary form a subgroup of real dimension seven, the eight of $\mathrm{U}(\mathbb{B})\times\mathrm{U}(\mathbb{B})$ less the circle of pairs $(\lambda e_t,\lambda^{-1}e_t)$ with $\lvert\lambda\rvert=1$, which acts trivially. So the generic unitary of a decomposition is neither a left multiplier nor a two-sided operator, and the factorization does not read the multiplication.

**The independence of the two sides.** $\mathcal U$ acts on the target and $\mathcal V$ on the source, and they are chosen independently: nothing ties the image family to the source family except the list of weights. This independence is the operator-theoretic content of the decomposition, and it is why the multiplication cannot be read from it. A two-sided operator ties its two families by the product rule of §*The Weights of Two Multipliers*; a generic endomorphism leaves them free, and this is the failure of the converse in §*The Rank-One Endomorphisms and the Products* seen from the other end.

**The layer that carries the statement.** The multiplication does enter the definition of the form, which is the scalar part of a product, but it enters there and nowhere else: only the scalar functional $\operatorname{Sc}$ and the star are used, and no other part of the product is read. The decomposition is therefore a statement about $\mathbb{B}$ as a four-dimensional complex Hilbert space, and it holds unchanged in $\mathbb{C}^{4}$. What the algebra adds is read after the fact and in one direction, from the multiplication to the decomposition: the weights of the multipliers, the rank pattern of the products, and the sixteen basis operators.

## Summary

Every endomorphism of $\mathbb{B}$ is a sum of at most four elementary endomorphisms $\mathcal P_{\tilde U_k,\tilde V_k}(\tilde X)=\tilde U_k\langle\tilde X,\tilde V_k\rangle_{*}$ with orthonormal families and decreasing weights $\rho_k$, the weights being the square roots of the eigenvalues of $F^{*}F$; this is the spectral theorem applied to the positive operator $F^{*}F$, and it is proved here rather than quoted. The same theorem has an operator form, $F=\mathcal U\Sigma\mathcal V^{*}$ with two unitary operators and a self-adjoint positive scale, and the freedom of the pair is the single condition $W\Sigma=\Sigma Z$. Written in the algebra, the three factors are sums of four atoms, $\Sigma=\sum_k\rho_k\mathcal P_{e_k,e_k}$ being the scale in the basis of the units; and for a two-sided operator all three collapse into elements, $L_{\tilde Q_1}R_{\tilde Q_2}=L_{\tilde U_1}R_{\tilde U_2}L_{\tilde H_1}R_{\tilde H_2}$ with the modulus $L_{\tilde H_1}R_{\tilde H_2}$.

The weights obey the identities $\rho_1\rho_2\rho_3\rho_4=\lvert\det F\rvert$, $\rho_1^{2}+\rho_2^{2}+\rho_3^{2}+\rho_4^{2}=\lVert F\rVert^{2}$ and $\rho_1=\lVert F\rVert_{\mathrm{op}}$; the number of positive weights is the rank; the truncation at $s$ terms is the nearest endomorphism of rank at most $s$, with the min-max characterisation and the interlacing behind it; and the freedom of the two families is a phase per term, a unitary mixing inside each group of equal weights, and a completion of the vanishing terms.

The multiplication rewrites the picture, and this is what the article adds to the decomposition of a map of a four-dimensional complex space. The product meets the decomposition on the zero-divisor cone: a two-sided operator with two zero-divisor multipliers has rank one, and the converse holds for an elementary endomorphism exactly when both its vectors are zero divisors, so the products are a family of dimension four inside the six of all rank-one endomorphisms, and the generic atom is not a product. An atom that is a product has two normalisations at once, orthonormal for the form and degenerate for the product, and it carries a single positive weight. The weights of a left multiplier are a pair repeated twice, and that pair is the two algebraic norms of the element read backwards, $\rho_1^{2}+\rho_2^{2}=2\langle\tilde Q,\tilde Q\rangle_{*}$ and $\rho_1\rho_2=\lvert N(\tilde Q)\rvert$, from which the closed form of the pair follows. The weights of a two-sided operator are the four products of the two pairs, so its rank is $0$, $1$, $2$ or $4$ and never $3$, and the two-sided operator has its two middle weights equal.

The two normalisations of a singular vector are different conditions, and the article separates them: orthonormal means of Hermitian norm one, while the algebra's own unit condition is $N=1$. The weights are what connects the two, and the sixteen basis operators show the other face of the ambient space, an orthogonal basis of invertible operators against the cone of the rank-one ones.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $G$ | An endomorphism of $\mathbb{B}$, and the competing endomorphism of the truncation |
| $F^{*}$ | The adjoint of $F$, the Hermitian adjoint of the operator |
| $\lVert F\rVert$, $\lVert F\rVert_{\mathrm{op}}$ | The Hilbert–Schmidt norm and the operator norm |
| $\langle\!\langle F,G\rangle\!\rangle$ | The form on the operator space |
| $\mathrm{I}_4$, $\det F$, $\operatorname{rank}F$ | The identity operator, the determinant and the rank |
| $\tilde Q$, $\tilde Q_1$, $\tilde Q_2$ | An element, and the two multipliers of a two-sided operator |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | The scalar unit and the three vector units |
| $\tilde Q^{*}$, $\tilde Q^{\natural}$ | The Hermitian and the quaternion conjugations |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$ | The Hermitian form, $\operatorname{Sc}(\tilde Q_1\tilde Q_2^{*})$ |
| $\lVert\tilde Q\rVert^{2}=\langle\tilde Q,\tilde Q\rangle_{*}$ | The Hermitian norm of an element |
| $N(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ | The quaternionic algebraic norm, multiplicative and complex-valued |
| $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | The complex square of the vector part |
| $L_{\tilde Q}$, $R_{\tilde Q}$ | The left and the right multiplier |
| $L_{\tilde Q_1}R_{\tilde Q_2}$ | The two-sided operator, left multiplier first |
| $\mathrm{Sd}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ | The two-sided operator |
| $\mathcal P_{\tilde U_1,\tilde U_2}$ | The elementary endomorphism, $\tilde X\mapsto\tilde U_1\langle\tilde X,\tilde U_2\rangle_{*}$ |
| $\rho_k(F)$ | The $k$-th weight of the endomorphism $F$ |
| $\rho_1(\tilde Q),\rho_2(\tilde Q)$ | The two weights of the element $\tilde Q$ |
| $\mathsf M_2(\tilde Q)$ | The $2\times2$ image of the element |
| $\mathcal U$, $\mathcal V$, $\Sigma$ | The two unitary operators and the scale of the operator form |
| $\lvert F\rvert=(F^{*}F)^{1/2}$, $\Pi_i$ | The modulus of $F$, and the spectral projectors of the scale |
| $\tilde H$, $\tilde H_1$, $\tilde H_2$ | The Hermitian factor of an element, of nonnegative spectrum |
| $\mathrm{vec}(A)$, $A_1\otimes A_2^{\mathsf T}$ | The model read row by row, and the Kronecker product of two model arrays |

## Further Reading

- [Product and Form Conventions](product-and-form-conventions.html). The twelve products and the four forms, with the letters the norms of this article are read from.
- [Norm and Unitary Conventions](norm-and-unitary-conventions.html). The layer tables, the qualified regularity, and the unitary convention that fixes what *unit* means on each layer.
- [Operator Family Conventions](operator-family-conventions.html). The four families, their letters, the slots and the four adjoint signs.
- [Matrix Representations Conventions](matrix-representations-conventions.html). The $2\times2$ isomorphism and the $4\times4$ regular representation, with the sixteen basis operators.
- [Operators Acting on Two Sides](operators-acting-on-two-sides.html). The cone, the composition law, the generation theorem and the plain adjoint against which the Hermitian adjoint of this article is read.
- [The Endomorphisms of the Biquaternion Algebra](the-endomorphisms-of-the-biquaternion-algebra.html). The ambient space, its dimension and its coordinate reading.
- [The Peirce Basis of a Peirce Decomposition of the Biquaternion Algebra](the-peirce-basis-of-the-biquaternion-algebra.html). The four corners that the decomposition is not.
- [The Eigenbasis of a Spectrally Regular Biquaternion](the-eigenbasis-of-a-spectrally-regular-biquaternion.html). The eigenvalues of left multiplication, which the weights are not.
