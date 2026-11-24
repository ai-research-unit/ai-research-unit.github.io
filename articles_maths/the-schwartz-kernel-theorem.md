
# __The Schwartz Kernel Theorem__

## Introduction

Every operator that arises in analysis is, or ought to be, an integral operator, and the question that the kernel theorem answers is what replaces the integral when the integral does not converge. The answer is a distribution on the product. Let $X \subseteq \mathbb{R}^m$ and $Y \subseteq \mathbb{R}^n$ be open, let $\mathcal D(X)$ be the test functions of *Distributions and Fundamental Solutions* and let $\mathcal D'(Y)$ be their dual, and let $T:\mathcal D(X) \to \mathcal D'(Y)$ be linear and continuous. The **Schwartz kernel theorem** states that there is a distribution $K \in \mathcal D'(Y \times X)$, unique, such that

$$
\langle T\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}}\rangle=\langle K,Ξ_{\mathrm{wfn}}\otimes\digamma_{\mathrm{map}}\rangle, \qquad (Ξ_{\mathrm{wfn}}\otimes\digamma_{\mathrm{map}})(y,x)=Ξ_{\mathrm{wfn}}(y)\digamma_{\mathrm{map}}(x),
$$

for all $\digamma_{\mathrm{map}} \in \mathcal D(X)$ and $Ξ_{\mathrm{wfn}} \in \mathcal D(Y)$. The kernel is written $K(y,x)$ with the variable of the image space first, the convention, so that when $K$ happens to be a locally integrable function the formula is the classical $T\digamma_{\mathrm{map}}(y)=\int K(y,x)\digamma_{\mathrm{map}}(x)\,dx$; the theorem says that the formula survives, with $K$ a distribution, for *every* continuous operator, and that no information about the operator is lost in the passage.

The theorem is a statement about the duality of tensor products, and it is exactly where the topological structure of the test-function spaces enters: for a pair of general Fréchet spaces the corresponding assertion is false, and it becomes true when the spaces are nuclear, which $\mathcal D(X)$ and $\mathcal S(\mathbb{R}^n)$ are. This article states the theorem in three equivalent forms — the operator form, the tensor-product form and the kernel-distribution form — proves it in the form that the nuclearity of $\mathcal D$ makes available, computes the kernels of the standard operators (identity, derivative, adjoint, composition, integral and pseudodifferential operators) and identifies the smooth kernels with the smoothing operators. The route through nuclearity is the one that shows *why* the theorem holds, and it uses the theory of topological tensor products of Part II rather than reproducing it.

Throughout, $X \subseteq \mathbb{R}^m$ and $Y \subseteq \mathbb{R}^n$ are nonempty open sets, $X \times Y \subseteq \mathbb{R}^{m+n}$ is their product, $\digamma_{\mathrm{map}}\otimesΞ_{\mathrm{wfn}}$ denotes the tensor product of test functions, and $\mathcal L(E,F)$ denotes the continuous linear maps between topological vector spaces, with $\mathcal D'(X)=\mathcal L(\mathcal D(X),\mathbb{K})$. The spaces $\mathcal D$, $\mathcal E$, $\mathcal S$ and their duals, the pairing, convolution, the differentiation of distributions and their Fourier transform are those of *Distributions and Fundamental Solutions*, and the derivative notation $D^\alpha$ fixed there is used without comment. The duality theory of locally convex spaces is that of *Duality Theory*, the Fréchet and LF structures are those of *Locally Convex Spaces*, and the projective and injective tensor products, their completions and the notion of a nuclear space are those of *Topological Tensor Products* and *Nuclear Spaces*. Compact operators and the Hilbert–Schmidt class are those of *Banach and Hilbert Spaces*. The pseudodifferential calculus that computes the kernel of a symbol and the composition of two such kernels is not covered here; the wavefront-set refinement of the kernel's singularities is not covered here; and the use of kernels to define the index and the Fredholm alternative is the subject, to which this article is the immediate prerequisite.

No physics is invoked.

## Distributions on a Product

### The Tensor Product of Test Functions

**Definition.** For $\digamma_{\mathrm{map}} \in \mathcal D(X)$ and $Ξ_{\mathrm{wfn}} \in \mathcal D(Y)$ the **tensor product** is the function

$$
(\digamma_{\mathrm{map}}\otimesΞ_{\mathrm{wfn}})(x,y)=\digamma_{\mathrm{map}}(x)Ξ_{\mathrm{wfn}}(y) \in \mathcal D(X \times Y),
$$

and $\mathcal D(X)\otimes\mathcal D(Y)$ denotes the vector space of finite sums $\sum_j\digamma_{\mathrm{map},j}\otimesΞ_{\mathrm{wfn},j}$.

**Proposition.** The bilinear map $(\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}})\mapsto\digamma_{\mathrm{map}}\otimesΞ_{\mathrm{wfn}}$ is injective and $\mathcal D(X)\otimes\mathcal D(Y)$ is dense in $\mathcal D(X\times Y)$.

*Proof.* Injectivity: if $\sum_j\digamma_{\mathrm{map},j}\otimesΞ_{\mathrm{wfn},j}=0$ as a function and the $Ξ_{\mathrm{wfn},j}$ are linearly independent, then every $\digamma_{\mathrm{map},j}=0$, choosing points $y$ at which the vectors $(Ξ_{\mathrm{wfn},j}(y))_j$ separate. Density: the space $\mathcal D(X)\otimes\mathcal D(Y)$ is a subalgebra of $C^\infty(X\times Y)$ that separates points and contains, with any two functions, their product; it is closed under differentiation and contains bump functions, since a product of bumps is a bump. Given $f \in \mathcal D(X\times Y)$ of compact support, its regularisations $f*\rho_\varepsilon$ lie in the closure of the tensor product by the uniform approximation of the smooth compactly supported $f$ together with the existence of product approximations on the support; more directly, one approximates $f$ uniformly with all derivatives by a finite sum of products using a partition of unity and one-dimensional approximations in each variable, and the supports are controlled.

**Remark.** Density of the algebraic tensor product is the essential point of the theorem, but it is not sufficient for it: the topology in which the density holds and the topology of $\mathcal D(X\times Y)$ have to match well enough that a continuous linear functional on the product is determined by its values on the products, and that a separately continuous bilinear form on $\mathcal D(X)\times\mathcal D(Y)$ factors through a continuous functional on $\mathcal D(X\times Y)$. Both requirements are consequences of nuclearity.

### The Tensor Product of Distributions

**Definition.** For $u \in \mathcal D'(X)$ and $v \in \mathcal D'(Y)$ the **tensor product** $u\otimes v \in \mathcal D'(X\times Y)$ is defined on products by

$$
\langle u\otimes v,\digamma_{\mathrm{map}}\otimesΞ_{\mathrm{wfn}}\rangle=\langle u,\digamma_{\mathrm{map}}\rangle\langle v,Ξ_{\mathrm{wfn}}\rangle
$$

and extended to all of $\mathcal D(X\times Y)$ by continuity and the density above; the extension exists and is unique because the estimate defining continuity is multiplicative on products.

**Proposition.** The map $(u,v)\mapsto u\otimes v$ is bilinear, separately continuous, and injective; the linear span $\mathcal D'(X)\otimes\mathcal D'(Y)$ is dense in $\mathcal D'(X\times Y)$ for the weak-$*$ topology.

**Example.** On $\mathbb{R}\times\mathbb{R}$ the tensor product of $\delta_0 \in \mathcal D'(\mathbb{R})$ with itself is the distribution $\delta_0\otimes\delta_0$, with $\langle\delta_0\otimes\delta_0,\Phi\rangle=\Phi(0,0)$; it is the two-dimensional delta at the origin and is not the same as the delta of the diagonal, which is the kernel of the identity below. The tensor product of a function of $x$ with a function of $y$ is the product function; the tensor product of $H(x)$ with $H(y)$ is $H(x)H(y)$.

## Continuous Linear Maps and Their Transposes

### The Space of Operators

**Definition.** The space $\mathcal L(\mathcal D(X),\mathcal D'(Y))$ carries the topology of bounded convergence: the seminorms are

$$
T \longmapsto \sup_{\digamma_{\mathrm{map}} \in B}\sup_{Ξ_{\mathrm{wfn}} \in C}|\langle T\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}}\rangle|,
$$

where $B$ ranges over the bounded subsets of $\mathcal D(X)$ and $C$ over the bounded subsets of $\mathcal D(Y)$; the pairing that defines them is the **bilinear form** of $T$,

$$
B_T(\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}})=\langle T\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}}\rangle, \qquad \digamma_{\mathrm{map}} \in \mathcal D(X),\ Ξ_{\mathrm{wfn}} \in \mathcal D(Y).
$$

**Proposition.** $T \mapsto B_T$ is a linear isomorphism of $\mathcal L(\mathcal D(X),\mathcal D'(Y))$ onto the space of separately continuous bilinear forms on $\mathcal D(X)\times\mathcal D(Y)$.

*Proof.* Given $T$, the form $B_T$ is linear and continuous in $Ξ_{\mathrm{wfn}}$ for fixed $\digamma_{\mathrm{map}}$ because $T\digamma_{\mathrm{map}} \in \mathcal D'(Y)$, and linear and continuous in $\digamma_{\mathrm{map}}$ for fixed $Ξ_{\mathrm{wfn}}$ because $\digamma_{\mathrm{map}}\mapsto\langle T\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}}\rangle$ is a continuous linear functional on $\mathcal D(X)$. Conversely a separately continuous form $B$ defines $T\digamma_{\mathrm{map}}$ as the distribution $Ξ_{\mathrm{wfn}}\mapsto B(\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}})$, and the continuity of $\digamma_{\mathrm{map}}\mapsto T\digamma_{\mathrm{map}}$ is the statement that $B$ is continuous in the first variable uniformly on the bounded sets of the second, which is the definition of the topology.

**Definition.** The **transpose** of $T \in \mathcal L(\mathcal D(X),\mathcal D'(Y))$ is the map ${}^tT:\mathcal D(Y)\to\mathcal D'(X)$ defined by

$$
\langle{}^tTΞ_{\mathrm{wfn}},\digamma_{\mathrm{map}}\rangle=\langle T\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}}\rangle .
$$

It is linear and continuous, and the assignment $T\mapsto{}^tT$ is an isomorphism of $\mathcal L(\mathcal D(X),\mathcal D'(Y))$ with $\mathcal L(\mathcal D(Y),\mathcal D'(X))$ of order two.

### Separate and Joint Continuity

For Fréchet spaces, separate continuity of a bilinear form implies joint continuity; this is the closed graph theorem of *Normed and Banach Spaces* together with Baire's theorem, and it is used below.

**Theorem.** Let $E,F$ be Fréchet spaces and $B:E\times F \to \mathbb{K}$ separately continuous and bilinear. Then $B$ is continuous for the product topology.

*Proof (sketch).* The associated linear map $\Phi:E\to F'$, $\Phi(x)=\langle x,\cdot\rangle$, has closed graph: if $x_k\to x$ in $E$ and $\Phi(x_k)\to f$ pointwise on $F$, then for each $y$ the continuity in the first variable gives $f(y)=\lim_kB(x_k,y)=B(x,y)$, so $f=\Phi(x)$; the closed graph theorem of *Normed and Banach Spaces* applied to $\Phi$, together with the continuity of the evaluation pairing, gives the joint continuity of $B$. The same conclusion follows from the Banach–Steinhaus theorem applied to the family of continuous functionals $\langle x_k,\cdot\rangle$.

**Corollary.** Every $T \in \mathcal L(\mathcal D(X),\mathcal D'(Y))$ has a bilinear form $B_T$ that is separately continuous, and the joint continuity of $B_T$ on $\mathcal D(X)\times\mathcal D(Y)$ is equivalent to the existence of the kernel, since $(\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}})\mapstoΞ_{\mathrm{wfn}}\otimes\digamma_{\mathrm{map}}$ is continuous into $\mathcal D(Y\times X)$: if $B_T(\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}})=\langle K,Ξ_{\mathrm{wfn}}\otimes\digamma_{\mathrm{map}}\rangle$ it is jointly continuous, and conversely a jointly continuous form extends to the completed projective tensor product. For Fréchet spaces the equivalence of separate and joint continuity is the theorem above; for the LF space $\mathcal D(X)$ it is proved with the kernel theorem below rather than before it.

## The Kernel Theorem

### Statement

**Theorem (Schwartz kernel theorem).** Let $X \subseteq \mathbb{R}^m$ and $Y \subseteq \mathbb{R}^n$ be open and nonempty. For every $T \in \mathcal L(\mathcal D(X),\mathcal D'(Y))$ there is a unique distribution $K \in \mathcal D'(Y \times X)$ with

$$
\boxed{\;\langle T\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}}\rangle=\langle K,Ξ_{\mathrm{wfn}}\otimes\digamma_{\mathrm{map}}\rangle \qquad \text{for all } \digamma_{\mathrm{map}} \in \mathcal D(X),\ Ξ_{\mathrm{wfn}} \in \mathcal D(Y)\;}.
$$

Conversely, every $K \in \mathcal D'(Y\times X)$ defines by this formula an operator $T \in \mathcal L(\mathcal D(X),\mathcal D'(Y))$. The map $K \mapsto T$ is a linear isomorphism

$$
\mathcal D'(Y\times X) \longrightarrow \mathcal L(\mathcal D(X),\mathcal D'(Y)).
$$

The distribution $K$ is the **kernel** or **Schwartz kernel** of $T$, and $T$ is the **operator with kernel** $K$.

**Corollary (partial pairing).** With $K$ the kernel of $T$ and $\digamma_{\mathrm{map}} \in \mathcal D(X)$,

$$
T\digamma_{\mathrm{map}}(y)=\langle K(y,x),\digamma_{\mathrm{map}}(x)\rangle_x \in \mathcal D'(Y),
$$

where the pairing is in the variable $x$ alone and the result is a distribution in $y$; explicitly, $\langle\langle K(y,x),\digamma_{\mathrm{map}}(x)\rangle_x,Ξ_{\mathrm{wfn}}(y)\rangle=\langle K,Ξ_{\mathrm{wfn}}\otimes\digamma_{\mathrm{map}}\rangle$.

### Proof from Nuclearity

The proof is quoted in outline, since the two ingredients are theorems of Part II.

**Theorem (nuclearity of the test-function spaces).** Every Fréchet nuclear space is a projective limit of Hilbert spaces with Hilbert–Schmidt linking maps; the spaces $\mathcal S(\mathbb{R}^n)$ and $\mathcal E(X)$ are Fréchet nuclear, and the LF space $\mathcal D(X)$ is nuclear in the sense of the inductive limits of nuclear Fréchet spaces. For two nuclear Fréchet spaces $E,F$ the completed projective and injective tensor products coincide,

$$
E\hat\otimes_\pi F=E\hat\otimes_\varepsilon F=:E\hat\otimes F,
$$

and the canonical maps $\mathcal D(X)\otimes\mathcal D(Y)\to\mathcal D(X\times Y)$ extend to a topological isomorphism

$$
\mathcal D(X)\hat\otimes_\pi\mathcal D(Y) \;\cong\; \mathcal D(X\times Y),
$$

and likewise $\mathcal S(\mathbb{R}^m)\hat\otimes_\pi\mathcal S(\mathbb{R}^n)\cong\mathcal S(\mathbb{R}^{m+n})$.

*Proof (sketch).* Injectivity and projectivity coincide for nuclear spaces by the construction of a nuclear Frechet space as a projective limit with Hilbert–Schmidt maps, and the second identity is the theorem of L. Schwartz that $\mathcal D(X\times Y)$ is the completed tensor product of $\mathcal D(X)$ and $\mathcal D(Y)$; the proofs are those of *Topological Tensor Products* and *Nuclear Spaces*.

**Proposition (dual of a projective tensor product).** For locally convex spaces $E,F$ the dual of the completed projective tensor product is the space of continuous bilinear forms,

$$
\bigl(E\hat\otimes_\pi F\bigr)' \;\cong\; \mathcal B(E,F),
$$

the isomorphism carrying a continuous linear functional on $E\hat\otimes_\pi F$ to its restriction $B(x,y)=\ell(x\otimes y)$. For Fréchet $E,F$ every separately continuous bilinear form is continuous, so the right-hand side is $\mathcal L(E,F')$ under $B \mapsto (x \mapsto \langle x,\cdot\rangle)$.

*Proof of the kernel theorem.* By the two theorems above,

$$
\mathcal L(\mathcal D(X),\mathcal D'(Y)) \cong \bigl(\mathcal D(X)\hat\otimes_\pi\mathcal D(Y)\bigr)' \cong \mathcal D'(X\times Y),
$$

since $\mathcal D(X)\hat\otimes_\pi\mathcal D(Y)\cong\mathcal D(X\times Y)$ and the dual of $\mathcal D(X\times Y)$ is $\mathcal D'(X\times Y)$; writing $K_{\mathrm{tr}}(x,y)$ for the distribution on $X\times Y$ so obtained and putting $K(y,x)=K_{\mathrm{tr}}(x,y)$, the interchange of the two factors being the canonical isomorphism $\mathcal D'(X\times Y)\cong\mathcal D'(Y\times X)$, gives the distribution of the theorem, with the variable of $Y$ first and the pairing $\langle K,Ξ_{\mathrm{wfn}}\otimes\digamma_{\mathrm{map}}\rangle$. Tracing the isomorphisms gives exactly the formula of the theorem: a functional $\ell$ on $\mathcal D(X)\hat\otimes_\pi\mathcal D(Y)$ restricts to $B(\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}})=\ell(\digamma_{\mathrm{map}}\otimesΞ_{\mathrm{wfn}})$, and the operator is $T\digamma_{\mathrm{map}}=\langle\digamma_{\mathrm{map}},\cdot\rangle$; conversely an operator gives a bilinear form and hence a functional, which is the distribution $K$. Uniqueness is the density of the algebraic tensor product in the completed one.

**Remark (where the theorem can fail).** For a pair of Fréchet spaces that are not nuclear the projective and injective tensor products differ, and the completion $E\hat\otimes_\pi F$ need not be identifiable with a space of functions or distributions on a product. The identity operator on $\ell^2$, which is not nuclear, still defines a continuous bilinear form $\langle x,y\rangle$ and hence an element of $(E\hat\otimes_\pi F)'$, but the form does not lie in the algebraic tensor product $\ell^2\otimes\ell^2$ and there is no kernel in $\ell^2\otimes\ell^2$ that represents it; the representation exists only after completion, and the completed object is no longer a space of distributions on $\ell^2\times\ell^2$. Nuclearity is what makes the two completions agree and the representation concrete.

### The Tempered Case

**Theorem (kernel theorem for $\mathcal S$).** For every $T \in \mathcal L(\mathcal S(\mathbb{R}^m),\mathcal S'(\mathbb{R}^n))$ there is a unique $K \in \mathcal S'(\mathbb{R}^n\times\mathbb{R}^m)$ with

$$
\langle T\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}}\rangle=\langle K,Ξ_{\mathrm{wfn}}\otimes\digamma_{\mathrm{map}}\rangle, \qquad \digamma_{\mathrm{map}} \in \mathcal S(\mathbb{R}^m),\ Ξ_{\mathrm{wfn}} \in \mathcal S(\mathbb{R}^n),
$$

and $K\mapsto T$ is an isomorphism $\mathcal S'(\mathbb{R}^{m+n})\cong\mathcal L(\mathcal S(\mathbb{R}^m),\mathcal S'(\mathbb{R}^n))$, the product of variables being identified with $\mathbb{R}^{m+n}$ in the order $(y,x)$. Consequently every continuous operator on the Schwartz space represents, and is represented , a tempered distribution in two variables; on the Fourier side, the kernel of $T$ corresponds to the distributional symbol of $T$ under the partial transform, which is the starting point.

**Example.** The operator of multiplication by a smooth function $\mathfrak{a} \in C^\infty(\mathbb{R}^n)$ on $\mathcal S(\mathbb{R}^n)$ has kernel $K(y,x)=\mathfrak{a}(y)\delta(x-y)$: indeed $\langle K,Ξ_{\mathrm{wfn}}\otimes\digamma_{\mathrm{map}}\rangle=\iint \mathfrak{a}(y)\delta(x-y)Ξ_{\mathrm{wfn}}(y)\digamma_{\mathrm{map}}(x)\,dx\,dy=\int \mathfrak{a}(y)\digamma_{\mathrm{map}}(y)Ξ_{\mathrm{wfn}}(y)\,dy=\langle \mathfrak{a}\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}}\rangle$. The kernel is not a function but a distribution concentrated on the diagonal, and this is the simplest instance of a kernel that no classical integral operator possesses.

## Kernels of the Standard Operators

### Identity, Derivative and Translation

**Theorem.** On $X=Y=\mathbb{R}^n$ and with $\Delta=\{(x,x)\}\subseteq\mathbb{R}^n\times\mathbb{R}^n$:

(i) the identity $T=I$ has kernel $\delta_\Delta=\delta(x-y)$, the **delta of the diagonal**, $\langle\delta(x-y),\Phi\rangle=\int_{\mathbb{R}^n}\Phi(x,x)\,dx$;

(ii) the derivative $T=\partial^\alpha$ has kernel $\partial^\alpha_y\delta(x-y)=(-1)^{|\alpha|}\partial^\alpha_x\delta(x-y)$;

(iii) the translation $T=\tau_a$, $\tau_a\digamma_{\mathrm{map}}(x)=\digamma_{\mathrm{map}}(x-a)$, has kernel $\delta(x+a-y)$;

(iv) the operator $T\digamma_{\mathrm{map}}(x)=\mathfrak{a}(x)\digamma_{\mathrm{map}}(x)$ of multiplication by $\mathfrak{a} \in C^\infty$ has kernel $\mathfrak{a}(y)\delta(x-y)$.

*Proof.* Each is verified by pairing with $\digamma_{\mathrm{map}}\otimesΞ_{\mathrm{wfn}}$ and reducing to the definitions: (i) gives $\langle\delta(x-y),\digamma_{\mathrm{map}}\otimesΞ_{\mathrm{wfn}}\rangle=\int\digamma_{\mathrm{map}}(x)Ξ_{\mathrm{wfn}}(x)=\langle\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}}\rangle$; (ii) gives $(-1)^{|\alpha|}\int\digamma_{\mathrm{map}}(x)\partial^\alphaΞ_{\mathrm{wfn}}(x)=\langle\partial^\alpha\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}}\rangle$; (iii) and (iv) are direct.

**Remark.** The identity operator is not an integral operator with a locally integrable kernel; its kernel is the delta of the diagonal, and every statement about kernels is a distributional statement. The diagonal is the set on which the classical theory fails, and the restriction to the diagonal of a general kernel — needed to define a trace — is not defined without further hypotheses, which are given microlocally.

### Adjoint, Composition and Integral Operators

**Definition.** For $T \in \mathcal L(\mathcal D(X),\mathcal D'(Y))$ with kernel $K \in \mathcal D'(X\times Y)$, the **adjoint** is the operator $T^* \in \mathcal L(\mathcal D(Y),\mathcal D'(X))$ with $\langle T\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}}\rangle=\langle\digamma_{\mathrm{map}},T^*Ξ_{\mathrm{wfn}}\rangle$ for test functions, and its kernel is written $K^*$.

**Theorem.** (i) $K^*(x,y)=\overline{K(y,x)}$; (ii) if $S \in \mathcal L(\mathcal D(Y),\mathcal D'(Z))$ has kernel $L(z,y)$, then $S\circ T$ has kernel

$$
\boxed{\;(L\circ K)(z,x)=\int_Y L(z,y)K(y,x)\,dy\;}
$$

whenever one of the operators has compactly supported kernel, the integral being the distributional pairing in $y$, $\langle L(z,\cdot),K(\cdot,x)\rangle$; (iii) if $K \in L^2(X\times Y)$ then $T$ extends to a compact operator $L^2(X)\to L^2(Y)$ with Hilbert–Schmidt norm $\langle T\rangle_*=\iint|K(x,y)|^2\,dx\,dy$, and every such operator has a kernel in $L^2(X\times Y)$; (iv) if $K \in C^\infty(X\times Y)$ then $T$ maps $\mathcal E'(X)$ into $C^\infty(Y)$, and these **smoothing** operators form a two-sided ideal in $\mathcal L(\mathcal D,\mathcal D')$.

*Proof.* (i) is the definition of the adjoint pairing; (ii) is the associative law for the iterated pairing, valid by Fubini when the supports permit; (iii) is the Hilbert–Schmidt theorem of *Banach and Hilbert Spaces*, the kernel being the matrix of $T$ in the continuous basis of the Hilbert space; (iv) is differentiation under the pairing against a smooth compactly supported distribution.

**Example (Green's function).** Let $P$ be a linear differential operator on $\Omega$ and let $G \in \mathcal D'(\Omega\times\Omega)$ be the kernel of a right inverse $T$ of $P$, so that $PT=I$. Then $G$ is a **Green's function**: for $f \in \mathcal D(\Omega)$, $u=Gf$ satisfies $Pu=f$ by composition of kernels, $PG=\delta_\Delta$. For an elliptic operator with a self-adjoint realisation the kernel is symmetric in the two variables, $G(x,y)=\overline{G(y,x)}$, and its singularity on the diagonal is the same as that of the fundamental solution of *Distributions and Fundamental Solutions*.

### Pseudodifferential Kernels

**Example (symbols and kernels).** For a symbol $\mathfrak{a}(x,\zeta)$ on $\mathbb{R}^n$ define formally

$$
T\digamma_{\mathrm{map}}(x)=\frac{1}{(2\pi)^n}\int \exp(i(x-y)\cdot\zeta)\mathfrak{a}(x,\zeta)\digamma_{\mathrm{map}}(y)\,dy\,d\zeta .
$$

If $\mathfrak{a}$ is a smooth function of at most polynomial growth in $\zeta$, the functional is defined by regularisation and the kernel is

$$
K(x,y)=\frac{1}{(2\pi)^n}\int \exp(i(x-y)\cdot\zeta)\mathfrak{a}(x,\zeta)\,d\zeta ,
$$

a distribution whose singularities lie on the diagonal and whose behaviour off the diagonal records the smoothness of $\mathfrak{a}$. The class of symbols, the composition formula that computes the kernel of a product of two such operators, and the conditions under which the integral converges are those, where the calculus is developed; the kernel theorem is what permits the operator and the kernel to be treated as the same object throughout.

## The Algebraic Form of the Theorem

The kernel theorem can be stated without test functions, as the compatibility of two tensor products with a duality.

**Theorem (algebraic form).** For Fréchet nuclear $E$ and $F$,

$$
\boxed{\;(E\hat\otimes F)' \cong E'\hat\otimes F' \cong \mathcal L(E,F')\;},
$$

the isomorphisms being the natural ones. Specialising to $E=\mathcal D(X)$, $F=\mathcal D(Y)$ recovers the kernel theorem in the form

$$
\mathcal D'(Y\times X) \cong \mathcal D'(Y)\hat\otimes\mathcal D'(X) ,
$$

and specialising to $E=\mathcal S(\mathbb{R}^m)$, $F=\mathcal S(\mathbb{R}^n)$ gives $\mathcal S'(\mathbb{R}^{m+n})\cong\mathcal S'(\mathbb{R}^m)\hat\otimes\mathcal S'(\mathbb{R}^n)$. In this form the theorem says that a distribution in $m+n$ variables decomposes, with respect to the two groups of variables, exactly as the operator from the first group to the second, and that the two descriptions are interchangeable.

**Corollary (finite-dimensional case).** For finite-dimensional spaces the theorem is the elementary identity $\mathcal L(\mathbb{K}^m,\mathbb{K}^n)\cong\mathbb{K}^m\otimes\mathbb{K}^n$: fixing bases $(e_i)$ of $\mathbb{K}^m$ and $(f_j)$ of $\mathbb{K}^n$, the kernel of the operator with matrix $(T_{ij})$ is

$$
K(y,x)=\sum_{i,j}T_{ij}\,f_i(y)e_j(x),
$$

which is the same as writing $K=\sum_{ij}T_{ij}\,\delta_{y_i}\otimes\delta_{x_j}$; composition of kernels is matrix multiplication, the adjoint kernel is the conjugate transpose, and the delta of the diagonal is the identity matrix. The kernel theorem is the infinite-dimensional form of the identification of an operator with its matrix.

## Summary

For open $X \subseteq \mathbb{R}^m$ and $Y \subseteq \mathbb{R}^n$, the algebraic tensor product $\mathcal D(X)\otimes\mathcal D(Y)$ of test functions, with $(\digamma_{\mathrm{map}}\otimesΞ_{\mathrm{wfn}})(x,y)=\digamma_{\mathrm{map}}(x)Ξ_{\mathrm{wfn}}(y)$, is dense in $\mathcal D(X\times Y)$, and tensor products of distributions extend to distributions on the product. Every continuous linear map $T:\mathcal D(X)\to\mathcal D'(Y)$ has a unique **kernel** $K \in \mathcal D'(Y\times X)$, characterised by $\langle T\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}}\rangle=\langle K,Ξ_{\mathrm{wfn}}\otimes\digamma_{\mathrm{map}}\rangle$ and recovered from the operator by the partial pairing $T\digamma_{\mathrm{map}}(y)=\langle K(y,x),\digamma_{\mathrm{map}}(x)\rangle_x$; the correspondence $K\leftrightarrow T$ is a linear isomorphism, and the transpose of $T$ corresponds to the reversal of the two variables.

The proof is the identification of three dualities: $\mathcal L(\mathcal D(X),\mathcal D'(Y))$ is the space of continuous bilinear forms on $\mathcal D(X)\times\mathcal D(Y)$, the dual of the completed projective tensor product is the space of such forms, and for the nuclear spaces $\mathcal D(X)$, $\mathcal D(Y)$ the completed projective tensor product is $\mathcal D(X\times Y)$. Nuclearity is essential: the two completions coincide, and the representation of an operator by a kernel on the product is concrete. The tempered version holds for $\mathcal S(\mathbb{R}^m)$, $\mathcal S(\mathbb{R}^n)$ and gives $\mathcal S'(\mathbb{R}^{m+n})\cong\mathcal L(\mathcal S(\mathbb{R}^m),\mathcal S'(\mathbb{R}^n))$, the bridge from operators to symbols.

The standard kernels are the delta of the diagonal for the identity, the derivatives of the delta for the differential operators, $\mathfrak{a}(x)\delta(x-y)$ for multiplication, the reflected conjugate kernel for the adjoint and the pairing integral for the composition; kernels in $L^2(X\times Y)$ are exactly the Hilbert–Schmidt operators, with the norm equal to the $L^2$ norm of the kernel, and smooth kernels are exactly the smoothing operators, which form a two-sided ideal. Green's functions are the kernels of inverses of differential operators, and the kernels of pseudodifferential operators are the oscillatory integrals $\frac{1}{(2\pi)^n}\int \exp(i(x-y)\cdot\zeta)\mathfrak{a}(x,\zeta)\,d\zeta$. The algebraic form of the theorem identifies $(E\hat\otimes F)'$ with $E'\hat\otimes F'$ and with $\mathcal L(E,F')$ for Fréchet nuclear $E,F$, so that a distribution in $m+n$ variables is the same thing as an operator from the first group of variables to the second; in finite dimension this is the identification of an operator with its matrix.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X,Y,Z$ | open subsets of $\mathbb{R}^m,\mathbb{R}^n,\mathbb{R}^p$ |
| $\mathcal D(X)$, $\mathcal D'(X)$ | test functions and distributions |
| $\mathcal S(\mathbb{R}^n)$, $\mathcal S'$ | Schwartz space and tempered distributions |
| $\digamma_{\mathrm{map}}\otimesΞ_{\mathrm{wfn}}$, $Ξ_{\mathrm{wfn}}\otimes\digamma_{\mathrm{map}}$ | tensor products of test functions, with the variables ordered as written |
| $\mathcal D(X)\otimes\mathcal D(Y)$ | algebraic tensor product |
| $E\hat\otimes_\pi F$, $E\hat\otimes_\varepsilon F$, $E\hat\otimes F$ | completed projective, injective and (nuclear) tensor products |
| $\mathcal L(E,F)$ | continuous linear maps |
| $B_T(\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}})=\langle T\digamma_{\mathrm{map}},Ξ_{\mathrm{wfn}}\rangle$ | bilinear form of an operator |
| $K$, $K(y,x)$ | Schwartz kernel, written with the variable of the image space first |
| $\delta(x-y)$, $\delta_\Delta$ | delta of the diagonal |
| ${}^tT$, $T^*$, $K^*$ | transpose, adjoint and adjoint kernel |
| $L\circ K$ | composition of kernels |
| $\langle T\rangle_*^{1/2}$ | Hilbert–Schmidt norm |
| $\mathfrak{a}(x,\zeta)$ | symbol of an operator |
| $G(x,y)$ | Green's function |


## Further Reading

- Laurent Schwartz, "Théorie des noyaux", *Proceedings of the International Congress of Mathematicians* (1950), vol. 1, 220–230, for the original statement and proof.
- Laurent Schwartz, *Théorie des distributions* (Hermann, 1950–51; revised 1966), for the tensor products of distributions and the nuclear structure of $\mathcal D$.
- Alexander Grothendieck, *Produits tensoriels topologiques et espaces nucléaires* (Memoirs of the American Mathematical Society 16, 1955), for the theory of nuclear spaces and tensor products on which the proof rests.
- François Trèves, *Topological Vector Spaces, Distributions and Kernels* (Academic Press, 1967), for the tensor-product form of the kernel theorem and its applications.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (Springer, 2nd ed. 1990), for the kernel theorem in the form used in the calculus of pseudodifferential operators.
- Gottfried Köthe, *Topological Vector Spaces II* (Springer, 1979), for nuclearity, tensor products and the duality theory of Fréchet spaces.
- Albrecht Pietsch, *Nuclear Locally Convex Spaces* (Springer, 1972), for the operator-theoretic account of nuclearity.
- Kôsaku Yosida, *Functional Analysis* (Springer, 6th ed. 1980), for the kernel theorem as the representation of an operator by its matrix in the continuous basis.
