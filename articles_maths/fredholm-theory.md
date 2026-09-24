
# __Fredholm Theory__

## Introduction

A bounded operator between Banach spaces can fail to be invertible in two ways: it can have a kernel, and it can have a cokernel. For a large and useful class of operators both failures are finite, and the two numbers that measure them can be subtracted. That difference, the **index**, is an integer that survives every compact perturbation, is additive under composition and is constant on each connected component of the set of such operators; it is the first example of a topological invariant attached to an operator, and the ancestor of the index theorems of elliptic theory. The operators are the **Fredholm operators**, and their theory is the systematic form of the classical alternative for integral equations of the second kind: for $T=I-K$ with $K$ compact, either $Tx=y$ has a unique solution for every $y$, or the homogeneous equation has nontrivial solutions, and in the second case the number of independent solutions equals the number of independent obstructions.

The article proceeds from the compact theory to the index theory. The Riesz–Schauder theory identifies the operators of the form identity minus compact with the Fredholm operators of index zero on a fixed space and gives the alternative in its classical form; the definition of a Fredholm operator then isolates the two finite-dimensionality properties, and the index is defined and shown to be stable. The central structural theorem is Atkinson's: an operator is Fredholm exactly when it is invertible modulo the compact operators, and the index measures the failure of that invertibility to be liftable. From Atkinson follow the invariance of the index under compact perturbations, its additivity under composition and the skew-symmetry $\operatorname{ind}(T^*)=-\operatorname{ind}(T)$. The article closes with the Hilbert-space form of the theory, with the Toeplitz operators as a worked class whose index is computed by a winding number, and with the elliptic operators, where the index is the object of the Atiyah–Singer theorem.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, $X,Y,Z$ are Banach spaces over $\mathbb{K}$, and $T \in B(X,Y)$ means a bounded linear operator, with the operator norm and the dual as in *Banach and Hilbert Spaces*. The compact operators are those of that article, and the Riesz–Schauder and Fredholm-alternative statements recorded there are used as the starting point and extended here. The spectrum and the resolvent are those of *Banach and Hilbert Spaces*; their unbounded version, and the spectral measures of self-adjoint operators, are not covered here. The Schwartz kernel representation of an integral operator is that of *The Schwartz Kernel Theorem*; the algebra of compact operators and the Calkin algebra are developed further in *Operator Algebras*. The index theorems for elliptic operators on manifolds, of which the Toeplitz index is the model case, belong to *The Atiyah–Singer Index Theorem and K-Theory*, and the Toeplitz operators themselves are harmonic analysis, treated; both are cited rather than developed. The Hardy space $H^2$ used in the Toeplitz example is the standard one.

No physics is invoked.

## Compact Operators and the Riesz–Schauder Theory

### Compactness

**Definition.** An operator $T \in B(X,Y)$ is **compact** if the image of the closed unit ball of $X$ is relatively compact in $Y$; equivalently, if every bounded sequence $(x_n)$ has a subsequence $(x_{n_k})$ for which $T x_{n_k}$ converges. The set of compact operators is written $\mathcal K(X,Y)$, and $\mathcal K(X)=\mathcal K(X,X)$.

The compact operators form a closed two-sided ideal of $B(X)$, hence of each $B(X,Y)$; they are the closure of the finite-rank operators when $X$ or $Y$ has a Schauder basis with the approximation property, and in particular on Hilbert spaces. A compact operator is never invertible on an infinite-dimensional space, and the identity on an infinite-dimensional space is not compact: this is the Riesz lemma.

**Theorem (Schauder).** $T \in B(X,Y)$ is compact if and only if its transpose $T^* \in B(Y^*,X^*)$ is compact.

### The Fredholm Alternative

**Definition.** For $K \in \mathcal K(X)$ the operator $T=I-K$ is a **Riesz–Schauder operator**. The **null space** of $T$ is $N(T)=\ker T$ and the **range** is $R(T)=T(X)$.

**Theorem (Riesz–Schauder).** Let $K \in \mathcal K(X)$ and $T=I-K$. Then:

(i) $N(T)$ is finite-dimensional and $R(T)$ is closed in $X$;

(ii) $X/R(T)$ is finite-dimensional and $\dim(X/R(T))=\dim N(T)$;

(iii) $R(T)=R(T^m)$ and $N(T)=N(T^m)$ for every $m \ge 1$;

(iv) the operator $T$ is injective if and only if it is surjective, and then it is invertible with a bounded inverse;

(v) $\dim N(T)=\dim N(T^*)$, where $T^*=I-K^*$ on $X^*$ and $K^*$ is compact.

**Theorem (Fredholm alternative).** Let $K$ be compact on $X$. For the equation $Tx=y$ with $T=I-K$ exactly one of the following holds: either for every $y \in X$ there is a unique solution, or the homogeneous equation $Tx=0$ has a finite number $d\ge1$ of independent solutions, in which case $Tx=y$ is solvable exactly for those $y$ orthogonal to the $d$-dimensional solution space of the transposed homogeneous equation $T^*\varphi=0$.

*Proof.* The two theorems are standard; the compactness of $K$ makes the unit ball of $N(T)$ compact, so $N(T)$ is finite-dimensional; the closedness of $R(T)$ and the equality of the dimensions follow from the Riesz theory of compact operators on Banach spaces, and (iv) is the principle of the alternative. A complete proof is given in the works cited below. $\square$

**Theorem (spectrum of a compact operator).** Let $K \in \mathcal K(X)$ with $X$ infinite-dimensional. Then $\sigma(K)$ consists of $0$ together with at most countably many nonzero eigenvalues of finite algebraic multiplicity, and if there are infinitely many nonzero eigenvalues they accumulate only at $0$; the eigenspaces $N(K-\lambda)$ for $\lambda \neq0$ are finite-dimensional, and $K-\lambda$ is Fredholm of index $0$ for every $\lambda \neq0$.

## Fredholm Operators and the Index

### Definition and Elementary Properties

**Definition.** An operator $T \in B(X,Y)$ is **Fredholm** if

$$
\dim\ker T<\infty, \qquad \operatorname{codim}T(X)=\dim(Y/T(X))<\infty,
$$

the range is required to be closed so that the codimension is defined; conversely the finite-dimensionality of $Y/T(X)$ forces the range to be closed, since for a finite-dimensional complement $M$ of $T(X)$ the map $X\times M\to Y$, $(x,m)\mapsto Tx+m$, is a bounded bijection onto the Banach space $Y$ and therefore, by the open mapping theorem, a homeomorphism, which carries the closed subspace $X\times\{0\}$ onto $T(X)$. So $T$ is Fredholm exactly when $\dim\ker T<\infty$ and $\operatorname{codim}T(X)<\infty$. The **index** of a Fredholm operator is the integer

$$
\operatorname{ind}T=\dim\ker T-\dim\operatorname{coker}T, \qquad \operatorname{coker}T=Y/T(X).
$$

The set of Fredholm operators from $X$ to $Y$ is written $\Phi(X,Y)$, and $\Phi(X)=\Phi(X,X)$.

**Proposition.** (i) Every invertible operator is Fredholm of index $0$. (ii) If $K$ is compact then $I-K$ is Fredholm of index $0$. (iii) A finite-rank perturbation $T+F$ of a Fredholm operator is Fredholm, and its index equals that of $T$ by the stability theorem proved below.

*Proof.* (i) $\dim\ker T=0$ and $\operatorname{coker}T=0$. (ii) is the Riesz–Schauder theorem, part (ii). (iii) The perturbation is by a compact operator, so Fredholmness follows from the parametrix argument of Atkinson's theorem and the index equality from the invariance under compact perturbation. $\square$

**Example (the unilateral shift).** On $\ell^2$ with the standard orthonormal basis $(e_1,e_2,\dots)$, the **forward shift** is $S(x_1,x_2,\dots)=(0,x_1,x_2,\dots)$, and its Hilbert adjoint, the **backward shift**, is $S^*(x_1,x_2,\dots)=(x_2,x_3,\dots)$. Then

$$
\ker S=0, \qquad \operatorname{coker}S=\ell^2/S(\ell^2)\cong\mathbb{K}, \qquad \operatorname{ind}S=-1,
$$

because $S(\ell^2)=\{x:x_1=0\}$ is a closed hyperplane, while

$$
\ker S^*=\mathbb{K}e_1, \qquad \operatorname{coker}S^*=0, \qquad \operatorname{ind}S^*=+1 .
$$

The shift is the simplest Fredholm operator of nonzero index; it is an isometry, so it is not compact, and its index is the obstruction to its being invertible. The product $S^*S=I$ has index $0=(-1)+(+1)$, in agreement with additivity, while $SS^*$ is the orthogonal projection onto $\{x:x_1=0\}$, of index $0$ as well.

**Example (integral operators).** Let $K \in L^2(X\times Y)$ and let $T$ be the Hilbert–Schmidt operator with kernel $K$, as in *The Schwartz Kernel Theorem*. Then $T$ is compact, so $I-T$ is Fredholm of index $0$ on $L^2$, and the Fredholm alternative applies to the integral equation $u-Tu=f$: the equation is solvable for exactly those $f$ orthogonal to the solutions of the transposed homogeneous equation.

### The Parametrix Characterisation

**Definition.** A **parametrix**, or **Fredholm inverse**, of $T \in B(X,Y)$ is an operator $S \in B(Y,X)$ with

$$
ST=I-K_1, \qquad TS=I-K_2, \qquad K_1 \in \mathcal K(X),\ K_2 \in \mathcal K(Y).
$$

**Theorem (Atkinson).** $T \in \Phi(X,Y)$ if and only if $T$ has a parametrix.

*Proof.* Let $T$ be Fredholm. Since $\ker T$ is finite-dimensional and $T(X)$ is closed with finite-dimensional complement, there are closed subspaces $X_0 \subseteq X$ and $Y_0 \subseteq Y$ with $X=\ker T\oplus X_0$, $Y=T(X)\oplus Y_0$, and $T$ maps $X_0$ bijectively onto $T(X)$; by the open mapping theorem of *Normed and Banach Spaces*, the inverse $T|_{X_0}^{-1}:T(X)\to X_0$ is bounded, and it extends to a bounded $S:Y \to X$ by setting $S=0$ on $Y_0$. Then $ST$ is the projection of $X$ onto $X_0$ along $\ker T$, so $ST=I-K_1$ with $K_1$ of finite rank, and $TS$ is the projection onto $T(X)$ along $Y_0$, so $TS=I-K_2$ with $K_2$ of finite rank; both are compact. Conversely, if $ST=I-K_1$, then $\ker T \subseteq \ker(ST)=\ker(I-K_1)$, which is finite-dimensional by Riesz–Schauder. Also $T(X)\supseteq TS(Y)=(I-K_2)(Y)$, a closed subspace of finite codimension in $Y$; a subspace containing a closed subspace of finite codimension is itself closed, since its image in the finite-dimensional quotient is a subspace and hence closed, so the range is closed, and $Y/T(X)$ is a quotient of $Y/(I-K_2)(Y)$, of dimension at most $\dim\ker(I-K_2)<\infty$, the kernel and the cokernel of the Riesz–Schauder operator $I-K_2$ having the same finite dimension. $\square$

**Corollary (Calkin algebra).** Let $\mathcal K(X)$ be the closed two-sided ideal of compact operators on $X$. Then $T$ is Fredholm if and only if its class $[T]$ in the **Calkin algebra** $B(X)/\mathcal K(X)$ is invertible, and the index is a homomorphism from the group of invertible elements of the Calkin algebra to $\mathbb{Z}$,

$$
\operatorname{ind}:\Phi(X)/\!\sim\;\longrightarrow\mathbb{Z}, \qquad [T]\longmapsto\operatorname{ind}T,
$$

which does not depend on the choice of representative. The Calkin algebra is a $C^*$-algebra when $X$ is a Hilbert space; its structure and the theory of its invertible elements are those of *Operator Algebras*.

**Theorem (Atkinson's theorem, compact-perturbation form).** If $T$ is Fredholm and $K$ is compact, then $T+K$ is Fredholm and

$$
\operatorname{ind}(T+K)=\operatorname{ind}T .
$$

*Proof.* Let $S$ be a parametrix of $T$: $ST=I-K_1$, $TS=I-K_2$ with $K_i$ compact. Then $S(T+K)=I-K_1+SK$, and $SK$ is compact because the compact operators are an ideal; hence $I-K_1+SK=I-(K_1-SK)$ is Fredholm of index $0$ by Riesz–Schauder, so $S(T+K)$ is Fredholm; since $S$ has a parametrix $T$, the product $S(T+K)$ is Fredholm exactly when $T+K$ is, and the index of the product is additive. The same argument on the other side gives the two-sided statement. The additivity used here is proved next. $\square$

### Additivity and Functoriality of the Index

**Theorem.** Let $T \in \Phi(X,Y)$ and $S \in \Phi(Y,Z)$. Then $ST \in \Phi(X,Z)$ and

$$
\operatorname{ind}(ST)=\operatorname{ind}S+\operatorname{ind}T .
$$

*Proof.* That $ST$ is Fredholm follows from the parametrix characterisation: the product of parametrices is a parametrix. For the index, consider the exact sequence

$$
0 \longrightarrow \ker T \longrightarrow \ker(ST) \xrightarrow{\,T\,} \ker S \xrightarrow{\,\delta\,} \operatorname{coker}T \xrightarrow{\,S\,} \operatorname{coker}(ST) \longrightarrow \operatorname{coker}S \longrightarrow 0,
$$

where the map $\delta$ sends $y \in \ker S$ to its class in $Y/T(X)$ and the maps between cokernels are induced by $S$. Exactness is checked at each term: the image of $T|_{\ker(ST)}$ is $T(X)\cap\ker S$, which is the kernel of $\delta$; the kernel of the map $\operatorname{coker}T\to\operatorname{coker}(ST)$ is $(\ker S+T(X))/T(X)$, which is the image of $\delta$; and the last map is surjective because it is the quotient map $Z/ST(X)\to Z/S(Y)$. Taking alternating dimensions along the sequence gives

$$
0=\dim\ker T-\dim\ker(ST)+\dim\ker S-\dim\operatorname{coker}T+\dim\operatorname{coker}(ST)-\dim\operatorname{coker}S,
$$

which rearranges to $\operatorname{ind}(ST)=\operatorname{ind}S+\operatorname{ind}T$. $\square$

**Theorem.** For $T \in \Phi(X,Y)$, the transpose $T^*$ is Fredholm from $Y^*$ to $X^*$ and

$$
\operatorname{ind}T^*=-\operatorname{ind}T, \qquad \dim\operatorname{coker}T=\dim\ker T^* .
$$

*Proof.* The annihilator of $T(X)$ in $Y^*$ is $\ker T^*$, and the annihilator of $\ker T$ in $X^*$ is the image $T^*(Y^*)$ when the range is closed; these are the standard duality identities of *Duality Theory*. Hence $\operatorname{coker}T=Y/T(X)$ has dual $\ker T^*$, so the two spaces have the same finite dimension, and $\dim\operatorname{coker}T^*=\dim\ker T$. Therefore

$$
\operatorname{ind}T^*=\dim\ker T^*-\dim\operatorname{coker}T^*=\dim\operatorname{coker}T-\dim\ker T=-\operatorname{ind}T . \qquad\square
$$

**Corollary.** $\operatorname{ind}T=0$ for every $T \in \Phi(X)$ of the form $T=I-K$ with $K$ compact, in agreement with Riesz–Schauder; more generally, an operator is Fredholm if and only if it is a compact perturbation of an invertible operator of the same index.

### Stability and Continuity of the Index

**Theorem (openness).** $\Phi(X,Y)$ is open in $B(X,Y)$ and the index is constant on each connected component of $\Phi(X,Y)$; consequently the index is a homotopy invariant: if $t \mapsto T_t$ is a continuous path in $\Phi(X,Y)$ then $\operatorname{ind}T_t$ is independent of $t$.

*Proof.* Let $T$ be Fredholm with parametrix $S$, so $ST=I-K_1$ and $TS=I-K_2$ with $K_1,K_2$ compact. Let $\|A\|<\|S\|^{-1}$, so $\|SA\|<1$ and $I+SA$ is invertible with inverse given by the Neumann series. Then

$$
S(T+A)=ST+SA=I+SA-K_1=(I+SA)\bigl(I-(I+SA)^{-1}K_1\bigr),
$$

and $(I+SA)^{-1}K_1$ is compact because the compact operators are an ideal; by Riesz–Schauder the factor $I-(I+SA)^{-1}K_1$ is Fredholm of index $0$, so $S(T+A)$ is Fredholm, and since $S$ is Fredholm with parametrix $T$, the class $[T+A]=[S]^{-1}[S(T+A)]$ is invertible in the Calkin algebra; hence $T+A$ is Fredholm. For the index, additivity applied to $S(T+A)$ gives $\operatorname{ind}(S(T+A))=0=\operatorname{ind}S+\operatorname{ind}(T+A)$, while additivity applied to $ST$ gives $\operatorname{ind}S+\operatorname{ind}T=0$; subtracting, $\operatorname{ind}(T+A)=\operatorname{ind}T$. The estimate is uniform on the ball of radius $\|S\|^{-1}$ about $T$, so the index is locally constant on $\Phi(X,Y)$ and hence constant on each connected component; a continuous path lies in one component. $\square$

**Corollary (invariance).** The index is invariant under compact perturbation, under finite-rank perturbation, under composition with invertible operators, $\operatorname{ind}(UTV)=\operatorname{ind}T$ for invertible $U,V$ of the appropriate spaces, and under transposition up to sign.

**Corollary (essential spectrum).** For $T \in B(X)$ the **essential spectrum** is

$$
\sigma_{\mathrm{ess}}(T)=\{\lambda \in \mathbb{K}:T-\lambda \notin \Phi(X)\},
$$

a closed subset of $\sigma(T)$. Every compact perturbation of $T$ has the same essential spectrum, because compact perturbations preserve Fredholmness and the index; this is Weyl's theorem. The index function $\lambda \mapsto \operatorname{ind}(T-\lambda)$ is constant on each component of the complement of $\sigma_{\mathrm{ess}}(T)$, and the study of this function is the starting point of the index theory of families of operators.

## Fredholm Operators on Hilbert Space

### Adjoints and Orthogonal Splittings

**Definition.** Let $H$ be a Hilbert space and $T \in B(H)$. The **Hilbert adjoint** $T^{\dagger}$ is defined by $\langle Tx,y\rangle=\langle x,T^{\dagger}y\rangle$.

**Theorem.** Let $T \in B(H)$ be Fredholm. Then

$$
H=\ker T \oplus (\ker T)^\perp=\overline{T(H)}\oplus\ker T^{\dagger}, \qquad T(H)=\ker(T^{\dagger})^\perp ,
$$

the map $T|_{(\ker T)^\perp}:(\ker T)^\perp \to T(H)$ is a topological isomorphism, and

$$
\operatorname{ind}T=\dim\ker T-\dim\ker T^{\dagger} .
$$

Moreover $T$ is Fredholm if and only if $T^{\dagger}$ is, and $\operatorname{ind}T^{\dagger}=-\operatorname{ind}T$.

*Proof.* The orthogonal decomposition $H=\overline{T(H)}\oplus T(H)^\perp$ and the identity $T(H)^\perp=\ker T^{\dagger}$ are the standard orthogonal-projection facts of *Banach and Hilbert Spaces*; the range $T(H)$ is closed and equals $\ker(T^{\dagger})^\perp$. The restriction is injective by the definition of $(\ker T)^\perp$ and surjective onto $T(H)$, and it is bounded below, hence a topological isomorphism. The formula for the index is $\dim\ker T-\dim\operatorname{coker}T=\dim\ker T-\dim\ker T^{\dagger}$. $\square$

**Corollary (Fredholm operators and the polar decomposition).** If $T \in B(H)$ is Fredholm, then $T^{\dagger}T$ and $TT^{\dagger}$ are Fredholm of index $0$, and $T=U|T|$ with $|T|=(T^{\dagger}T)^{1/2}$ and $U$ the partial isometry that is unitary from $(\ker T)^\perp$ onto $T(H)$, the pair $(U,|T|)$ being determined uniquely by these properties; the positive operator $T^{\dagger}T$ is invertible on $(\ker T)^\perp$, its kernel is exactly $\ker T$, and that kernel is finite-dimensional because $T$ is Fredholm.

### Toeplitz Operators and the Winding Number

Let $S^1 \subseteq \mathbb{C}$ be the unit circle and let $H^2(S^1) \subseteq L^2(S^1)$ be the Hardy space of functions whose negative Fourier coefficients vanish, with the orthogonal projection $P$. For $\varphi \in C(S^1)$ the **Toeplitz operator** with symbol $\varphi$ is

$$
T_\varphi:H^2 \to H^2, \qquad T_\varphi f=P(\varphi f).
$$

**Theorem (Toeplitz index theorem).** Let $\varphi \in C(S^1)$ be nowhere vanishing and let $\operatorname{wind}(\varphi)$ be the winding number of $\varphi$ about $0$. Then $T_\varphi$ is Fredholm and

$$
\operatorname{ind}T_\varphi=-\operatorname{wind}(\varphi).
$$

*Proof (sketch).* The symbol map is a homomorphism modulo compacts: $T_\varphi T_\psi-T_{\varphi\psi}$ is compact, so $T_\varphi$ is invertible in the Calkin algebra exactly when $\varphi$ is invertible in $C(S^1)$, that is, nowhere vanishing. The index is then computed on the generator: for $\varphi(z)=z$ the operator $T_z$ is the forward shift on $H^2$, whose index is $-1$ by the computation above, and $\operatorname{wind}(z)=1$; since the winding number is additive under multiplication and the index is additive under composition, the identity holds on the dense subalgebra generated by the monomials and extends by continuity and the homotopy invariance of both sides. $\square$

The theorem is the model of an index theorem: an analytic integer, the index, equals a topological integer, the winding number, and the equality is proved by checking one generator. The Toeplitz operators, their symbols and their Fredholm theory are developed; the Hardy space and its projection are the standard ones. The generalisation to an elliptic operator on a closed manifold replaces the winding number by a topological invariant of the symbol, and the result is the Atiyah–Singer index theorem, treated in *The Atiyah–Singer Index Theorem and K-Theory*.

### Elliptic Operators

**Theorem (Fredholm property of elliptic operators).** Let $P$ be an elliptic linear differential operator of order $m$ on a closed manifold $M$, acting between the Sobolev spaces $H^s(M)$ and $H^{s-m}(M)$. Then $P$ extends to a Fredholm operator for every $s$, its kernel consists of smooth functions and is finite-dimensional, and $\operatorname{ind}P$ is independent of $s$.

*Proof (sketch).* The parametrix of *Distributions and Fundamental Solutions* is a pseudodifferential operator $E$ with $PE=I-R$ and $EP=I-R'$ with smoothing remainders; smoothing operators are compact by the Sobolev embedding $H^s\hookrightarrow H^{s-m}$, so $E$ is a parametrix in the sense above and Atkinson's theorem applies. The regularity of the kernel and the independence of $s$ are the elliptic regularity and the smoothing property. $\square$

**Example (the Cauchy–Riemann operator).** On the Riemann sphere the Cauchy–Riemann operator $\bar\partial$ acting from functions to $(0,1)$-forms is Fredholm: its kernel is the constants, of dimension $1$, and its cokernel vanishes, so its index is $1$, the arithmetic genus of the sphere. It is the prototype of the Atiyah–Singer computation, in which the index of an elliptic operator is evaluated by topological data of its symbol; the examples, including the de Rham and Dolbeault complexes and their indices in terms of characteristic classes, belong to *The Atiyah–Singer Index Theorem and K-Theory*.

## Summary

A compact operator $K$ makes $I-K$ a Riesz–Schauder operator: its kernel and cokernel are finite-dimensional of equal dimension, its range is closed and it is invertible as soon as it is injective, and the spectrum of a compact operator consists of $0$ and countably many nonzero eigenvalues of finite multiplicity accumulating only at $0$; this is the Fredholm alternative for integral equations of the second kind. A bounded operator $T:X\to Y$ is **Fredholm** when its kernel and its cokernel are finite-dimensional, and its **index** is $\operatorname{ind}T=\dim\ker T-\dim\operatorname{coker}T$, an integer; invertible operators have index $0$, and so do the operators $I-K$ with $K$ compact.

The structural theorem is **Atkinson's**: $T$ is Fredholm if and only if it has a parametrix $S$ with $ST-I$ and $TS-I$ compact, equivalently if and only if its class in the Calkin algebra $B(X)/\mathcal K(X)$ is invertible. From this follow the invariance of the index under compact perturbations, its additivity $\operatorname{ind}(ST)=\operatorname{ind}S+\operatorname{ind}T$ under composition, its skew-symmetry $\operatorname{ind}T^*=-\operatorname{ind}T$ together with $\dim\operatorname{coker}T=\dim\ker T^*$, and the openness of the set of Fredholm operators with an index that is locally constant and therefore homotopy invariant. On a Hilbert space the orthogonal splittings $H=\ker T\oplus(\ker T)^\perp=T(H)\oplus\ker T^{\dagger}$ identify the cokernel with $\ker T^{\dagger}$ and give $\operatorname{ind}T=\dim\ker T-\dim\ker T^{\dagger}$. The unilateral shift on $\ell^2$ is the standard Fredholm operator of nonzero index, $\operatorname{ind}S=-1$, and it generates the Toeplitz example: for a nowhere-vanishing continuous symbol $\varphi$ on the circle, $\operatorname{ind}T_\varphi=-\operatorname{wind}(\varphi)$. Elliptic operators on closed manifolds are Fredholm between Sobolev spaces, with a parametrix supplied by the pseudodifferential calculus, and their index is the object of the Atiyah–Singer theorem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X,Y,Z$ | Banach spaces; $H$ a Hilbert space |
| $B(X,Y)$, $B(X)$ | bounded operators |
| $\mathcal K(X,Y)$, $\mathcal K(X)$ | compact operators |
| $T^*$, $T^{\dagger}$ | Banach transpose and Hilbert adjoint |
| $N(T)=\ker T$, $R(T)=T(X)$ | kernel and range |
| $\operatorname{coker}T=Y/T(X)$ | cokernel |
| $\Phi(X,Y)$, $\Phi(X)$ | Fredholm operators |
| $\operatorname{ind}T$ | Fredholm index $\dim\ker T-\dim\operatorname{coker}T$ |
| $S$, $K_1$, $K_2$ | parametrix and compact remainders |
| $B(X)/\mathcal K(X)$ | Calkin algebra |
| $\sigma(T)$, $\sigma_{\mathrm{ess}}(T)$ | spectrum and essential spectrum |
| $S$, $S^*$ | forward and backward shift on $\ell^2$ |
| $H^2(S^1)$, $P$, $T_\varphi$ | Hardy space, Szegő projection, Toeplitz operator |
| $\operatorname{wind}(\varphi)$ | winding number of a symbol |
| $H^s(M)$ | Sobolev space on a manifold |
| $R$ | smoothing remainder of a parametrix |





## Further Reading

- Ivar Fredholm, "Sur une classe d'équations fonctionnelles", *Acta Mathematica* 27 (1903), 365–390, for the original integral-equation theory and the alternative.
- Friedrich Riesz, "Über lineare Funktionalgleichungen", *Acta Mathematica* 41 (1918), 71–98, for the Riesz–Schauder theory of compact operators.
- Stefan Banach, *Théorie des opérations linéaires* (Warsaw, 1932), for the Fredholm theory in Banach spaces and the open mapping background.
- Frederick V. Atkinson, "The normal solvability of linear equations in normed spaces", *Matematicheskii Sbornik* 28 (1951), 3–14, for the theorem characterising Fredholm operators by invertibility modulo compacts.
- Israel Gohberg, Seymour Goldberg and Marinus A. Kaashoek, *Classes of Linear Operators*, vol. 1 (Birkhäuser, 1990), for the operator-theoretic Fredholm theory, the index and its stability.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for Fredholm operators, the essential spectrum and the invariance of the index.
- Michael F. Atiyah and Isadore M. Singer, "The index of elliptic operators I", *Annals of Mathematics* 87 (1968), 484–530, for the index theorem of which the Toeplitz theorem is the model case.
- Ronald G. Douglas, *Banach Algebra Techniques in Operator Theory* (Springer, 2nd ed. 1998), for the Calkin algebra, Toeplitz operators and their index.
- Albrecht Böttcher and Bernd Silbermann, *Analysis of Toeplitz Operators* (Springer, 2nd ed. 2006), for the Toeplitz index theorem in its general form.
