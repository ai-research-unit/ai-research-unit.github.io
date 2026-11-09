# __The Fourier Transform on a Gelfand Triple__

## Introduction

A frequency is not an eigenvalue. On the line the functions that diagonalise the derivative are the exponentials $e^{i\zeta x}$, and not one of them lies in $L^2(\mathbb{R})$; the operator $i\partial$ has spectrum $\mathbb{R}$ and no eigenvector at all. The theory of this article supplies the objects that are missing. A test space $\Phi$ is chosen small enough that the exponentials act on it continuously, and its dual $\Phi'$ is large enough to contain them, and the two are tied to the Hilbert space by a chain

$$
\Phi\subset H\subset\Phi'
$$

of continuous injections with dense images. Such a chain is a **Gelfand triple**, and the article proves the three theorems that make it work for the transform of a constant-coefficient operator with values in a finite-dimensional real algebra: the transform is a topological isomorphism of the test space onto itself, its transpose is a topological isomorphism of the dual onto itself, and at every zero of the symbol the generalized eigenvectors form an explicit family in the dual, of dimension $d-r(\zeta)$.

**What is proved here.** That the transform is a homeomorphism of $\mathcal{S}(\mathbb{R}^n;A_{\mathbb{C}})$ onto itself and, by transposition, of $\mathcal{S}'$ (§*The Schwartz Triple*). That at a frequency the distributions $e^{i\zeta\cdot x}a$ are exactly the generalized eigenvectors of the translation group, annihilated by $P(D)$ exactly when $a$ is annihilated by $\sigma_P(\zeta)$, of dimension $d-r(\zeta)$ on the zero set (§*Generalized Eigenvectors at a Frequency*). That no nonzero element of $L^2$ is one of them, which is why the third space is needed (§*Why None of Them Lies in the Hilbert Space*). And that the Paley–Wiener triple fails the density axiom although its dual contains the eigenvectors (§*The Banach Triple and Its Defect*).

**What is quoted.** The nuclearity of $\mathcal{S}$ is *Nuclear Spaces*, and the reflexivity and the Montel property are *Locally Convex Spaces*; the inversion formula and the reflection identity, in the normalisation used here, are *Fourier Analysis on Euclidean Spaces* after the substitution described in §*The Transform Is an Isomorphism of the Test Space*. Three statements are quoted with their hypotheses and not proved: the Minlos theorem, which turns a continuous positive-definite function on a nuclear space into a measure on the dual; the nuclear spectral theorem of Gelfand and Maurin, which turns a self-adjoint operator acting on a nuclear triple into a family of generalized eigenvectors; and the Paley–Wiener characterisation of $PW_K$ by entire functions of exponential type. The last two are stated only to explain what is missing, and neither is used in a proof.

**The trap, and it has one word.** The word is *eigenvector*. In a Hilbert space an eigenvector is a vector, and the equation $Tu=\lambda u$ is an equation in $H$. Here the object that satisfies $P(D)u=\sigma_P(\zeta)u$ is an element of $\Phi'$ and not of $H$, and the equation holds in $\Phi'$, read through the transpose $P^{t}(D)$ acting on the test space. A sentence that says "$u\in L^2$ is an eigenvector at the frequency $\zeta$" is false for every nonzero $u$ (§*Why None of Them Lies in the Hilbert Space*), and a sentence that says "$u\in\Phi'$ is an eigenvector at the frequency $\zeta$" is a definition and not a theorem. **Every statement below names the space in which its equation holds.**

**Boundaries.** The symbol, its zero set $Z(P)$, and the dimensions of the kernel and the cokernel of $L_{\sigma_P(\zeta)}$ are *The Fourier Transform and the Symbol of a Differential Operator*; only its theorem on the three dimensions is used here. The growth of the inverse transform and its poles are *The Inverse Fourier Transform of a Symbol*, and the vector- and operator-valued Hilbert spaces, with the Plancherel theorem on a group, are *The Fourier Transform on Vector-Valued and Operator-Valued Function Spaces*. The distributions and their calculus are *Distributions and Fundamental Solutions*, the topology of the Schwartz space is *Nuclear Spaces*, and the duality is *Duality Theory*. The biquaternion case is where the multiplicities become concrete, and the numbers are quoted from *Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set*. **No spectral theorem for the general algebra is proved or assumed**, and §*What the Triple Does Not Give* says why the one that exists does not apply.

**What the word Gelfand adds.** The construction was made for the eigenfunction expansion of a self-adjoint operator, and this article does not prove that expansion. It proves the part that survives without self-adjointness: the test space, the dual, the isomorphism of the transform, and the identification of the generalized eigenvectors. **The expansion is a separate theorem with separate hypotheses, and it is not available for a symbol with values in an algebra.**

## The Rigged Triple

### The Three Spaces and the Pairing

**Definition (Gelfand triple).** Let $H$ be a separable complex Hilbert space, identified with its dual by the Riesz map, and let $\Phi$ be a locally convex space with a continuous linear injection $\Phi\to H$ whose image is dense. Write $\Phi'$ for the strong dual of $\Phi$, and let $H\to\Phi'$ be the transpose of the injection. The chain $\Phi\subset H\subset\Phi'$ is a **Gelfand triple**, or **rigged Hilbert space**, when both injections are continuous with dense image. The pairing of $\Phi'$ with $\Phi$ is written $\langle u,\varphi\rangle$; it is $A_{\mathbb{C}}$-valued, and when $A=\mathbb{C}$ it extends the inner product of $H$, in the sense that $\langle f,\varphi\rangle=(f,\varphi)_H$ for $f\in H$ and $\varphi\in\Phi$.

**Remark (the pairing against the inner product).** For $A=\mathbb{C}$ the pairing of $H$ with $\Phi$ is the inner product, since $H\to\Phi'$ is the transpose of $\iota:\Phi\to H$ and $\langle\iota^{*}f,\varphi\rangle=(f,\iota\varphi)_H$; for a general $A$ the pairing is $A_{\mathbb{C}}$-valued and a scalar inner product is recovered from it by applying a state, the trace of the regular representation being the natural one. **The algebra-valuedness of the pairing is the one place where the general case is not the scalar case with a vector attached.**

**Remark (the three inclusions, and which one is a theorem).** The inclusion $\Phi\subset H$ is a hypothesis, checked once for each example; $H\subset\Phi'$ is the transpose of it and is therefore automatic, as is its continuity. **What is not automatic is that the second inclusion is dense**, and that is the single hypothesis this theory has to verify; §*Density as Injectivity* turns it into a statement about injectivity, and §*The Banach Triple and Its Defect* exhibits a triple where it fails.

### Density as Injectivity

**Proposition (density of $\Phi$ is injectivity of the transpose).** The image of $\Phi$ in $H$ is dense if and only if the map $H\to\Phi'$ is injective.

*Proof.* Suppose first that $\Phi$ is dense and that $f\in H$ maps to zero. Then $(f,\varphi)_H=0$ for every $\varphi\in\Phi$, and density extends the identity to every element of $H$, so $f=0$. Suppose next that $\Phi$ is not dense. Its closure is then a proper closed subspace of $H$, its orthogonal complement contains a nonzero $f$, and that $f$ is orthogonal to every $\varphi\in\Phi$, hence maps to zero.

**Remark (why this proposition is the hinge).** It converts a topological statement into an algebraic one, and the algebraic one is easier to disprove: one nonzero element of $H$ orthogonal to the whole of $\Phi$ destroys the triple. **The Banach triple of §*The Banach Triple and Its Defect* is destroyed in exactly this way**, visibly, by an explicit function.

**Proposition (the scale is strict, in general).** The three spaces are distinct in the examples of this article: $\Phi'$ contains elements outside $H$, and $H$ contains elements outside $\Phi$.

*Proof.* The first is a generalized eigenvector in $\Phi'\setminus H$, exhibited in §*Why None of Them Lies in the Hilbert Space*. The second holds because $\mathcal{S}\subset L^\infty$ and $L^2\not\subset L^\infty$.

### Why the Hilbert Space Alone Is Not Enough

**Proposition (the derivative has no eigenvalue in $L^2$).** Let $\mathcal{F}$ be the transform $\mathcal{F}f(\zeta)=\int e^{-i\zeta\cdot x}f(x)\,dx$, extended to $L^2(\mathbb{R}^n;\mathbb{C})$ by continuity. Then $\mathcal{F}(i\partial_j f)(\zeta)=-\zeta_j\mathcal{F}f(\zeta)$ for $f$ in the Schwartz space, the operator $i\partial_j$ is unitarily equivalent to multiplication by $-\zeta_j$, and it has no eigenvalues; its spectrum is the whole real line, every point of which belongs to the continuous spectrum.

*Proof.* The identity is the differentiation rule $\mathcal{F}(\partial_jf)(\zeta)=i\zeta_j\mathcal{F}f(\zeta)$ multiplied by $i$. The normalised transform $\mathcal{U}=(2\pi)^{-n/2}\mathcal{F}$ is unitary, so $\mathcal{U}i\partial_j\mathcal{U}^{*}$ is multiplication by $-\zeta_j$. If $g\in L^2$ satisfied $\zeta_jg=\lambda g$ then $(\zeta_j-\lambda)g=0$ almost everywhere, and since $\zeta_j-\lambda$ vanishes on a set of measure zero the function $g$ is zero almost everywhere. The spectrum of multiplication by $\zeta_j$ is the essential range of $\zeta_j$, which is $\mathbb{R}$, and the absence of eigenvalues makes the spectrum purely continuous.

**Corollary (the missing objects).** The exponentials $e^{i\zeta\cdot x}$ satisfy $i\partial_je^{i\zeta\cdot x}=-\zeta_je^{i\zeta\cdot x}$ in the sense of distributions and are not in $L^2$; and every eigenvector of $i\partial_j$ in $L^2$ is zero.

*Proof.* The first statement is a computation of derivatives of a smooth function. The second is the proposition, and the assertion $e^{i\zeta\cdot x}\notin L^2$ is the statement that a function of constant modulus one does not lie in $L^2(\mathbb{R}^n)$.

**Remark (what the third space is for).** The corollary says that the diagonalisation of $i\partial$ exists but that its eigenvectors lie outside the Hilbert space. **The third space is where they lie**, and §*Generalized Eigenvectors at a Frequency* identifies them there. The identification is not a formality: it produces, for each frequency, a concrete family of distributions whose dimension is computed from the symbol.

## The Schwartz Triple

### The Test Space and Its Topology

**Definition (the algebra-valued Schwartz space).** Let $\mathcal{S}=\mathcal{S}(\mathbb{R}^n;A_{\mathbb{C}})$ be the space of smooth functions $f:\mathbb{R}^n\to A_{\mathbb{C}}$ such that $\sup_x\lVert x^\beta\partial^\alpha f(x)\rVert$ is finite for every pair of multi-indices, with the seminorms

$$
\lVert f\rVert_{\alpha,\beta}=\sup_{x\in\mathbb{R}^n}\ \lVert x^\beta\partial^\alpha f(x)\rVert ,
$$

where $\lVert\cdot\rVert$ is any norm on the finite-dimensional complex vector space $A_{\mathbb{C}}$. The space is a Fréchet space, nuclear, reflexive and Montel; the first two properties are *Nuclear Spaces* and the second two are *Locally Convex Spaces*. The functions are $A_{\mathbb{C}}$-valued, which is to say $d$ complex-valued functions in a chosen basis, and every identity below is proved componentwise and reassembled.

**Remark (the topology uses the vector space only).** The topology of $\mathcal{S}$ uses only the vector space $A_{\mathbb{C}}$, since all norms on a finite-dimensional space are equivalent; the algebra structure enters through $P(D)$, whose coefficients multiply on the left, and through nothing else. **One triple therefore serves every algebra of the family**, with a different operator and a different zero set but the same test space and the same transform.

### The Transform Is an Isomorphism of the Test Space

**Proposition (the two exchange identities).** For $f\in\mathcal{S}$ and multi-indices $\alpha,\beta$,

$$
\mathcal{F}(\partial^\alpha f)(\zeta)=(i\zeta)^\alpha\,\mathcal{F}f(\zeta),\qquad \partial_\zeta^\alpha\mathcal{F}f(\zeta)=\mathcal{F}\big((-ix)^\alpha f\big)(\zeta).
$$

*Proof.* The first is differentiation under the integral sign, justified by the decay of $f$ and of its derivatives; the second is the same computation with the derivative taken in the frequency variable, where the factor $-ix$ appears because the exponent is $-i\zeta\cdot x$. Both are identities of $A_{\mathbb{C}}$-valued functions, the factors being scalar.

**Theorem (the transform is a homeomorphism of the test space).** The transform $\mathcal{F}$ maps $\mathcal{S}$ continuously into itself, and it is a topological isomorphism onto $\mathcal{S}$, with inverse $g\mapsto(2\pi)^{-n}\int e^{i\zeta\cdot x}g(\zeta)\,d\zeta$.

*Proof.* Let $\alpha$ be a multi-index in the frequency and $\beta$ one in the position variable. By the two identities, $\zeta^\beta\partial^\alpha_\zeta\mathcal{F}f$ is a constant of modulus one times $\mathcal{F}\big(\partial^\beta(x^\alpha f)\big)$, and $\lVert\mathcal{F}g\rVert_\infty\le\lVert g\rVert_1$. The $L^1$ norm is bounded by a finite sum of the seminorms $\lVert g\rVert_{0,\gamma}$ with $\lvert\gamma\rvert\le n+1$, by the elementary estimate that $(1+\lvert x\rvert^2)^{-(n+1)/2}$ is integrable. Leibniz expands $\partial^\beta(x^\alpha f)$ as a finite sum of terms $x^{\alpha'}\partial^{\beta'}f$ with $\alpha'\le\alpha$ and $\beta'\le\beta$, so that

$$
\lVert\mathcal{F}f\rVert_{\alpha,\beta}\ \le\ C_{\alpha,\beta}\sum_{\alpha'\le\alpha}\ \sum_{\lvert\gamma\rvert\le n+1}\ \lVert f\rVert_{\alpha'+\gamma,\beta},
$$

which is a finite sum of seminorms of $f$; the transform is therefore continuous. The inverse has the same form with $+i$ in the exponent and the factor $(2\pi)^{-n}$, hence is continuous as well; and it is a genuine inverse because the inversion formula on $\mathcal{S}$ holds, quoted from *Fourier Analysis on Euclidean Spaces* after the substitution of the next remark.

**Remark (the two normalisations, and how the constant moves).** *Fourier Analysis on Euclidean Spaces* writes the transform with the exponent $-2\pi i\zeta\cdot x$ and has no constant in the inversion. The substitution $\zeta\mapsto2\pi\zeta$ converts its statements into the ones used here, and the factor $(2\pi)^n$ is exactly the Jacobian of that substitution. **The constant is not a convention of the theory but the price of counting the frequency in radians**, which is the counting forced by the symbol $\sigma_P(\zeta)=\sum a_\alpha(i\zeta)^\alpha$ of *The Fourier Transform and the Symbol of a Differential Operator*.

### The Transpose on the Tempered Distributions

**Definition (the pairing and the dual).** For $T\in L^1_{\mathrm{loc}}(\mathbb{R}^n;A_{\mathbb{C}})$ and $\varphi\in\mathcal{S}$ put $\langle T,\varphi\rangle=\int\varphi(x)T(x)\,dx$, an element of $A_{\mathbb{C}}$; the integral is bilinear over $\mathbb{C}$ in each slot and the values multiply in the algebra, **the test function standing on the left inside the integral**. The space $\mathcal{S}'$ of continuous functionals for this pairing, with the strong topology, is the space of **tempered distributions**, and the pairing extends to $\mathcal{S}'\times\mathcal{S}$ by continuity.

**Remark (why the test function stands on the left).** The order is forced by the algebra. With this pairing $\langle au,\varphi\rangle=\int\varphi au=\langle u,\varphi a\rangle$, so the transpose of left multiplication by $a$ is right multiplication by $a$. **The non-commutativity of $A$ appears in the definition of the transpose, and nowhere else in this article.**

**Theorem (the transform is self-transpose).** For $T\in\mathcal{S}'$ and $\varphi\in\mathcal{S}$,

$$
\langle\mathcal{F}T,\varphi\rangle=\langle T,\mathcal{F}\varphi\rangle ,
$$

so that $\mathcal{F}$ extends to a topological isomorphism of $\mathcal{S}'$ onto itself, whose inverse is $(2\pi)^{-n}\mathcal{F}$ followed by the reflection $x\mapsto-x$; in particular $\mathcal{F}^{2}T=(2\pi)^nT(-\cdot)$ in $\mathcal{S}'$.

*Proof.* For $T\in\mathcal{S}$ the identity is Fubini's theorem applied to the double integral of $e^{-i\zeta\cdot x}T(x)\varphi(\zeta)$, which is absolutely convergent by the decay of both factors. For general $T$ both sides are continuous in the strong topology of $\mathcal{S}'$, and $\mathcal{S}$ is dense in $\mathcal{S}'$, so the identity extends. The transpose of a topological isomorphism between reflexive spaces is a topological isomorphism of the strong duals, and $\mathcal{S}$ is reflexive and Montel, so $\mathcal{F}$ is one; the inverse formula is the transpose of the inversion formula of §*The Transform Is an Isomorphism of the Test Space*.

**Remark (what self-transposition buys).** The identity $\langle\mathcal{F}T,\varphi\rangle=\langle T,\mathcal{F}\varphi\rangle$ lets the same letter serve for the transform on functions and on distributions, and it lets a generalized eigenvector be written down without a theory of eigenfunction expansions: **the equation in $\mathcal{S}'$ is verified against test functions, and the verification uses only the identity on $\mathcal{S}$.**

## Generalized Eigenvectors at a Frequency

### The Eigenvalue Equation in the Dual

**Definition (generalized eigenvector of the operator).** Let $\zeta\in\mathbb{R}^n$ and $u\in\mathcal{S}'$. Then $u$ is a **generalized eigenvector of $P(D)$ with eigenvalue $\sigma_P(\zeta)$** when $P(D)u=\sigma_P(\zeta)u$ in $\mathcal{S}'$, that is, when

$$
\langle u,P^{t}(D)\varphi\rangle=\sigma_P(\zeta)\,\langle u,\varphi\rangle\qquad\text{for every }\varphi\in\mathcal{S},
$$

where $P^{t}(D)\varphi=\sum_{\lvert\alpha\rvert\le m}(-1)^{\lvert\alpha\rvert}(\partial^\alpha\varphi)a_\alpha$ is the transpose of $P(D)$, **with the coefficients on the right**, and the right side is the left multiplication of $\langle u,\varphi\rangle$ by the constant $\sigma_P(\zeta)$. The transpose is computed once: $\langle P(D)u,\varphi\rangle=\sum_\alpha\int\varphi a_\alpha\partial^\alpha u=\sum_\alpha(-1)^{\lvert\alpha\rvert}\int(\partial^\alpha\varphi)a_\alpha u=\langle u,P^{t}(D)\varphi\rangle$, the middle step being integration by parts and the constant $a_\alpha$ passing through the derivative.

**Definition (generalized eigenvector at a frequency).** With the same notation, $u$ is a **generalized eigenvector at the frequency $\zeta$** when $(\partial_j-i\zeta_j)u=0$ in $\mathcal{S}'$ for $j=1,\dots,n$. The second notion is stronger, and the next proposition says how much.

**Proposition (the frequency implies the eigenvalue).** If $u$ is a generalized eigenvector at the frequency $\zeta$ then it is a generalized eigenvector of $P(D)$ with eigenvalue $\sigma_P(\zeta)$.

*Proof.* From $(\partial_j-i\zeta_j)u=0$ and the linearity of the derivative on $\mathcal{S}'$ one gets $\partial^\alpha u=(i\zeta)^\alpha u$ by induction on $\lvert\alpha\rvert$. Multiplying by $a_\alpha$ on the left and summing, $P(D)u=\sum a_\alpha(i\zeta)^\alpha u=\sigma_P(\zeta)u$, the coefficients being constants and therefore passing through the differentiation.

**Remark (the converse fails, and the failure is not a technicality).** Take $P=\partial_1\partial_2$ on $\mathbb{R}^2$ and $\zeta=0$, where $\sigma_P(0)=0$. Every distribution of the form $f(x_1)$, with $f\in\mathcal{S}'(\mathbb{R})$, is annihilated by $P$ and is therefore an eigenvector with eigenvalue $0$, while only the constant $f$ is a generalized eigenvector at the frequency $0$. **The frequency notion is the one the transform diagonalises**, and it is the only one for which the frequency is a well-defined object.

### Three Equivalent Descriptions

**Theorem (the family at a frequency).** Let $\zeta\in\mathbb{R}^n$ and $u\in\mathcal{S}'$. The following three conditions are equivalent: (i) $(\partial_j-i\zeta_j)u=0$ for every $j$; (ii) $\tau_yu=e^{i\zeta\cdot y}u$ for every $y\in\mathbb{R}^n$, where $(\tau_yu)(x)=u(x+y)$; (iii) $u=u_{\zeta,a}$ for some $a\in A_{\mathbb{C}}$, where

$$
u_{\zeta,a}(x)=e^{i\zeta\cdot x}a .
$$

*Proof.* From (i) to (iii): put $v=e^{-i\zeta\cdot x}u$, a distribution because multiplication by the smooth function $e^{-i\zeta\cdot x}$ preserves $\mathcal{S}'$; then $\partial_jv=0$ for every $j$, since $\partial_j(e^{-i\zeta\cdot x}u)=e^{-i\zeta\cdot x}(\partial_j-i\zeta_j)u$. A distribution annihilated by every $\partial_j$ is a constant: for $\rho\in C_c^\infty(\mathbb{R}^n)$ with $\int\rho=1$, the convolution $v*\rho$ is constant because $\partial_j(v*\rho)=(\partial_jv)*\rho=0$, and $v*\rho\to v$ as $\rho$ shrinks to a delta. From (iii) to (ii): $u_{\zeta,a}(x+y)=e^{i\zeta\cdot y}u_{\zeta,a}(x)$. From (ii) to (iii): the same function $v$ is invariant under every translation, hence constant by the same mollifier argument, so $u=e^{i\zeta\cdot x}a$ with $a=v$.

**Remark (what the three descriptions say).** Condition (ii) says that $u$ is a generalized eigenvector of the whole translation group with the character $\gamma_\zeta(y)=e^{i\zeta\cdot y}$, the same object as the multiplier $\mu_y$ of *The Fourier Transform on Vector-Valued and Operator-Valued Function Spaces*. **The family is the trace of that character inside $\mathcal{S}'$.**

### The Family at a Zero of the Symbol

**Theorem (the eigenvectors annihilated by the operator).** Let $\zeta\in\mathbb{R}^n$ and $a\in A_{\mathbb{C}}$. Then $u_{\zeta,a}\in\mathcal{S}'$, and $P(D)u_{\zeta,a}=e^{i\zeta\cdot x}\sigma_P(\zeta)a$; consequently $P(D)u_{\zeta,a}=0$ if and only if $a\in\operatorname{Ann}_L(\sigma_P(\zeta))=\ker L_{\sigma_P(\zeta)}$. The map $a\mapsto u_{\zeta,a}$ is injective, so at a frequency $\zeta\in Z(P)$ the generalized eigenvectors at $\zeta$ that are annihilated by $P(D)$ form a family of dimension $d-r(\zeta)$, and at a frequency outside $Z(P)$ the only such element is zero.

*Proof.* Multiplication by $e^{i\zeta\cdot x}$ is a continuous endomorphism of $\mathcal{S}$, because every derivative of the exponential has polynomial growth and the seminorms of $\mathcal{S}$ absorb a polynomial factor; hence $\varphi\mapsto\int e^{i\zeta\cdot x}a\,\varphi(x)\,dx$ is a continuous functional, that is, an element of $\mathcal{S}'$. The computation $\partial_ju_{\zeta,a}=i\zeta_ju_{\zeta,a}$ is integration by parts against test functions, $\int(\partial_j\varphi+i\zeta_j\varphi)e^{i\zeta\cdot x}a\,dx=0$ for $\varphi$ of compact support, and it gives $P(D)u_{\zeta,a}=e^{i\zeta\cdot x}\sum_\alpha a_\alpha(i\zeta)^\alpha a=e^{i\zeta\cdot x}\sigma_P(\zeta)a$. Injectivity: if $u_{\zeta,a}=0$ then $(\int e^{i\zeta\cdot x}\varphi(x)\,dx)a=0$ for every $\varphi$, the integral is a nonzero complex number for a suitable $\varphi$, and $a=0$. The dimension is the theorem on the three dimensions of *The Fourier Transform and the Symbol of a Differential Operator*.

**Remark (the transform of the eigenvector is a delta).** Applying the self-transposition to $\psi\in\mathcal{S}$,

$$
\langle\mathcal{F}u_{\zeta,a},\psi\rangle=\langle u_{\zeta,a},\mathcal{F}\psi\rangle=\mathcal{F}(\mathcal{F}\psi)(-\zeta)\,a=(2\pi)^n\psi(\zeta)\,a,
$$

so that $\mathcal{F}u_{\zeta,a}=(2\pi)^n\delta_\zeta\,a$: **the generalized eigenvector at the frequency $\zeta$ is the object whose transform is the delta at $\zeta$**, multiplied on the right by $a$. Equivalently, $\langle u_{\zeta,a},\varphi\rangle=\mathcal{F}\varphi(-\zeta)\,a$, so the eigenvector acts on a test function by evaluating the transform at $-\zeta$. Either way, the eigenvector is concentrated at one frequency and is not localised at all in position.

**Remark (the numbers in the biquaternion case).** At a null element of the biquaternion algebra away from the origin the rank of left multiplication is $4$ of $8$, so the family has dimension $4$; at the origin the symbol vanishes and the family has dimension $8$, which is the whole algebra. Both numbers are proved in *Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set*, and they are quoted here as the concrete instance of the formula $d-r(\zeta)$.

### Why None of Them Lies in the Hilbert Space

**Lemma (a distribution annihilated by one derivative is independent of that variable).** Let $v\in\mathcal{S}'(\mathbb{R}^n)$ and suppose $\partial_jv=0$. Then $v(\varphi)$ depends only on $\int\varphi(x)\,dx_j$: for every $\varphi$ one has $v(\varphi)=v(\varphi_0)$, where $\varphi_0(x)=\rho(x_j)\int\varphi(x',t)\,dt$ for a fixed $\rho\in C_c^\infty(\mathbb{R})$ with $\int\rho=1$.

*Proof.* For fixed $x'$ the function $t\mapsto\varphi(x',t)-\int\varphi(x',s)\,ds\,\rho(t)$ has integral zero, so it is the derivative of a compactly supported smooth function $\chi(\cdot,x')$; then $\varphi-\varphi_0=\partial_j\chi$, and $v(\varphi-\varphi_0)=-v(\partial_j\chi)=(\partial_jv)(\chi)=0$.

**Lemma (no nonzero element of $L^2$ is an eigenvector at a frequency).** Let $\zeta\in\mathbb{R}^n$ and let $u\in L^2(\mathbb{R}^n;A_{\mathbb{C}})$ satisfy $(\partial_j-i\zeta_j)u=0$ in $\mathcal{S}'$ for every $j$. Then $u=0$.

*Proof.* Put $v=e^{-i\zeta\cdot x}u$, which lies in $L^2$ and satisfies $\partial_jv=0$ for every $j$. By the lemma, iterated over the $n$ variables, $v$ is a constant $c\in A_{\mathbb{C}}$; then $\lVert u\rVert_2^2=\lVert c\rVert^2\int_{\mathbb{R}^n}1$, which is infinite unless $c=0$.

**Corollary (the third space is not optional).** For $a\neq0$ and every $\zeta$, the distribution $u_{\zeta,a}$ lies in $\mathcal{S}'\setminus L^2$. Hence the generalized eigenvectors of §*The Family at a Zero of the Symbol* are available in the triple and in no smaller space of the chain.

*Proof.* The distribution is an eigenvector at $\zeta$ by the theorem, and no nonzero element of $L^2$ is one by the lemma.

**Remark (what the lemma does not say).** It says nothing about the weaker equation $P(D)u=\sigma_P(\zeta)u$, whose solutions can be far more numerous, as the example $P=\partial_1\partial_2$ shows. **The lemma is a statement about the frequency, and the frequency is the notion that carries the transform.**

## The Banach Triple and Its Defect

### The Paley–Wiener Space

**Definition (the space of a compact frequency set).** Let $K\subset\mathbb{R}^n$ be compact and let $\lvert K\rvert$ be its Lebesgue measure. Put

$$
PW_K=\{f\in L^2(\mathbb{R}^n;A_{\mathbb{C}}):\operatorname{supp}\mathcal{F}f\subset K\},
$$

the **Paley–Wiener space** of $K$: the functions of $L^2$ whose transform vanishes outside $K$.

**Proposition ($PW_K$ is a Banach space, and point evaluation is continuous).** $PW_K$ is a closed subspace of $L^2$, hence a Banach space for the $L^2$ norm, and for every $f\in PW_K$ and every $x$,

$$
\lvert f(x)\rvert\le(2\pi)^{-n/2}\lvert K\rvert^{1/2}\lVert f\rVert_2 .
$$

*Proof.* The set of $g\in L^2$ with $\operatorname{supp}g\subset K$ is closed, because a limit in $L^2$ of such functions has a subsequence converging almost everywhere; and $\mathcal{F}$ is a homeomorphism of $L^2$ onto itself by Plancherel, so the preimage of a closed set is closed. For the bound, $\mathcal{F}f$ lies in $L^1$ because it lies in $L^2$ and is supported in a set of finite measure, so the inversion formula gives $f(x)=(2\pi)^{-n}\int_K\mathcal{F}f(\zeta)e^{ix\cdot\zeta}\,d\zeta$, and Cauchy–Schwarz in $L^2(K)$ gives $\lvert f(x)\rvert\le(2\pi)^{-n}\lvert K\rvert^{1/2}\lVert\mathcal{F}f\rVert_2=(2\pi)^{-n/2}\lvert K\rvert^{1/2}\lVert f\rVert_2$ by Plancherel.

**Remark (Paley–Wiener, quoted).** $PW_K$ is exactly the space of entire $A_{\mathbb{C}}$-valued functions of exponential type whose type is bounded by $K$ and whose restriction to $\mathbb{R}^n$ lies in $L^2$, and the correspondence is an isomorphism of Banach spaces. This is quoted from the classical theorem of Paley and Wiener and is used only to say what the objects are: **the members of $PW_K$ are analytic, and the triple is a triple of analytic objects.**

### The Injection Is Not Dense

**Proposition ($PW_K$ is not dense in $L^2$).** $PW_K$ is a proper closed subspace of $L^2$, so its injection into $L^2$ is not dense, and the chain $PW_K\subset L^2\subset PW_K'$ fails the density axiom of a Gelfand triple.

*Proof.* Choose $g\in L^2$ with $g\neq0$ and $\operatorname{supp}g$ disjoint from $K$, and put $f=\mathcal{F}^{-1}g$, which is nonzero. For $h\in PW_K$, Plancherel gives $(f,h)_2=(2\pi)^{-n}(\mathcal{F}f,\mathcal{F}h)_2=(2\pi)^{-n}(g,\mathcal{F}h)_2=0$, because the two transforms have disjoint supports. Hence $f$ is a nonzero element of the orthogonal complement, and $PW_K$ is not dense.

**Corollary (the failure, in the form of §*Density as Injectivity*).** The map $L^2\to PW_K'$ is not injective. Two elements of $H$ that differ by an element of $PW_K^{\perp}$ define the same functional on $PW_K$, and the annihilator $PW_K^{\perp}$ is the nonzero closed subspace of functions whose transforms vanish almost everywhere on $K$.

*Proof.* The corollary is the proposition combined with §*Density as Injectivity*, and the description of the annihilator is the computation in the proof of the proposition read backwards.

**Remark (the failure is not repairable inside the Banach category).** Enlarging $PW_K$ leaves the category, as the union over $K$ shows; replacing $PW_K$ by a dense subspace produces a space that is not complete, and a triple needs completeness for its dual to be a space of distributions. **The Banach triple is a triple with a proved defect, and the defect is exactly the failure of the axiom that a rigged triple needs.**

### What the Banach Dual Still Contains

**Proposition (the generalized eigenvectors lie in $PW_K'$).** Let $\zeta\in\mathbb{R}^n$, $a\in A_{\mathbb{C}}$, and $\psi\in PW_K$, and put $\varphi=\mathcal{F}^{-1}\psi$. Then

$$
\langle u_{\zeta,a},\psi\rangle=(2\pi)^n\varphi(\zeta)\,a,\qquad\lvert\langle u_{\zeta,a},\psi\rangle\rvert\le\lvert K\rvert^{1/2}\lVert a\rVert\,\lVert\psi\rVert_2 ,
$$

so the restriction of $u_{\zeta,a}$ to $PW_K$ is continuous, with norm at most $\lvert K\rvert^{1/2}\lVert a\rVert$.

*Proof.* For $\psi\in PW_K\cap\mathcal{S}$ the first identity is the computation $\langle u,\psi\rangle=\mathcal{F}\psi(-\zeta)a$ combined with $\mathcal{F}\psi=\mathcal{F}^2\varphi=(2\pi)^n\varphi(-\cdot)$, which gives $\mathcal{F}\psi(-\zeta)a=(2\pi)^n\varphi(\zeta)a$; the general case follows because $PW_K\cap\mathcal{S}$ is dense in $PW_K$, the inverse transforms of the smooth functions of compact support being dense in $PW_K$. The function $\varphi$ lies in $PW_K$ as well, since $\mathcal{F}\varphi=\psi$ is supported in $K$; the point-evaluation bound of §*The Paley–Wiener Space* applied to $\varphi$ gives $\lvert\varphi(\zeta)\rvert\le(2\pi)^{-n}\lvert K\rvert^{1/2}\lVert\psi\rVert_2$, and the estimate follows.

**Remark (what the Banach triple does and does not do).** It contains the generalized eigenvectors, and it computes their action. What it does not do is separate the elements of the Hilbert space, and that failure is the density axiom. **A triple can be good for the eigenvectors and bad for the space they act on, and the Paley–Wiener triple is the example.**

### The Union over Compact Sets

**Definition (the space of compactly supported transform).** Put $S_0=\bigcup_KPW_K$, the union over the compact subsets of $\mathbb{R}^n$, with the strict inductive limit topology of the increasing family $K_m=\{\lvert x\rvert\le m\}$.

**Proposition ($S_0$ is dense in $L^2$ and is not a Banach space).** $S_0$ is dense in $L^2$, so $L^2\to S_0'$ is injective and $(S_0,L^2,S_0')$ is a Gelfand triple; $S_0$ is a strict inductive limit of the Banach spaces $PW_{K_m}$ and is neither normable nor metrisable.

*Proof.* Density: $S_0$ contains the inverse transforms of the smooth functions of compact support, because such a transform lies in $L^2$ and is supported in the support of the function; those inverse transforms are dense in $L^2$ because the smooth functions of compact support are dense and $\mathcal{F}^{-1}$ is a surjective isometry. The strictness: $PW_{K_m}$ is a proper closed subspace of $PW_{K_{m+1}}$, and a strict inductive limit of such a sequence is not normable, by *Topological Vector Spaces, Distributions and Kernels*.

### No Infinite-Dimensional Banach Space Is Nuclear

**Theorem (the Banach category is closed to nuclearity).** An infinite-dimensional Banach space is not nuclear; hence every nuclear Gelfand triple has a test space that is not a Banach space, and the triple $PW_K\subset L^2\subset PW_K'$ is not nuclear.

*Proof.* In a nuclear space every bounded set is precompact, so the unit ball of a nuclear normed space is precompact, and a normed space with a precompact unit ball is finite-dimensional by Riesz's lemma; this is the argument of *Nuclear Spaces*. The space $PW_K$ is an infinite-dimensional Hilbert space, hence not nuclear, and it is the test space of its own triple. A subspace of a nuclear space is nuclear, so $S_0$ is not nuclear either: if it were, each $PW_{K_m}$ would be, and none is.

**Remark (the two axioms pull in opposite directions).** The density axiom wants a small test space, and the smaller it is the more elements the dual acquires. Nuclearity wants a space with summable approximation numbers, and no infinite-dimensional Banach space has them. **The Schwartz space satisfies both axioms, and it is the only space of this article that does**; that is the reason the theory of rigged triples is a theory of nuclear Fréchet spaces and not a theory of Banach spaces.

## The General Nuclear Case, Stated

**The Minlos theorem, quoted.** Let $\Phi$ be a nuclear Fréchet space and let $\Phi\to H$ be a continuous injection with dense image. Let $\chi:\Phi\to\mathbb{C}$ be continuous, positive definite, and normalised by $\chi(0)=1$. Then there is a Radon probability measure $\mu$ on the dual $\Phi'$, for the cylinder $\sigma$-algebra, such that

$$
\chi(\xi)=\int_{\Phi'}e^{i\langle x,\xi\rangle}\,d\mu(x)\qquad\text{for every }\xi\in\Phi ,
$$

where the pairing is that of $\Phi'$ with $\Phi$. This is Minlos's theorem, quoted from *Generalized Functions IV* of Gelfand and Vilenkin; nuclearity supplies the Hilbert–Schmidt condition that the proof requires, and the statement is not proved here.

**Proposition (why nuclearity and not merely completeness).** On an infinite-dimensional Hilbert space $H$ the function $\chi(\xi)=e^{-\lVert\xi\rVert^2/2}$ is continuous and positive definite, and it is not the transform of a Radon probability measure; the cylinder measure that would correspond to it is only finitely additive.

*Proof.* A Radon probability measure with that transform would be a Gaussian measure whose covariance operator is the identity, and the covariance operator of a Gaussian measure on $H$ is trace class; the identity of an infinite-dimensional Hilbert space is not trace class, since its trace is the dimension. The measure therefore does not exist, and the cylinder measure is not countably additive.

**Remark (the exact sense of the failure).** The proposition is not a defect of $\chi$, which is as regular as a function can be, but of the space. **Nuclearity replaces finite dimension in Bochner's theorem, and the triple records where the measure lives.**

**Remark (what the theorem is used for, and what it is not).** It produces a measure on the dual from a positive-definite function on the test space, which is the inverse problem of the transform; it produces no expansion of an arbitrary element of $H$ and no eigenvectors. **The two theorems are separate, and only the first is available for a general nuclear triple.**

## What the Triple Does Not Give

**The nuclear spectral theorem, quoted and not applicable.** Let $T$ be a self-adjoint operator on $H$ with $\Phi\subset D(T)$, $T\Phi\subset\Phi$, and $T$ continuous on $\Phi$, and let $\Phi$ be nuclear. Then for the spectral measure $E$ of $T$ there is, for $E$-almost every $\lambda$, a generalized eigenvector $\xi_\lambda\in\Phi'$ with $T\xi_\lambda=\lambda\xi_\lambda$, the family is complete in the sense that $\langle\xi_\lambda,\varphi\rangle=0$ for $E$-almost every $\lambda$ forces $\varphi=0$, and the spectral measure is recovered from the family. This is the theorem of Gelfand and Maurin, quoted from *Generalized Eigenfunction Expansions* of Maurin, with the hypotheses as stated.

**Remark (the hypotheses fail here, and each fails for a reason).** Two of them fail for the operator of this article. The operator $P(D)$ is not self-adjoint on $L^2(\mathbb{R}^n;A_{\mathbb{C}})$: self-adjointness needs an involution of $A$ and a Hilbert structure for which every left multiplication $L_a$ is self-adjoint, and no such structure is assumed; for $A=\mathbb{C}$ and real coefficients an odd-order $P$ is only skew-symmetric, the self-adjoint operator being $iP$, and for a general $A$ there is no involution under which that passage can be made. And the conclusion is an expansion, a statement about a measure on the spectrum; for an algebra-valued symbol the spectrum lies in $A_{\mathbb{C}}$, and no measure on it is constructed here. **The theorem is quoted to name what is missing, and it is not used.**

**What the triple does give.** The generalized eigenvectors at every frequency, an explicit formula for them, the dimension $d-r(\zeta)$ of the family at each zero of the symbol, and the emptiness of the family off the zero set. The transform as an isomorphism of the test space and of its dual, so that the eigenvector is the inverse transform of a delta. And the pairing that replaces the inner product, $\langle u_{\zeta,a},\varphi\rangle=\mathcal{F}\varphi(-\zeta)a$, which is the only sense in which a generalized eigenvector is tested.

**What it does not give.** It gives no orthogonality among the generalized eigenvectors. Two elements of $\Phi'$ cannot be paired, since the pairing is between $\Phi'$ and $\Phi$; the statement that two eigenvectors at distinct frequencies are orthogonal is not a statement of this theory, and the substitute, the identity $\langle u_{\zeta,a},\varphi\rangle=\mathcal{F}\varphi(-\zeta)a$, is a statement about one eigenvector at a time. It gives no multiplicity function beyond the pointwise dimension $d-r(\zeta)$, and no measure on the frequency set; a Plancherel formula for the algebra-valued transform needs a density on that set, and for the biquaternion algebra the natural candidate is a measure on the null cone, which is the programme of *The Inverse Biquaternion Fourier Transform: Poles, Types and Tails*. It gives no expansion, as §*The General Nuclear Case, Stated* says. **The triple is a vocabulary for eigenvectors, not a spectral theorem, and the distinction is the whole of §*Generalized Eigenvectors at a Frequency* read backwards.**

**The one exception, and its exact size.** For $A=\mathbb{C}$ and $P=i\partial_j$ the expansion does exist: it is Fourier inversion, an integral over the real line, and it is the theorem of *Fourier Analysis on Euclidean Spaces*. The expansion is an integral and not a sum, its index set is a continuum, and the coefficient of each generalized eigenvector is a transform. **The exceptional case is therefore not a counterexample to the warnings above but their model**: the triple is what makes the integral a statement about eigenvectors, and the integral itself is a separate theorem, proved once in the scalar case and not available in general.

## Summary

The triple is a chain of three spaces built so that a frequency can be an eigenvalue. The test space is small enough for the exponentials to act on it continuously, the dual is large enough to contain them, and the Hilbert space sits between the two with a pairing that agrees with its inner product. For the transform of a constant-coefficient operator over a finite-dimensional real algebra the chain works: the transform is a homeomorphism of the Schwartz space and of the tempered distributions; the generalized eigenvectors at a frequency are the distributions $e^{i\zeta\cdot x}a$, annihilated by $P(D)$ exactly when $a$ is annihilated by $\sigma_P(\zeta)$, of dimension $d-r(\zeta)$ on the zero set; and the transform of each is a delta at the frequency.

The Banach triple is the instructive failure. The Paley–Wiener space $PW_K$ is a closed subspace of $L^2$ and a genuine Banach space, it contains the generalized eigenvectors and computes their action, and it is not dense; the map from the Hilbert space to its dual is therefore not injective, and an annihilator appears. The union $S_0$ restores density and loses the Banach property, and no infinite-dimensional Banach space is nuclear, so no Banach triple satisfies both axioms. **The two axioms are independent, the Schwartz triple satisfies both, and that is why the general theory is stated for nuclear Fréchet spaces.** Minlos's theorem is quoted as the theorem that uses nuclearity, and Gelfand–Maurin as the one that is not available, with the hypotheses that fail here named.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | A finite-dimensional real associative algebra with unit |
| $A_{\mathbb{C}}$ | The complexification, where the symbol and the values live |
| $d$ | The dimension of $A$ over $\mathbb{R}$ |
| $P(D)$ | A constant-coefficient operator $\sum_{\lvert\alpha\rvert\le m}a_\alpha\partial^\alpha$ with $a_\alpha\in A$ |
| $P^{t}(D)$ | The transpose $\varphi\mapsto\sum(-1)^{\lvert\alpha\rvert}(\partial^\alpha\varphi)a_\alpha$, coefficients on the right |
| $\sigma_P(\zeta)$ | The symbol $\sum a_\alpha(i\zeta)^\alpha$, an element of $A_{\mathbb{C}}$ |
| $Z(P)$ | The zero set $\{\zeta:\sigma_P(\zeta)$ is not a unit$\}$ |
| $r(\zeta)$ | The rank of $L_{\sigma_P(\zeta)}$ at the frequency $\zeta$ |
| $L_a$ | Left multiplication by $a$ |
| $\operatorname{Ann}_L(a)$ | The left annihilator $\{x:ax=0\}$, the kernel of $L_a$ |
| $H$ | A separable complex Hilbert space |
| $\Phi$, $\Phi'$ | The test space and its strong dual |
| $\mathcal{S}$ | The Schwartz space of $A_{\mathbb{C}}$-valued functions |
| $\mathcal{S}'$ | The tempered distributions, the dual of $\mathcal{S}$ |
| $\lVert\cdot\rVert_{\alpha,\beta}$ | The seminorm $\sup_x\lVert x^\beta\partial^\alpha f(x)\rVert$ on $\mathcal{S}$ |
| $\mathcal{F}$ | The transform $\int e^{-i\zeta\cdot x}f(x)\,dx$, and its transpose on $\mathcal{S}'$ |
| $\langle u,\varphi\rangle$ | The pairing of $\Phi'$ with $\Phi$, $A_{\mathbb{C}}$-valued |
| $\tau_y$ | The translation $(\tau_yu)(x)=u(x+y)$ |
| $\gamma_\zeta$ | The character $\gamma_\zeta(y)=e^{i\zeta\cdot y}$ |
| $u_{\zeta,a}$ | The generalized eigenvector $e^{i\zeta\cdot x}a$ at the frequency $\zeta$ |
| $\delta_\zeta$ | The delta distribution at the frequency $\zeta$ |
| $PW_K$ | The Paley–Wiener space of a compact $K$, $\{f:\operatorname{supp}\mathcal{F}f\subset K\}$ |
| $S_0$ | The union of the $PW_K$ over compact $K$, the space of compactly supported transform |
| $\lvert K\rvert$ | The Lebesgue measure of $K$ |
| $\chi$ | A continuous positive-definite function on $\Phi$, in the Minlos theorem |
| $\mu$ | A Radon probability measure on $\Phi'$ |
| $E$ | The spectral measure of a self-adjoint operator |
| $\xi_\lambda$ | A generalized eigenvector of a self-adjoint operator, eigenvalue $\lambda$ |
| $\zeta$, $n$ | The frequency in $\mathbb{R}^n$, and the number of variables |
| $\alpha$, $\beta$ | Multi-indices, in the derivative and in the position variable |

## Further Reading

- *The Fourier Transform and the Symbol of a Differential Operator*, for the symbol, the zero set, and the theorem that the kernel and the cokernel of $L_{\sigma_P(\zeta)}$ have dimension $d-r(\zeta)$; the second half of this article is that theorem read in the dual.
- *The Inverse Fourier Transform of a Symbol*, for the Plancherel identity with the constant $(2\pi)^n$ and for the growth of the inverse transform, which is the scalar form of the pole questions.
- *The Fourier Transform on Vector-Valued and Operator-Valued Function Spaces*, for the transform on a Hilbert space of values, the unitary it defines, and the character that appears here as $\gamma_\zeta$.
- *Fourier Analysis on Euclidean Spaces*, for the inversion formula, the reflection identity $\mathcal{F}^2f=(2\pi)^nf(-\cdot)$, and the inversion theorem in the normalisation with $2\pi$ in the exponent, from which the constant here is obtained by substitution.
- *Distributions and Fundamental Solutions*, for the calculus of tempered distributions, the transpose of a differential operator, and the pairing used in every computation of §*Generalized Eigenvectors at a Frequency*.
- *Nuclear Spaces*, for nuclearity, the theorem that an infinite-dimensional Banach space is not nuclear, and the approximation numbers that make Minlos's hypothesis available.
- *Locally Convex Spaces*, for the topology of $\mathcal{S}$, its reflexivity and its Montel property, and for the strong dual.
- *Duality Theory*, for the transpose of a continuous linear map and for the duality between a space and its strong dual.
- *The Schwartz Kernel Theorem*, for the kernel theorem on a nuclear space, which is the other use of the same nuclearity.
- *Biquaternion Fourier Transform: Symbol, Block Determinant and Zero Set*, for the rank $4$ of $8$ on the null cone and the rank $0$ at the origin, which are the numbers $r(\zeta)$ in the case of the biquaternion algebra.
- *The Inverse Biquaternion Fourier Transform: Poles, Types and Tails*, for the programme of a measure and a residue calculus on the null cone, which is what a Plancherel formula for the algebra-valued transform would need.
- I. M. Gelfand and N. Ya. Vilenkin, *Generalized Functions, Volume IV: Applications of Harmonic Analysis* (Academic Press, 1964), for rigged Hilbert spaces, the Minlos theorem, and the nuclear spectral theorem.
- K. Maurin, *Generalized Eigenfunction Expansions and Unitary Representations of Topological Groups* (Polish Scientific Publishers, 1968), for the spectral theorem on a nuclear triple and for the completeness of the generalized eigenvectors.
- Laurent Schwartz, *Théorie des distributions* (Hermann, 1966), for the topology of $\mathcal{S}$ and $\mathcal{S}'$ and for the transpose of a differential operator.
- François Trèves, *Topological Vector Spaces, Distributions and Kernels* (Academic Press, 1967), for the inductive limits, the strictness, and the duality of the spaces $PW_K$.
- Raymond E. A. C. Paley and Norbert Wiener, *Fourier Transforms in the Complex Domain* (American Mathematical Society, 1934), for the characterisation of $PW_K$ by entire functions of exponential type.
