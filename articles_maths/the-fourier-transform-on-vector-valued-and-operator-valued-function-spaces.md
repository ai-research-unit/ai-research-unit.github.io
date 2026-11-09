# __The Fourier Transform on Vector-Valued and Operator-Valued Function Spaces__

## Introduction

The transform of a function with values in a Hilbert space is the transform of each of its coordinates, and no new integral appears. This article proves that sentence and then works out what it costs: nothing in the formula, and something in every statement about convergence, in what counts as a product, and in what normalises the measure on the dual group.

**The three settings.** Throughout, $H$ is a separable complex Hilbert space with inner product $\langle\cdot,\cdot\rangle$ linear in the second variable, and $\mathcal{L}(H)$ is the algebra of bounded operators on it. The first setting is $L^2(\mathbb{R}^n;H)$, the Bochner square-integrable functions, normed by $\lVert f\rVert_2^2=\int\lVert f(x)\rVert^2dx$. The second replaces $H$ by the Hilbert–Schmidt class inside $\mathcal{L}(H)$, so that the functions are operator-valued; here the value space carries a product and a trace, and both are used. The third replaces $\mathbb{R}^n$ by a locally compact abelian group $G$: characters replace exponentials, Haar measure replaces Lebesgue measure, and the constant $(2\pi)^n$ becomes a density on the dual group.

**What is proved here.** Four theorems. The coordinate formula, and the fact that the transform commutes with every bounded operator on $H$, in §*The Transform of a Vector-Valued Function*. The isometry with the constant $(2\pi)^n$, for every $H$, and the unitary it defines, in §*The Isometry and the Unitary*. The Hilbert–Schmidt isometry and the convolution theorem for operator-valued functions, in §*Operator-Valued Functions*. The transfer of positivity from a kernel to its transform, with the diagonal in integrated form, in §*Kernels and Their Transforms*. A fifth result, the Plancherel measure on the dual of a locally compact abelian group and the inversion that goes with it, occupies §*Inversion on a Locally Compact Abelian Group*; its scalar case is quoted and the passage to $H$-valued functions is proved.

**What is quoted, and with which hypotheses.** The scalar Plancherel identity on $\mathbb{R}^n$, with its constant, is the one of *The Inverse Fourier Transform of a Symbol*. The scalar Plancherel theorem for a locally compact abelian group is quoted from *A Course in Abstract Harmonic Analysis* of Folland, with its hypotheses: the group is locally compact, abelian, and carries a Haar measure, which in the abelian case is automatically two-sided invariant. The fact that $L^\infty$ acts on $L^2$ as a maximal abelian subalgebra is quoted from the same source and is used once, in §*The Uniqueness Claim*. The Kolmogorov decomposition of a positive-definite kernel is quoted from *Reproducing Kernel Hilbert Spaces*, and the trace formula for a trace-class operator with continuous kernel is quoted from *Trace Ideals and Their Applications* of Simon. Both are used only to say what the objects are.

**The one unverified claim.** The article needs one statement that it does not prove, and it is this: **the transform is unique up to a unitary identification of the target and a choice of normalisation.** That is the form in which the claim is stated here, and it is quoted from Folland, not proved here in the generality stated. §*The Uniqueness Claim* proves the corresponding statement for $G=\mathbb{R}^n$, where it is a computation with the commutant of the multiplication algebra, and it records why the form "unique up to a scalar" is false: the scalar may be replaced by any unimodular function, and that is a unitary of the target and not a constant.

**Boundaries.** The symbol of a differential operator, its zero set and the kernel of its reciprocal belong to *The Fourier Transform and the Symbol of a Differential Operator* and to *The Inverse Fourier Transform of a Symbol*; this article uses neither. The placement of the transform in a triple of test spaces is *The Fourier Transform on a Gelfand Triple*. The transform of a distribution, and the sense in which an operator-valued function defines one, is *Distributions and Fundamental Solutions*. The non-abelian Plancherel theorem, where the dual is not a group and the inversion is an integral over a space of representations, is *Unitary Representations and the Plancherel Theorem*, and nothing here extends to it. The convolution of functions on a group is *Convolution on a Group*, and the Haar measure is *Locally Compact Groups and Haar Measure*; both are taken as given.

**The trap, and it has one word.** That word is convergence. In the scalar theory a transform is an integral of a function, and the only question is whether the integral exists. Here the integral is a Bochner integral, so it exists when the norm is integrable and $H$ is separable; but the limit of a sequence of such integrals may be taken in the norm of $H$, in the weak topology of $H$, in the Hilbert–Schmidt norm of $\mathcal{L}(H)$, or weakly as an operator, and these four are different statements. **Every theorem below names its mode of convergence**, and a theorem that names none is a defect rather than a shorthand.

**The phrase "the transform does not see $H$".** It has a precise meaning, given in §*The Transform of a Vector-Valued Function*: the transform commutes with every bounded operator on $H$, so it acts as the identity on the $H$ factor and as the scalar transform on the other. It does not mean that $H$ is irrelevant. The theorem of §*Kernels and Their Transforms* is a statement about positivity, and positivity is a property of the inner product of $H$; the theorem of §*Operator-Valued Functions* is a statement about a product, and the product is a property of $\mathcal{L}(H)$.

## The Transform of a Vector-Valued Function

**Definition (the space).** A function $f:\mathbb{R}^n\to H$ is **strongly measurable** when it is a pointwise limit almost everywhere of a sequence of countably valued functions; for separable $H$ this is the same as the measurability of every coordinate $\langle f,u\rangle$. It is in $L^2(\mathbb{R}^n;H)$ when it is strongly measurable and $\int\lVert f(x)\rVert^2dx<\infty$, and that space is complete for the norm $\lVert f\rVert_2$, with inner product $\langle f,g\rangle=\int\langle f(x),g(x)\rangle dx$. It is in $L^1(\mathbb{R}^n;H)$ when $\int\lVert f(x)\rVert dx<\infty$.

**Definition (the transform).** For $f\in L^1(\mathbb{R}^n;H)$ and $\zeta\in\mathbb{R}^n$, the **transform** is the Bochner integral

$$
\mathcal{F}[f](\zeta)=\int_{\mathbb{R}^n}e^{-i\zeta\cdot x}f(x)\,dx \in H .
$$

The integrand is strongly measurable and its norm is $\lVert f(x)\rVert$, which is integrable; the Bochner integral therefore exists, and $\lVert\mathcal{F}[f](\zeta)\rVert\le\lVert f\rVert_1$ for every $\zeta$. The scalar exponential is outside and the vector value is inside, so no question of non-commutativity arises at this stage.

**Proposition (the coordinate formula).** For $f\in L^1(\mathbb{R}^n;H)$, every $u\in H$, and every $\zeta$,

$$
\big\langle \mathcal{F}[f](\zeta),u\big\rangle=\mathcal{F}\big[\langle f(\cdot),u\rangle\big](\zeta).
$$

*Proof.* The map $v\mapsto\langle v,u\rangle$ is continuous and linear on $H$, and a continuous linear map carries a Bochner integral to the integral of the images. The scalar function $x\mapsto\langle f(x),u\rangle$ is integrable because $\lvert\langle f(x),u\rangle\rvert\le\lVert f(x)\rVert\lVert u\rVert$. The right side is by definition the scalar transform of that function.

**Proposition (bounded operators pass through).** Let $T\in\mathcal{L}(H)$ and $f\in L^1(\mathbb{R}^n;H)$. Then $Tf\in L^1(\mathbb{R}^n;H)$ and $\mathcal{F}[Tf](\zeta)=T\mathcal{F}[f](\zeta)$ for every $\zeta$.

*Proof.* Continuity of $T$ gives $\lVert Tf\rVert\le\lVert T\rVert\lVert f\rVert$, so $Tf$ is integrable, and the same continuity carries the Bochner integral through, since $T$ applied to a limit of simple functions is the limit of their images.

**Corollary (the transform is the identity on the value space).** Let $(\varphi_j)$ be an orthonormal basis of $H$ and write $f_j=\langle f,\varphi_j\rangle$. Then, for each $\zeta$, the series

$$
\mathcal{F}[f](\zeta)=\sum_{j}\mathcal{F}[f_j](\zeta)\,\varphi_j
$$

converges in the norm of $H$, and $\lVert\mathcal{F}[f](\zeta)\rVert^2=\sum_j\lvert\mathcal{F}[f_j](\zeta)\rvert^2$.

*Proof.* By the coordinate formula, $\langle\mathcal{F}[f](\zeta),\varphi_j\rangle=\mathcal{F}[f_j](\zeta)$, so the coefficients of $\mathcal{F}[f](\zeta)$ in the basis are the scalar transforms, and the norm identity is Parseval's. The finite partial sums form a Cauchy sequence, because the squared norm of the tail of the series is the sum of the tail of the non-negative series on the right, which converges; and the limit has the stated norm.

**Remark (what has and has not been proved).** The corollary is the whole reason the theory has no new formula: the transform of $f$ is assembled from the scalar transforms of the coordinates, and the assembly is the identity map of $H$. Equivalently, $\mathcal{F}$ acting on $L^2(\mathbb{R}^n;H)$ is the tensor product of the scalar transform with the identity of $H$, in the sense that it agrees on the algebraic tensor product $L^2(\mathbb{R}^n)\odot H$ with $\mathcal{F}\otimes 1_H$ and is continuous there. **A change of orthonormal basis of $H$ does not change the transform of any function**, which is the first hint of the uniqueness statement of §*The Uniqueness Claim*.

**Remark (what the four convergences are).** The series above converges in the norm of $H$. A statement about $Tf$ may instead be read as a weak operator statement, that $\langle T\mathcal{F}[f],u\rangle$ is the integral of $\langle Tf,u\rangle$ for each $u$. A statement about an operator-valued transform may be read in the Hilbert–Schmidt norm, which is the norm of the space $\mathcal{L}_2(H)$ in which the values lie. And a statement about inversion may be read as convergence of the inverse integrals in the norm of $L^2$, which is a statement about a sequence of functions and not about a sequence of vectors. The four are separate, and the theorems below say which they use.

## The Isometry and the Unitary

**Theorem (Plancherel for $H$-valued functions).** Let $f\in L^1\cap L^2(\mathbb{R}^n;H)$. Then $\mathcal{F}[f]\in L^2(\mathbb{R}^n;H)$ and

$$
\int_{\mathbb{R}^n}\lVert\mathcal{F}[f](\zeta)\rVert^2\,d\zeta=(2\pi)^n\int_{\mathbb{R}^n}\lVert f(x)\rVert^2\,dx .
$$

*Proof.* Choose an orthonormal basis $(\varphi_j)$ of $H$ and write $f_j=\langle f,\varphi_j\rangle$. Each $f_j$ lies in $L^1\cap L^2(\mathbb{R}^n;\mathbb{C})$, because $\lvert f_j\rvert\le\lVert f\rVert$. By the corollary of §*The Transform of a Vector-Valued Function*, $\lVert\mathcal{F}[f](\zeta)\rVert^2=\sum_j\lvert\mathcal{F}[f_j](\zeta)\rvert^2$ for every $\zeta$, a series of non-negative terms; integrating it and interchanging sum and integral by monotone convergence gives $\sum_j\lVert\mathcal{F}[f_j]\rVert_2^2$ on the left. The scalar identity of *The Inverse Fourier Transform of a Symbol* gives $\lVert\mathcal{F}[f_j]\rVert_2^2=(2\pi)^n\lVert f_j\rVert_2^2$ for each $j$, and Parseval gives $\sum_j\lVert f_j\rVert_2^2=\lVert f\rVert_2^2$. Assembling the three equalities gives the statement, and the value $(2\pi)^n\lVert f\rVert_2^2$ is finite, so the series converges and $\mathcal{F}[f]$ lies in $L^2$.

**Corollary (the unitary).** The operator $\mathcal{U}=(2\pi)^{-n/2}\mathcal{F}$, defined first on $L^1\cap L^2(\mathbb{R}^n;H)$, extends by continuity to an isometry of $L^2(\mathbb{R}^n;H)$ onto itself, and it is surjective, hence unitary.

*Proof.* The isometry is the theorem; $L^1\cap L^2$ is dense in $L^2$ because the compactly supported continuous $H$-valued functions lie in it and are dense; and an isometry with dense range is surjective onto a closed subspace, so it remains to see that the range is dense. The inverse operator $(2\pi)^{-n/2}\mathcal{F}$ acting on $L^1\cap L^2$ is an isometry with the same constant, read with the opposite sign in the exponent, and it is a left inverse on that dense set; hence the range of $\mathcal{U}$ contains the range of the inverse operator, which is dense.

**Corollary (the fourth power).** On $L^2(\mathbb{R}^n;H)$ one has $\mathcal{U}^2f(x)=f(-x)$ and $\mathcal{U}^4=1$.

*Proof.* Both statements are read in coordinates: the scalar identity $\mathcal{F}^2g(x)=(2\pi)^ng(-x)$ holds for $g\in L^1\cap L^2$, and by the corollary of §*The Transform of a Vector-Valued Function* the transform of $f$ is assembled from the transforms of its coordinates, so applying it twice multiplies each coordinate by $(2\pi)^n$ and reflects it. Hence $\mathcal{U}^2$ is the reflection $f\mapsto f(-\cdot)$, whose square is the identity.

**Remark (the constant does not depend on the dimension of $H$).** The formula carries $(2\pi)^n$ and not $(2\pi)^n\dim H$ or an analogous power, because the identity is applied once to $f$ as a whole and not once per coordinate. When $H$ is finite dimensional, the theorem of *The Inverse Fourier Transform of a Symbol* applied in a complex basis of $H$ gives one scalar identity per basis vector, with weights from the Gram matrix, and the weights cancel between the two sides; the present proof replaces that computation by a sum over an orthonormal basis, which is the same computation with the Gram matrix taken to be the identity. **Neither route produces a factor depending on the dimension of $H$, and this is the honest content of the phrase "the constant is the same".**

**Remark (a second reading, by duality).** Since $\mathcal{U}$ is unitary, its adjoint is its inverse, and the inversion formula on $L^2(\mathbb{R}^n;H)$ is the statement $\mathcal{U}^{*}=\mathcal{U}^{-1}$. Written with integrals and read weakly, it says that $\langle f,g\rangle=(2\pi)^{-n}\int\langle\mathcal{F}[f](\zeta),\mathcal{F}[g](\zeta)\rangle\,d\zeta$ for $g\in L^2(\mathbb{R}^n;H)$, which is the polarization of the theorem. The right side is a scalar integral of a scalar function, so the statement is again a scalar identity, and this is why the vector case needs no new apparatus.

## Operator-Valued Functions

**Definition (the Hilbert–Schmidt class).** An operator $T\in\mathcal{L}(H)$ is **Hilbert–Schmidt** when $\sum_j\lVert T\varphi_j\rVert^2<\infty$ for one, and then for every, orthonormal basis $(\varphi_j)$; the sum is the square of the **Hilbert–Schmidt norm** $\lVert T\rVert_2$, and the class $\mathcal{L}_2(H)$ is a Hilbert space for the inner product $\langle S,T\rangle_2=\sum_j\langle S\varphi_j,T\varphi_j\rangle=\operatorname{tr}(S^{*}T)$.

**Lemma (independence of the basis).** The number $\sum_{j,k}\lvert\langle T\varphi_j,\varphi_k\rangle\rvert^2$ does not depend on the orthonormal basis, and it equals $\operatorname{tr}(T^{*}T)$.

*Proof.* For fixed $j$ the sum over $k$ is $\lVert T\varphi_j\rVert^2$ by Parseval. The sum over $j$ of these is the trace of $T^{*}T$, which is a positive trace-class operator, and the trace of such an operator is the sum of its diagonal entries in any orthonormal basis, by monotone convergence applied to the definition of the trace.

**Definition (the weak transform).** For $T:\mathbb{R}^n\to\mathcal{L}(H)$ and $\zeta\in\mathbb{R}^n$, the **transform** is the operator $\mathcal{F}[T](\zeta)$ determined by

$$
\big\langle \mathcal{F}[T](\zeta)u,v\big\rangle=\mathcal{F}\big[\langle T(\cdot)u,v\rangle\big](\zeta)
$$

for all $u,v\in H$.

**Proposition (the weak transform agrees with the strong one).** If $T\in L^1(\mathbb{R}^n;\mathcal{L}_2(H))$, then the Bochner integral $\int e^{-i\zeta\cdot x}T(x)\,dx$ converges in $\mathcal{L}_2(H)$ and defines the same operator as the weak definition; moreover $\lVert\mathcal{F}[T](\zeta)\rVert_2\le\int\lVert T(x)\rVert_2dx$.

*Proof.* The class $\mathcal{L}_2(H)$ is a Hilbert space, so the integrand is an $\mathcal{L}_2(H)$-valued function with integrable norm, and §*The Transform of a Vector-Valued Function* applies with $H$ replaced by $\mathcal{L}_2(H)$. The two definitions agree because $S\mapsto\langle Su,v\rangle$ is a continuous linear functional on $\mathcal{L}_2(H)$ for fixed $u,v$ in $H$, and by the coordinate formula applied in that Hilbert space. The bound is the bound on a Bochner integral.

**Theorem (the Hilbert–Schmidt isometry).** Let $T\in L^1\cap L^2(\mathbb{R}^n;\mathcal{L}_2(H))$. Then

$$
\int_{\mathbb{R}^n}\lVert\mathcal{F}[T](\zeta)\rVert_2^2\,d\zeta=(2\pi)^n\int_{\mathbb{R}^n}\lVert T(x)\rVert_2^2\,dx .
$$

*Proof.* Apply the theorem of §*The Isometry and the Unitary* in the Hilbert space $\mathcal{L}_2(H)$, whose inner product is $\langle S,T\rangle_2$. The norm there is $\lVert\cdot\rVert_2$ and the transform is the one just defined. No structure of $H$ beyond separability is used.

**Proposition (the convolution theorem).** Let $T\in L^1(\mathbb{R}^n;\mathcal{L}(H))$ and $f\in L^1(\mathbb{R}^n;H)$, and define $(T*f)(x)=\int_{\mathbb{R}^n}T(x-y)f(y)\,dy$. Then $T*f\in L^1(\mathbb{R}^n;H)$ and $\mathcal{F}[T*f](\zeta)=\mathcal{F}[T](\zeta)\,\mathcal{F}[f](\zeta)$ for every $\zeta$.

*Proof.* The integrand is bounded by $\lVert T(x-y)\rVert\lVert f(y)\rVert$, whose double integral is $\lVert T\rVert_1\lVert f\rVert_1$; Fubini applies. Substituting $z=x-y$ in the transform,

$$
\mathcal{F}[T*f](\zeta)=\int_{\mathbb{R}^n}\int_{\mathbb{R}^n}e^{-i\zeta\cdot(z+y)}T(z)f(y)\,dy\,dz ,
$$

and the double integral factorises because the exponential does and because $T(z)f(y)$ is the product of an operator and a vector. The first factor is $\mathcal{F}[T](\zeta)$ and the second is $\mathcal{F}[f](\zeta)$.

**Remark (this is the content the operator values add).** For $H$-valued functions alone the transform is the scalar transform in each coordinate, and no theorem above uses more than that. The operator-valued case adds two structures: the **product**, used in the proposition just proved, and the **trace**, used in the isometry. The product turns convolution into operator multiplication, and the placement matters: $T$ acts on the left of $f$, and $\mathcal{F}[T](\zeta)\mathcal{F}[f](\zeta)$ is the product of an operator and a vector. Had the kernel been placed on the right, with $(f*T)(x)=\int f(x-y)T(y)\,dy$, the conclusion would be $\mathcal{F}[f*T](\zeta)=\mathcal{F}[f](\zeta)\,\mathcal{F}[T](\zeta)$ with the vector multiplying the operator, which is a different object and is defined only when $H$ is finite dimensional. **The order of kernel and function is part of the theorem**, and it is fixed at the start of every statement that uses it.

## Kernels and Their Transforms

### The scalar kernel

**Definition (positive-definite kernel).** Let $X$ be a set. A function $K:X\times X\to\mathbb{C}$ is a **positive-definite kernel** when, for every finite family $x_1,\dots,x_N$ in $X$ and every $w_1,\dots,w_N$ in $\mathbb{C}$,

$$
\sum_{p,q=1}^{N}\overline{w_p}\,w_q\,K(x_p,x_q)\ \ge\ 0 .
$$

Such a $K$ is automatically sesquiholomorphic, $K(y,x)=\overline{K(x,y)}$, and the completion of the span of the functions $K_x=K(\cdot,x)$ for the inner product $\langle K_x,K_y\rangle=K(y,x)$ is a Hilbert space of functions on $X$ on which $K$ reproduces: $f(x)=\langle f,K_x\rangle$. This is the construction of *Reproducing Kernel Hilbert Spaces*, quoted here and not repeated.

**Lemma (a kernel tested against a bounded integrable function).** Let $K$ be positive definite and integrable on $\mathbb{R}^n\times\mathbb{R}^n$, and let $\Lambda\in L^1\cap L^\infty(\mathbb{R}^n)$. Then $\int\int K(x,y)\Lambda(x)\overline{\Lambda(y)}\,dx\,dy\ge0$, the double integral being taken over $\mathbb{R}^n\times\mathbb{R}^n$.

*Proof.* Choose step functions $\Lambda_m$, bounded by $\lVert\Lambda\rVert_\infty$ and converging to $\Lambda$ in $L^1$. For a step function the double integral is the finite sum $\sum_{i,j}c_i\overline{c_j}K(x_i,x_j)\lvert E_i\rvert\lvert E_j\rvert$, with $E_i$ the pieces on which $\Lambda_m$ is constant, which is non-negative by positive definiteness. The double integral is continuous in $\Lambda$ in the $L^1$ norm, because $\lvert K\rvert$ is integrable and both $\Lambda$ and $\Lambda_m$ are bounded by $\lVert\Lambda\rVert_\infty$. Hence the limit of the non-negative numbers is non-negative.

**Theorem (the transform of a kernel is a kernel).** Let $K$ be a positive-definite kernel on $\mathbb{R}^n\times\mathbb{R}^n$ that is integrable. Then the function

$$
\widehat K(\zeta,\eta)=\int_{\mathbb{R}^n}\int_{\mathbb{R}^n}e^{-i(\zeta\cdot x-\eta\cdot y)}\,K(x,y)\,dx\,dy
$$

is a positive-definite kernel on $\mathbb{R}^n\times\mathbb{R}^n$.

*Proof.* Let $\zeta_1,\dots,\zeta_N$ and $w_1,\dots,w_N$ be given, and put $\Lambda(x)=\sum_p\overline{w_p}e^{-i\zeta_p\cdot x}$, which is bounded and integrable. Exchanging the finite sum with the double integral, which is legitimate because the sum is finite,

$$
\sum_{p,q}\overline{w_p}w_q\widehat K(\zeta_p,\zeta_q)=\int\int K(x,y)\,\Lambda(x)\,\overline{\Lambda(y)}\,dx\,dy ,
$$

and the right side is non-negative by the lemma. Since the families were arbitrary, $\widehat K$ is positive definite.

**Definition and proposition (the diagonal).** The **diagonal** of a kernel $K$ is the function $x\mapsto K(x,x)$, and the diagonal of the transformed kernel is $\zeta\mapsto\widehat K(\zeta,\zeta)$. The second is the **symbol of the kernel**, the function $\widehat K(\zeta,\zeta)=\int\int e^{-i\zeta\cdot(x-y)}K(x,y)\,dx\,dy$, which is the quadratic form of the kernel at the frequency $\zeta$ and is non-negative by the theorem with $\eta=\zeta$.

**Proposition (the two diagonals agree in integral).** Let $K$ be continuous on $\mathbb{R}^n\times\mathbb{R}^n$ and suppose the operator $T_K$ with kernel $K$ is of trace class. Then

$$
\int_{\mathbb{R}^n}\widehat K(\zeta,\zeta)\,d\zeta=(2\pi)^n\int_{\mathbb{R}^n}K(x,x)\,dx .
$$

*Proof.* For $g\in C_c^\infty(\mathbb{R}^n)$ one computes $(\mathcal{F}T_K\mathcal{F}^{-1}g)(\zeta)=\int e^{-i\zeta\cdot x}(T_K\mathcal{F}^{-1}g)(x)\,dx$ and $\mathcal{F}^{-1}g(x)=(2\pi)^{-n}\int e^{ix\cdot\eta}g(\eta)\,d\eta$; substituting and exchanging the integrals shows that $(2\pi)^{-n}\widehat K$ is the kernel of $\mathcal{F}T_K\mathcal{F}^{-1}$. The trace of an operator with a continuous kernel is the integral of its diagonal, quoted from *Trace Ideals and Their Applications* of Simon, and the trace is invariant under conjugation by an invertible operator. Applying both to $\mathcal{F}T_K\mathcal{F}^{-1}$ gives $\int(2\pi)^{-n}\widehat K(\zeta,\zeta)\,d\zeta=\int K(x,x)\,dx$.

**Remark (pointwise the two diagonals differ, and the Gaussian is where they nearly agree).** Take the rank-one kernel $K(x,y)=\psi(x)\overline{\psi(y)}$ with $\psi$ integrable. Its transform is the rank-one kernel $\widehat K(\zeta,\eta)=\hat\psi(\zeta)\overline{\hat\psi(\eta)}$, so the diagonal of the transformed kernel is $\lvert\hat\psi(\zeta)\rvert^2$ while the diagonal of the original is $\lvert\psi(x)\rvert^2$. The two agree pointwise only when $\psi$ is an eigenfunction of the transform. For $\psi(x)=e^{-\lvert x\rvert^2/2}$ one has $\hat\psi=(2\pi)^{n/2}\psi$, so that $\lvert\hat\psi\rvert^2=(2\pi)^n\lvert\psi\rvert^2$: the Gaussian diagonal is reproduced up to the constant, and the constant is exactly the factor by which the diagonal of a self-dual kernel rescales. **The proposition above is the only sense in which the two diagonals agree for a general kernel: the agreement is an identity of integrals, and it is a coincidence of pointwise values only for the self-dual kernels.**

### The operator-valued kernel

**Definition (the operator-valued kernel).** A function $K:X\times X\to\mathcal{L}(H)$ is a positive-definite kernel when $\sum_{p,q}\langle K(x_p,x_q)u_q,u_p\rangle\ge0$ for every finite family of points and every finite family of vectors in $H$. The Kolmogorov decomposition, quoted from *Reproducing Kernel Hilbert Spaces*, provides an $H$-valued Hilbert space on which $K$ reproduces in the sense $f(x)=\langle f,K_x\rangle$ with $K_x$ taking values in the operators of $H$; nothing below uses the decomposition, only the inequality.

**Theorem (the transform of an operator-valued kernel is a kernel).** Let $K:\mathbb{R}^n\times\mathbb{R}^n\to\mathcal{L}(H)$ be positive definite in the sense above and integrable in the Bochner sense. Then the function

$$
\widehat K(\zeta,\eta)=\int_{\mathbb{R}^n}\int_{\mathbb{R}^n}e^{-i(\zeta\cdot x-\eta\cdot y)}\,K(x,y)\,dx\,dy
$$

is a positive-definite operator-valued kernel.

*Proof.* Let $\zeta_1,\dots,\zeta_N$, $w_1,\dots,w_N\in H$, and put $\Lambda(x)=\sum_p w_p\,e^{-i\zeta_p\cdot x}$, an $H$-valued bounded integrable function. Then $\sum_{p,q}\langle\widehat K(\zeta_p,\zeta_q)w_q,w_p\rangle=\int\int\langle K(x,y)\Lambda(y),\Lambda(x)\rangle\,dx\,dy$, and the right side is non-negative by the definition, applied to step-function approximations of $\Lambda$ exactly as in the scalar lemma. The families being arbitrary, $\widehat K$ is positive definite.

**Corollary (the diagonal is a positive operator).** For every $\zeta$, the operator $\widehat K(\zeta,\zeta)$ is positive, and its trace, when finite, is $\sum_j\widehat K(\zeta,\zeta)$ evaluated on an orthonormal basis, which is the sum of scalar symbols of the kernels $\langle K(\cdot,\cdot)\varphi_j,\varphi_j\rangle$.

*Proof.* Positivity is the theorem with $\eta=\zeta$ and $N=1$. The trace statement is the definition of the diagonal entries in a basis and the scalar case applied to each of them.

**Remark (positivity is the reason the value space matters).** The transform commutes with bounded operators, so it cannot create or destroy operator structure; but it can create or destroy positivity of a kernel, and the theorem says that it does not destroy it. That statement is not a formal consequence of the commutation, because the transform is not positive on operators in general: an operator-valued function may be positive at every point of $\mathbb{R}^n$ while its transform is not, since the transform of a non-negative scalar function is not non-negative unless the function is a positive-definite kernel. **What is preserved is the double positivity of a kernel, and the hypothesis of the theorem is exactly that.**

## Inversion on a Locally Compact Abelian Group

### Haar measure and the dual group

**The setting, and what is quoted.** Let $G$ be a locally compact abelian group, written additively, with Haar measure $dx$; the abelian hypothesis makes the measure two-sided invariant, so the modular function is identically one. A **character** is a continuous homomorphism $\gamma:G\to\mathbb{T}$, and the set $\widehat G$ of characters, with the compact-open topology, is a locally compact abelian group, the **dual group**. These are *Locally Compact Groups and Haar Measure* and *Pontryagin Duality*; the transform on $G$ is

$$
\hat f(\gamma)=\int_G f(x)\,\overline{\gamma(x)}\,dx ,
$$

for $f\in L^1(G;H)$, the integral a Bochner integral and the convergence in the norm of $H$. The character is scalar-valued, so it sits outside the vector, exactly as the exponential did on $\mathbb{R}^n$.

**Proposition (the coordinate formula on a group).** For $f\in L^1(G;H)$ and $u\in H$, $\langle\hat f(\gamma),u\rangle=\widehat{\langle f,u\rangle}(\gamma)$, and for $T\in\mathcal{L}(H)$, $\widehat{Tf}=T\hat f$.

*Proof.* The two maps $v\mapsto\langle v,u\rangle$ and $v\mapsto Tv$ are continuous and linear, so both carry the Bochner integral to the integral of the images, as in §*The Transform of a Vector-Valued Function*.

### The Plancherel measure and its density

**Theorem (Plancherel, scalar case quoted and vector case proved).** There is a Haar measure $d\gamma$ on $\widehat G$, unique, such that for every $f\in L^1\cap L^2(G;\mathbb{C})$ the transform lies in $L^2(\widehat G;\mathbb{C})$ and

$$
\int_{\widehat G}\lvert\hat f(\gamma)\rvert^2\,d\gamma=\int_G\lvert f(x)\rvert^2\,dx .
$$

With that measure, and for $f\in L^1\cap L^2(G;H)$,

$$
\int_{\widehat G}\lVert\hat f(\gamma)\rVert_H^2\,d\gamma=\int_G\lVert f(x)\rVert_H^2\,dx ,
$$

and $\mathcal{U}f=\hat f$ extends to a unitary of $L^2(G;H)$ onto $L^2(\widehat G;H)$.

*Proof.* The scalar statement is the Plancherel theorem for a locally compact abelian group, quoted from *A Course in Abstract Harmonic Analysis* of Folland, together with the existence and uniqueness of the measure. The vector statement follows by choosing an orthonormal basis $(\varphi_j)$ of $H$, writing $f_j=\langle f,\varphi_j\rangle$, and repeating the argument of §*The Isometry and the Unitary*: the norm identity becomes a sum of scalar identities, and monotone convergence justifies the exchange. The unitary is then obtained by continuity on the dense set $L^1\cap L^2$.

**Definition (the Plancherel density).** The measure $d\gamma$ is the **Plancherel measure**. When $\widehat G$ is identified with a space carrying another measure $d\lambda$, say by a homeomorphism, the **density** is the function $\varpi$ with $d\gamma=\varpi\,d\lambda$, that is, the Radon–Nikodym derivative of the Plancherel measure against $d\lambda$. The density is not intrinsic; the pair of an identification and a density is.

**Remark (the constant of the classical formula is a density).** Take $G=\mathbb{R}^n$ and identify $\widehat G$ with $\mathbb{R}^n$ by $\gamma_\zeta(x)=e^{i\zeta\cdot x}$. Then $d\gamma=(2\pi)^{-n}d\zeta$, so the density is $\varpi(\zeta)=(2\pi)^{-n}$, and this is the whole origin of the constant in the inversion formula. Take instead the identification $\zeta\mapsto e^{2\pi i\zeta\cdot x}$, used when the frequency is counted in periods rather than in radians; then $d\gamma=d\zeta$ and the density is one. **The constant is not a property of the group; it is the Jacobian of the identification.** Under a linear change of the frequency variable by $L\in GL(n,\mathbb{R})$ the density changes by $\lvert\det L\rvert$, and the identity survives because the same factor appears in the measure on $\widehat G$.

**Remark (the compact case, for contrast).** For $G=\mathbb{T}^n$ with Haar measure of total one, the dual is $\mathbb{Z}^n$ with counting measure and the density is one; the transform is the sequence of Fourier coefficients, and the identity reads $\sum_{k\in\mathbb{Z}^n}\lvert\hat f(k)\rvert^2=\int_{\mathbb{T}^n}\lvert f\rvert^2$. For $G=\mathbb{Z}^n$ with counting measure the dual is $\mathbb{T}^n$ and the density is again one, with the roles exchanged. In both cases the inversion is a series or an integral over a compact group, and in neither case does a constant appear. **The $(2\pi)^n$ is the price of the additive line, and of nothing else.**

### Operator-valued inversion

**Theorem (inversion, operator-valued).** Let $F\in L^2(G;\mathcal{L}_2(H))$. Then $\hat F\in L^2(\widehat G;\mathcal{L}_2(H))$, the Hilbert–Schmidt identity

$$
\int_{\widehat G}\lVert\hat F(\gamma)\rVert_2^2\,d\gamma=\int_G\lVert F(x)\rVert_2^2\,dx
$$

holds, and the inversion formula

$$
F(x)=\int_{\widehat G}\hat F(\gamma)\,\gamma(x)\,d\gamma
$$

holds in the norm of $L^2(G;\mathcal{L}_2(H))$, that is, the integrals over an increasing family of compact subsets of $\widehat G$ converge to $F$ in that norm. If in addition $F$ is continuous, $F\in L^1$, and $\hat F\in L^1(\widehat G;\mathcal{L}_2(H))$, the formula holds pointwise in the Hilbert–Schmidt norm.

*Proof.* Apply the theorem of §*The Isometry and the Unitary* with $H$ replaced by the Hilbert space $\mathcal{L}_2(H)$: the Hilbert–Schmidt identity is that theorem, and the transform there is the weak transform of §*Operator-Valued Functions*, which agrees with the strong one by the proposition of that section. The pointwise statement is the scalar inversion theorem applied to each matrix entry $\langle F\varphi_j,\varphi_k\rangle$, followed by summation in the Hilbert–Schmidt norm, which is legitimate because $\hat F$ is integrable in that norm and the partial sums converge.

**Remark (what replaces the pointwise product).** In the scalar inversion the integrand is a number times a character. Here it is an operator times a character, and the order is fixed: the operator is on the left, which is the order in which the transform was defined. The two-sided version, with a character on each side of the operator, belongs to the biquaternion articles of the corpus, where the value algebra is not commutative and the placement carries information; on an abelian group with operator values the right placement is a different transform, not a variant of this one.

## The Uniqueness Claim

### The computation in Euclidean space

**The question.** The transform is defined by an integral, and an integral depends on a choice of measure and of a sign in the exponent. The question of this section is how much of the transform is forced by the requirement that it turn translations into multiplications. The answer, on $\mathbb{R}^n$, is: all of it except a unimodular factor and a constant.

**Notation.** Let $\tau_y$ be the translation $(\tau_yf)(x)=f(x+y)$ and let $\mu_y$ be the multiplication $(\mu_yg)(\zeta)=\gamma_y(\zeta)g(\zeta)$ with $\gamma_y(\zeta)=e^{i\zeta\cdot y}$. With this convention $\mathcal{F}[\tau_yf](\zeta)=e^{i\zeta\cdot y}\mathcal{F}[f](\zeta)$, so the transform intertwines $\tau_y$ with $\mu_y$ and not with $\mu_{-y}$.

**Proposition (the multiplication algebra is maximal abelian), quoted.** For a $\sigma$-finite measure space, the algebra $L^\infty$ acting by multiplication on $L^2$ is a maximal abelian subalgebra of $\mathcal{L}(L^2)$: every bounded operator commuting with all multiplications is itself a multiplication. This is quoted from *A Course in Abstract Harmonic Analysis* of Folland.

**Corollary (two transforms differ by a gauge).** Let $G=\mathbb{R}^n$ and let $\mathcal{U}_1,\mathcal{U}_2:L^2(G)\to L^2(\widehat G)$ be unitaries with $\mathcal{U}_i\tau_y=\mu_y\mathcal{U}_i$ for every $y\in G$. Then $\mathcal{U}_2\mathcal{U}_1^{-1}$ is the multiplication by a unimodular function $m$ on $\widehat G$, and

$$
\mathcal{U}_2=M_m\,\mathcal{U}_1,\qquad \lvert m(\zeta)\rvert=1\ \text{for almost every}\ \zeta .
$$

*Proof.* Put $V=\mathcal{U}_2\mathcal{U}_1^{-1}$, a unitary of $L^2(\widehat G)$. From the two intertwining relations, $V\mu_y=\mu_yV$ for every $y$. The $\mu_y$ generate the multiplication algebra of $L^\infty$ as a von Neumann algebra, by the spectral theorem applied to the commuting generators of the group; so $V$ commutes with that algebra, and by maximal abelian-ness $V=M_m$ for some $m\in L^\infty$. Unitarity of $V$ gives $\lvert m\rvert=1$ almost everywhere.

**Remark (this is the claim, for $\mathbb{R}^n$).** The corollary says that the transform is determined, among all unitaries intertwining translations with multiplications, by a unimodular function and a constant. The unimodular function is a unitary of the target space, in the precise sense that $g\mapsto mg$ is a unitary of $L^2(\widehat G)$; the constant is the normalisation. That is the content of the claim in the form stated in the Introduction, and on $\mathbb{R}^n$ it is proved.

**Remark (why "up to a scalar" is false).** Take $m(\zeta)=e^{i\lvert\zeta\rvert^2}$. Multiplication by $m$ is unitary, it commutes with every $\mu_y$, and it is not a constant. Hence there are unitaries intertwining translations with multiplications that differ from the standard transform by more than a scalar, and the statement "unique up to a scalar" is false as it stands. **The freedom is a unimodular function, not a number**, and a statement that omits the function omits the whole of the freedom.

### The quoted statement

**The claim, in the form used in this article, quoted and not proved.** For a locally compact abelian group $G$, the transform is unique up to a unitary identification of the target and a choice of normalisation. This is quoted from *A Course in Abstract Harmonic Analysis* of Folland, and it is the one statement of the article that is not proved here. The proof on $\mathbb{R}^n$ uses the maximal abelian property of the multiplication algebra, which is available for every $\sigma$-finite measure space; what is not done here is the corresponding argument on a general $\widehat G$, where the algebra generated by the characters must be identified before the commutant can be computed. The gap is real and it is named rather than papered over.

**Remark (what the claim does not say).** It does not say that the Plancherel measure is unique up to a scaling by a function. The measure is unique up to a positive constant, by the uniqueness of Haar measure on $\widehat G$, and the constant is fixed by the Plancherel identity. It does not say that the transform is unique up to a change of the identification of $\widehat G$ with a model space; such a change alters the density by the Jacobian and is absorbed with it, but it is a change of coordinates and not a change of the transform. **The only freedom is the unimodular factor and the normalisation, and neither of them is a change of measure or a map of the dual group:** a unimodular factor is a pointwise phase, and a phase moves no point.

**Remark (why the operator-valued case needs the scalar statement).** The transform on $L^2(G;\mathcal{L}_2(H))$ is the scalar transform applied entrywise in a basis of $H$, and it therefore inherits whatever uniqueness the scalar transform has. What it does not inherit is a separate uniqueness statement about the placement of the operator; that question is settled by the definition and not by a theorem, and it is the subject of the biquaternion article *Three Kernel Placements of the Biquaternion Fourier Transform*.

## Summary

The value space of a function does not change the Fourier transform: the transform acts on the scalar coordinate and as the identity on the values, and therefore carries over from the scalar theory with the same formula, the same constant, and the same inversion. What it changes is the meaning of the limit and the availability of extra structure. The isometry holds in the norm of $H$ with the constant $(2\pi)^n$, for every $H$, and defines a unitary whose square is the reflection. For operator-valued functions the Hilbert–Schmidt norm gives the same identity with the same constant, and the product of $\mathcal{L}(H)$ turns convolution into operator multiplication, with the operator on the left. A positive-definite kernel stays a positive-definite kernel under the transform in both variables, its diagonal maps to the symbol of the kernel, and the two diagonals agree in integral with the factor $(2\pi)^n$ and in pointwise value only for the self-dual kernels. On a locally compact abelian group the same theorems hold with characters in place of exponentials and Haar measure in place of Lebesgue measure; the constant of the classical formula is the density of the Plancherel measure against the chosen identification of the dual, and it disappears under the identification that counts frequencies in periods.

Three sentences carry the article. **The transform is the identity on the values and the scalar transform on the coordinates.** **The constant is a density, and a density is a choice of coordinates on the dual group.** **The freedom in the transform is a unimodular function, which is a unitary of the target, together with a normalisation.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H$ | A separable complex Hilbert space, the space of values |
| $\langle\cdot,\cdot\rangle$ | The inner product of $H$, linear in the second variable |
| $\mathcal{L}(H)$ | The bounded operators on $H$ |
| $\mathcal{L}_2(H)$ | The Hilbert–Schmidt operators, with norm $\lVert\cdot\rVert_2$ |
| $T$ | A bounded operator on $H$, and the value of an operator-valued function |
| $f,g$ | Functions with values in $H$ |
| $u,v,w_p$ | Vectors of $H$ |
| $\varphi_j$ | An orthonormal basis of $H$, indexed by $j$ and $k$ |
| $\mathcal{F}$ | The transform $\int e^{-i\zeta\cdot x}f(x)\,dx$ and its group analogue $\int f(x)\overline{\gamma(x)}\,dx$ |
| $\mathcal{U}$ | The unitary $(2\pi)^{-n/2}\mathcal{F}$, and its group analogue |
| $\tau_y$ | The translation $(\tau_yf)(x)=f(x+y)$, chosen so that the transform intertwines it with $\mu_y$ |
| $\mu_y$ | Multiplication by the character $\gamma_y$ |
| $m$ | A unimodular function on the dual, the gauge between two transforms |
| $K$ | A kernel on $X\times X$, and $K_x=K(\cdot,x)$ |
| $\widehat K$ | The transform of a kernel in both variables |
| $\psi$ | A function whose rank-one kernel is used as an example |
| $\Lambda$ | A bounded integrable test function used to prove positivity of $\widehat K$ |
| $X$ | The set on which a kernel is defined |
| $G$ | A locally compact abelian group, written additively |
| $\widehat G$ | The dual group of characters |
| $L^\infty$ | The bounded measurable functions, acting on $L^2$ by multiplication |
| $C_c^\infty$ | The smooth functions of compact support |
| $GL(n,\mathbb{R})$ | The invertible real $n\times n$ matrices, used for a change of frequency coordinates |
| $N$ | The number of points in a finite family, in the definition of a positive-definite kernel |
| $\mathbb{Z}$ | The integers, the dual of the circle group |
| $\gamma$ | A character, an element of $\widehat G$; $\gamma_\zeta(x)=e^{i\zeta\cdot x}$ for $G=\mathbb{R}^n$ |
| $dx$ | Haar measure on $G$ |
| $d\gamma$ | The Plancherel measure on $\widehat G$ |
| $\varpi$ | The Plancherel density, $d\gamma=\varpi\,d\lambda$, where $d\lambda$ is the measure of a chosen identification of $\widehat G$ |
| $T_K$ | The operator with kernel $K$ |
| $\mathbb{T}$ | The circle group, the values of a character |
| $\mathcal{F}^{-1}$ | The inverse transform $(2\pi)^{-n}\int e^{i\zeta\cdot x}g(\zeta)\,d\zeta$ |

## Further Reading

- *The Inverse Fourier Transform of a Symbol*, for the scalar Plancherel identity with its constant, which is the engine of every proof in §*The Isometry and the Unitary* and in §*Operator-Valued Functions*.
- *The Fourier Transform and the Symbol of a Differential Operator*, for the transform of a constant-coefficient operator, which is the case in which the value space is a finite-dimensional algebra rather than a Hilbert space.
- *The Fourier Transform on a Gelfand Triple*, for the placement of the transform in a triple of test spaces, which this article does not attempt.
- *The Fourier Operator*, for the general inversion formula and the two-sided reading of the transform, which is the scalar ancestor of §*Inversion on a Locally Compact Abelian Group*.
- *Convolution on a Group*, for the convolution of functions on a group, used once here in the operator-valued convolution theorem.
- *Locally Compact Groups and Haar Measure*, for the existence and uniqueness of Haar measure, which the Plancherel measure presupposes.
- *Pontryagin Duality*, for the dual group and the identification of $\widehat G$ with a model space, which is what supplies the density.
- *Reproducing Kernel Hilbert Spaces*, for positive-definite kernels, the Kolmogorov decomposition, and the reproducing property used in §*Kernels and Their Transforms*.
- *Unitary Representations and the Plancherel Theorem*, for the non-abelian case, where the dual is not a group and nothing here extends without new hypotheses.
- Walter Rudin, *Real and Complex Analysis* (3rd ed., McGraw-Hill, 1987), for the Plancherel theorem on $\mathbb{R}^n$ in the normalisation used throughout the corpus.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (2nd ed., CRC Press, 2015), for the Plancherel theorem on a locally compact abelian group, for the maximal abelian property of $L^\infty$, and for the uniqueness statement quoted in §*The Uniqueness Claim*.
- Barry Simon, *Trace Ideals and Their Applications* (2nd ed., American Mathematical Society, 2005), for the Hilbert–Schmidt class, for the trace of a positive operator computed in an orthonormal basis, and for the trace of an operator with continuous kernel.
- Masamichi Takesaki, *Theory of Operator Algebras I* (Springer, 1979), for the commutant of a multiplication algebra and the von Neumann algebra generated by a group of multiplications.
