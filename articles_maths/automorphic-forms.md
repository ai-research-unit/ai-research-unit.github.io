
# __Automorphic Forms__

## Introduction

An automorphic form is a function on a quotient of a reductive group by an arithmetic lattice that satisfies a finite set of analytic conditions — a transformation law under the lattice, a growth condition at infinity, and finiteness under the invariant differential operators. The classical examples are the modular forms of the upper half-plane, and the modern theory reads them as functions on the adelic group $G(\mathbb{A})$, where the arithmetic lattice becomes $G(\mathbb{Q})$ and the transformation law becomes invariance under the discrete subgroup. The altitude of the definition is what makes it powerful: the conditions are local, so an automorphic form decomposes into local pieces, one for each place of $\mathbb{Q}$, and the arithmetic information is carried by those local pieces.

The theory is the meeting point of four streams. The **classical** stream is the analytic theory of modular forms: the transformation law, the $q$-expansion, the Hecke operators, the Petersson inner product. The **representation-theoretic** stream is the decomposition of the space of automorphic forms into irreducible representations of $G(\mathbb{A})$, each a restricted tensor product of local representations, with the unramified local components encoded by a Satake parameter. The **spectral** stream is the decomposition of $L^2(G(\mathbb{Q})\backslash G(\mathbb{A}))$ into the cuspidal spectrum, the residual spectrum and the continuous spectrum of Eisenstein series, and the trace formula that computes it. The **arithmetic** stream is the theory of $L$-functions, the Euler products attached to an automorphic representation, and their functional equations. This article develops the first three and the outline of the fourth; the general conjectural framework that organises them is not treated here.

Three boundaries are held.

- The **classical theory of modular forms** — the upper half-plane, the transformation law, the Petersson inner product, the modular curves — is; this article cites it and does not develop it. The **adelic analysis** — the ring of adeles, the ideles, the Haar measure on an adèle group, Tate's local–global zeta integrals — is *Adeles and Ideles* and the neighbouring arithmetic articles; it is cited as the place where the tools are constructed.
- The **representation theory of locally compact groups** — admissibility, the unitary dual, induced representations, the tensor product theorems — is Part II's, in *Representation Theory of Locally Compact Groups* and *Induced Representations of Locally Compact Groups*; this article uses it.
- The **$L$-functions and zeta functions** in their general form are developed; this article states the automorphic $L$-function in line as standard mathematics and defers the general theory. The **Langlands correspondence** is not covered here. No physics is invoked.

Throughout, $\mathbb{A} = \mathbb{A}_{\mathbb{Q}}$ is the ring of adeles of $\mathbb{Q}$ and $\mathbb{A}^\times$ the ideles; a **place** $v$ of $\mathbb{Q}$ is either the archimedean place $\infty$ with $\mathbb{Q}_\infty = \mathbb{R}$, or a prime $p$ with $\mathbb{Q}_p$ the $p$-adic field; $G$ is a connected reductive group over $\mathbb{Q}$, and for $G = GL_2$ one writes $G(\mathbb{A})$ for the adelic group. The quotient $G(\mathbb{Q})\backslash G(\mathbb{A})$ is the arithmetic quotient, and $\Gamma = G(\mathbb{Z})$ is the arithmetic lattice. The Haar measure, the modular character, the centre $Z$, and the algebra $\mathfrak{g}$ of the Lie group $G(\mathbb{R})$ are those of Part II; the differential operators are the elements of the centre $\mathfrak{z}$ of the universal enveloping algebra of $\mathfrak{g}$.

## The Classical Picture

### Modular Forms

**Definition.** A **modular form** of weight $k \in \mathbb{Z}$ and level $1$ is a holomorphic function $f : \mathbb{H} \to \mathbb{C}$ on the upper half-plane satisfying

$$
f\!\left(\frac{az+b}{cz+d}\right) = (cz+d)^k f(z) \qquad \text{for all } \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in SL_2(\mathbb{Z}),
$$

together with the growth condition that $f$ is bounded as $z \to i\infty$ along vertical strips. The form is **cuspidal** if $f(z) \to 0$ as $z \to i\infty$; the space of modular forms of weight $k$ is denoted $M_k(SL_2(\mathbb{Z}))$ and the subspace of cusp forms $S_k(SL_2(\mathbb{Z}))$.

The transformation law is invariance of the function $\tilde f(g) = (ci+d)^{-k} f(g \cdot i)$ under $SL_2(\mathbb{Z})$, and the growth condition is the analytic part of the definition. The $q$-expansion $f(z) = \sum_{n\geq0} a_n q^n$, $q = e^{2\pi iz}$, converts the arithmetic into the coefficients $a_n$, and the finite-dimensionality of $M_k$ is the first structural theorem: $M_k = 0$ for odd $k$ and for $k<0$, and for even $k \geq 4$,

$$
\dim M_k = \begin{cases}\lfloor k/12\rfloor + 1, & k \not\equiv 2 \pmod{12}, \\ \lfloor k/12\rfloor, & k \equiv 2 \pmod{12},\end{cases}
$$

so that $\dim M_4 = \dim M_6 = \dim M_8 = \dim M_{10} = 1$ and $\dim M_{12} = 2$. The classical theory, including the congruence subgroups, the modular curves and the Petersson inner product, is not covered here.

### Hecke Operators

**Definition.** The **Hecke operator** $T_n$ on the space of modular forms acts on the $q$-expansion by

$$
(T_n f)(z) = n^{k-1}\sum_{ad=n} d^{-k}\sum_{b=0}^{d-1} f\!\left(\frac{az+b}{d}\right) = \sum_{m \geq 0} \left(\sum_{d \mid \gcd(m,n)} d^{k-1}\, a_{mn/d^2}\right) q^m,
$$

and the operators $T_n$ for $n \geq 1$ commute; they generate a commutative algebra, the **Hecke algebra**, acting on $M_k$ and preserving $S_k$.

The commutativity of the Hecke operators is the fundamental structural fact of the classical theory, and it has a conceptual proof: the operators $T_n$ are the adelic Hecke operators at the finite places, and the commutativity is the commutativity of the local Hecke algebras. A modular form that is an eigenfunction of all $T_n$ is a **Hecke eigenform**, and its eigenvalues $a_n$ (with the normalisation $a_1 = 1$) are multiplicative: $a_{mn} = a_m a_n$ for coprime $m,n$. The Euler product

$$
\sum_{n\geq1} a_n\, n^{-s} = \prod_p \left(1 - a_p p^{-s} + p^{k-1-2s}\right)^{-1}
$$

is the concrete form of the automorphic $L$-function, and the Ramanujan conjecture — $|a_p| \leq 2p^{(k-1)/2}$ — is the assertion that the local components are tempered.

## Automorphic Forms on $G(\mathbb{A})$

### The Adelic Setting

**Definition.** Let $G$ be a connected reductive group over $\mathbb{Q}$ and let $K \subseteq G(\mathbb{A})$ be a maximal compact subgroup. An **automorphic form** on $G$ is a function $f : G(\mathbb{Q})\backslash G(\mathbb{A}) \to \mathbb{C}$ satisfying

1. $f$ is smooth on the archimedean part and locally constant on the non-archimedean part (so that the right translates $f(\cdot k)$ span a finite-dimensional space for every $k \in K$, i.e. $f$ is $K$-finite);
2. $f$ is finite under the centre $\mathfrak{z}$ of the universal enveloping algebra of $\mathfrak{g}$, so that $f$ lies in a finite-dimensional space of eigenvectors of the Casimir-type operators;
3. $f$ is of moderate growth: there is a constant $C$ and an exponent $M$ with $|f(g)| \leq C\|g\|^M$ for all $g$;
4. when $G$ has a central character, $f$ transforms by a fixed character $\omega$ of $Z(\mathbb{Q})\backslash Z(\mathbb{A})$.

The group $G(\mathbb{A})$ acts on the space $\mathcal{A}(G)$ of automorphic forms by right translation, $(R(g)f)(x) = f(xg)$, and an **automorphic representation** is an irreducible subquotient of this representation. When $G = GL_2$ and $f$ is $Z(\mathbb{A})$-finite of central character $\omega$ and $K$-finite, the four conditions reduce to the classical ones: the functions on $GL_2(\mathbb{Q})\backslash GL_2(\mathbb{A})$ of fixed central character correspond to functions on $\mathbb{H}$ with a transformation law, and the finiteness under $\mathfrak{z}$ is the weight condition. The correspondence is made explicit by strong approximation, which is the statement of *Adeles and Ideles*.

**Definition.** An automorphic form $f$ is **cuspidal** if for every proper parabolic subgroup $P = MN$ of $G$ the constant term along $N$ vanishes:

$$
f_N(g) = \int_{N(\mathbb{Q})\backslash N(\mathbb{A})} f(ng)\, dn = 0.
$$

The cuspidal forms are square-integrable on the arithmetic quotient, and they are the analogue of the cusp forms of the classical theory. The constant term is the first term of the Fourier expansion of $f$ along the parabolic; the vanishing of all constant terms is the growth condition that rules out the Eisenstein series.

### The Space of Automorphic Forms

**Definition.** The **cuspidal spectrum** is the closed $G(\mathbb{A})$-invariant subspace $L^2_{cusp}$ of $L^2(G(\mathbb{Q})\backslash G(\mathbb{A}))$ spanned by the cuspidal automorphic forms, and the **residual spectrum** is the orthogonal complement in the discrete part, spanned by the residues of Eisenstein series.

The cuspidal spectrum decomposes discretely: $L^2_{cusp} = \bigoplus_\pi m(\pi)\, \pi$ with finite multiplicities $m(\pi)$, each $\pi$ an irreducible unitary representation of $G(\mathbb{A})$. This is the first instance of the general principle that the arithmetic quotient is a "spectral" object, and it is what makes the representation theory of $G(\mathbb{A})$ the right language.

**Theorem (multiplicity one for $GL_2$).** For $G = GL_2$ the cuspidal representation $\pi$ occurs in $L^2_{cusp}$ with multiplicity one: $m(\pi) \in \{0,1\}$. More generally, for $GL_n$ the multiplicity of a cuspidal automorphic representation in the discrete spectrum equals the order of the pole at $s=1$ of the relevant partial $L$-function, and for $GL_2$ the multiplicity is one because the cuspidal spectrum is simple.

**Theorem (strong multiplicity one; Jacquet–Shalika, Piatetski-Shapiro).** Let $\pi = \otimes'_v \pi_v$ and $\pi' = \otimes'_v \pi'_v$ be cuspidal automorphic representations of $GL_n(\mathbb{A})$. If $\pi_v \cong \pi'_v$ for all but finitely many places $v$, then $\pi = \pi'$.

Strong multiplicity one is the rigidity statement of the theory: an automorphic representation is determined by almost all of its local components. It is the reason the Hecke eigenvalues $a_p$ determine a classical eigenform, and it is the first of a family of rigidity results that culminate in the Langlands philosophy.

## The Structure of Automorphic Representations

### Tensor Products

**Theorem (flath's tensor product theorem).** Every irreducible admissible representation $\pi$ of $G(\mathbb{A})$ is a **restricted tensor product**

$$
\pi \cong \bigotimes_v' \pi_v,
$$

where $\pi_v$ is an irreducible admissible representation of $G(\mathbb{Q}_v)$ and, for all but finitely many places $v$, the local representation $\pi_v$ is **unramified**: it has a nonzero vector fixed by the hyperspecial maximal compact subgroup $K_v = G(\mathbb{Z}_v)$.

The restricted tensor product is the completion of the algebraic tensor product of the $\pi_v$ with respect to a family of unit vectors $u_v^0$ fixed by $K_v$ for almost all $v$; these vectors are the **spherical vectors**, and their choice makes the product well defined. The theorem reduces the global representation theory to the local one, one place at a time, and it is the structural reason the $L$-function of $\pi$ is a product of local factors.

**Definition.** The **level** of a cuspidal automorphic representation $\pi$ is the smallest $N$ such that $\pi$ has a vector fixed by the Hecke congruence subgroup of level $N$ on the non-archimedean part; the **conductor** is the corresponding local product. The **weight** is the archimedean parameter of the discrete series or principal series component of $\pi_\infty$.

The classical modular forms are recovered from the adelic picture by choosing the central character and the weight, and taking the subspace of vectors fixed by the congruence subgroup of level $N$; the $q$-expansion is the Fourier expansion along the unipotent radical of the Borel subgroup. Thus the classical theory and the adelic theory are the same theory seen at different levels of resolution, and the adelic version exposes the local factors that the classical version hides in the Hecke operators.

### Hecke Algebras and Spherical Representations

**Definition.** At a finite place $v = p$ the **spherical Hecke algebra** is $\mathcal{H}_p = \mathcal{H}(G(\mathbb{Q}_p), K_p)$ of compactly supported $K_p$-bi-invariant functions on $G(\mathbb{Q}_p)$ with the convolution product; it acts on the unramified local representation $\pi_p$ by integrating the action of $G(\mathbb{Q}_p)$ against the function.

**Theorem (Satake).** The Hecke algebra $\mathcal{H}_p$ is commutative, and the **Satake isomorphism** identifies it with the algebra of Weyl-invariant polynomial functions on the complex torus dual to the maximal torus:

$$
\mathcal{H}_p \cong \mathbb{C}[X_*(T)]^{W_v} \cong \mathbb{C}[A_1^{\pm1},\dots,A_n^{\pm1}]^{W},
$$

where $X_*(T)$ is the cocharacter lattice, $W_v$ the local Weyl group, and $n$ the rank. Consequently an unramified representation $\pi_p$ is determined by a **Satake parameter**, a semisimple conjugacy class $t_{\pi_p}$ in the Langlands dual group ${}^L G$.

The Satake parameter is the local datum that appears in the Euler factor of an automorphic $L$-function: the factor at $p$ is $\det(1 - t_{\pi_p} p^{-s} \mid V)^{-1}$ for the relevant representation $V$ of ${}^L G$. For $G = GL_2$ the Satake parameter is a diagonal matrix $\operatorname{diag}(\alpha_p, \beta_p)$ with $\alpha_p\beta_p = \omega(p)$ the central character, and the Euler factor is $(1-\alpha_p p^{-s})^{-1}(1-\beta_p p^{-s})^{-1}$, which after the substitution $a_p = p^{(k-1)/2}(\alpha_p+\beta_p)$ is the classical Euler product above.

**Corollary (classical Hecke operators as adelic Hecke operators).** The classical Hecke operator $T_n$ on modular forms is the adelic Hecke operator $\mathcal{H}_p$ at the places $p \mid n$, acting on the automorphic representation generated by the form. In particular the commutativity of the $T_n$ is the commutativity of the spherical Hecke algebras and the multiplicativity of the Hecke eigenvalues is the multiplicativity of the Satake parameters.

## The Spectral Decomposition

### Cuspidal, Residual and Continuous

**Theorem (spectral decomposition for $GL_2$).** The space $L^2(GL_2(\mathbb{Q})\backslash GL_2(\mathbb{A}), \omega)$ decomposes as a direct sum and integral

$$
L^2 = L^2_{cusp} \oplus L^2_{res} \oplus L^2_{cont},
$$

where $L^2_{cusp}$ is the cuspidal spectrum, $L^2_{res}$ is spanned by the residues of Eisenstein series, and $L^2_{cont}$ is the continuous spectrum spanned by the Eisenstein series $E(g, \varphi, s)$ for $\varphi$ in a space of automorphic forms on the Levi subgroup and $s$ on the critical line.

The decomposition is the analytic heart of the theory: it says that a general square-integrable automorphic form is a superposition of cuspidal forms, residues and Eisenstein series, and that the contribution of the Eisenstein series is indexed by the parameter $s$, which varies continuously. For $G = GL_1$ the decomposition reduces to the spectral theory of the multiplicative group, and the Eisenstein series becomes the classical zeta function; for $G = GL_2$ the constant term of an Eisenstein series produces the ratio of $L$-functions that gives the analytic continuation.

### Eisenstein Series

**Definition.** Let $P = MN$ be the standard Borel subgroup of $GL_2$ and let $\varphi$ be a cusp form on the Levi $M \cong GL_1 \times GL_1$ with a character parameter $s \in \mathbb{C}$. The **Eisenstein series** is

$$
E(g, \varphi, s) = \sum_{\gamma \in P(\mathbb{Q})\backslash G(\mathbb{Q})} \varphi(\gamma g)\, |a(\gamma g)|^{s+1/2},
$$

convergent for $\Re s > 1/2$ and continued meromorphically to $\mathbb{C}$ with a functional equation $E(g,\varphi,s) \leftrightarrow E(g, \varphi^\vee, -s)$.

The analytic continuation and the functional equation are proved by the theory of the constant term: the constant term of $E$ is $\varphi(g) + M(s)\varphi(g)$ with $M(s)$ an intertwining operator whose normalising factor is a ratio of local $L$-factors, and the functional equation of the Eisenstein series is the functional equation of that ratio. The poles of $M(s)$ give the residual spectrum and the residues $E(g,\varphi,s_0)$ are the residual automorphic forms. The classical Eisenstein series of the upper half-plane is the special case of the weight-zero form, and the analytic continuation of the zeta function is the case $G = GL_1$.

### The Trace Formula

**Theorem (Selberg's trace formula).** Let $G$ be a reductive group over $\mathbb{Q}$ and let $f$ be a test function on $G(\mathbb{A})$ of a suitable class. Then the trace of the operator $R(f)$ on the discrete part of $L^2(G(\mathbb{Q})\backslash G(\mathbb{A}))$ has two expansions,

$$
\operatorname{tr} R(f)\big|_{\mathrm{disc}} = \sum_{[\gamma]} \operatorname{vol}\!\left(G_\gamma(\mathbb{Q})\backslash G_\gamma(\mathbb{A})\right) O_\gamma(f) = \sum_{\pi} m(\pi)\, \operatorname{tr} \pi(f),
$$

the **geometric** expansion indexed by conjugacy classes $[\gamma]$ of $G(\mathbb{Q})$, with $G_\gamma$ the centraliser and $O_\gamma(f)$ the orbital integral, and the **spectral** expansion indexed by automorphic representations $\pi$ with multiplicities $m(\pi)$.

The trace formula is the identity that computes spectral data from geometric data, and it is the principal technical instrument of the theory. Selberg's version for $GL_2$ and its generalisation by Arthur to arbitrary reductive groups supply the Weyl law for the density of the cuspidal spectrum, the multiplicity formulas, the comparison of different groups that underlies functoriality, and the counting of automorphic representations of bounded conductor. The trace formula is the subject of a large body of literature and is stated here as the organising theorem; the details are not developed.

## $L$-Functions

### The Standard $L$-Function

**Definition.** Let $\pi = \otimes'_v \pi_v$ be a cuspidal automorphic representation of $GL_n(\mathbb{A})$ with Satake parameters $t_{\pi_p}$ at the unramified places. The **standard $L$-function** is the Euler product

$$
L(s, \pi) = \prod_p \det\!\left(1 - t_{\pi_p}\, p^{-s} \mid \mathbb{C}^n\right)^{-1},
$$

absolutely convergent for $\Re s$ large, and the **completed $L$-function** is

$$
\Lambda(s,\pi) = N_\pi^{s/2}\prod_{v \leq \infty} L_v(s,\pi_v),
$$

where $N_\pi$ is the **conductor** of $\pi$ — the product of the local conductors, equal to $1$ when $\pi$ is unramified — and the product includes the archimedean factors. The local factors at the ramified places and at infinity are defined by the local Langlands correspondence; for $GL_2$ the archimedean factor is a product of $\Gamma$-functions determined by the weight and the central character. The $L$-function is the analytic invariant of the automorphic representation, and its study is the arithmetic content of the theory.

**Theorem (functional equation).** For a cuspidal automorphic representation $\pi$ of $GL_n$ there is a **root number** $\varepsilon(\pi) \in \mathbb{C}^\times$ with $|\varepsilon(\pi)| = 1$ such that

$$
\Lambda(s, \pi) = \varepsilon(\pi)\, \Lambda(1-s, \tilde\pi),
$$

where $\tilde\pi$ is the contragredient representation. The completed $L$-function extends to a meromorphic function of $s$ of finite order, and it is entire when $\pi$ is cuspidal.

The functional equation is proved by Tate's thesis for $GL_1$ and by the theory of the zeta integrals for $GL_n$: one writes the $L$-function as the greatest common divisor of a family of local–global integrals $Z(s, f, \varphi) = \int_{G(\mathbb{Q})\backslash G(\mathbb{A})} f(g)\varphi(g)\, dg$ and proves the functional equation for the integrals, which transfers to the $L$-function. Tate's thesis is the case $G = GL_1$, in which the integrals are the classical adelic zeta integrals and the functional equation is the one of the Riemann zeta function; it is developed in *Adeles and Ideles*, where the adelic measure and the local Fourier analysis are constructed.

### Rankin–Selberg and the Arithmetic

For two cuspidal automorphic representations $\pi$ of $GL_n$ and $\pi'$ of $GL_m$ the **Rankin–Selberg convolution** $L(s, \pi \times \pi')$ is defined by an Euler product whose local factors are the local Rankin–Selberg factors, and the associated integral representation relates the analytic behaviour of the convolution to the inner product of the forms; the residue at $s=1$ measures the non-vanishing and is connected to the Petersson norm of the corresponding modular form. The general theory of these $L$-functions, their analytic continuation and their special values, is the subject andwhere the analytic theory is developed.

## Summary

An automorphic form on a reductive group $G$ over $\mathbb{Q}$ is a function on the arithmetic quotient $G(\mathbb{Q})\backslash G(\mathbb{A})$ that is $K$-finite, finite under the centre of the universal enveloping algebra, of moderate growth, and with a fixed central character. The space of such forms carries a representation of $G(\mathbb{A})$ by right translation, and an automorphic representation is an irreducible subquotient; the cuspidal automorphic forms are those with vanishing constant terms along every proper parabolic, and they are the square-integrable ones. By Flath's theorem every irreducible admissible representation of $G(\mathbb{A})$ is a restricted tensor product of local representations $\pi_v$, unramified at almost all places, and at each unramified place the representation is determined by a Satake parameter in the Langlands dual group through the Satake isomorphism of the spherical Hecke algebra.

The classical modular forms are the weight-and-level components of this picture, the classical Hecke operators are the adelic Hecke operators at the finite places, and the multiplicativity of the Hecke eigenvalues is the multiplicativity of the local parameters; strong multiplicity one says that an automorphic representation is determined by almost all its local components. The spectral decomposition of $L^2$ splits it into the cuspidal spectrum, the residual spectrum and the continuous spectrum of Eisenstein series, and Selberg's trace formula computes the discrete spectrum's multiplicities from the geometry of the conjugacy classes of $G(\mathbb{Q})$. The standard $L$-function of a cuspidal representation is an Euler product with the Satake parameters as coefficients, and it satisfies a functional equation with conductor and root number; Tate's thesis for $GL_1$ and the zeta integrals for $GL_n$ supply the analytic continuation. The general conjectural framework that organises the local parameters, the $L$-groups and the functorial transfer of representations is not covered here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{A} = \mathbb{A}_{\mathbb{Q}}$, $\mathbb{A}^\times$ | Adeles and ideles of $\mathbb{Q}$ |
| $v$, $\mathbb{Q}_v$ | A place of $\mathbb{Q}$ and the completion at it; $v=\infty$ gives $\mathbb{R}$, $v=p$ gives $\mathbb{Q}_p$ |
| $G$, $G(\mathbb{A})$, $G(\mathbb{Q})$ | Reductive group over $\mathbb{Q}$ and its adelic and rational points |
| $\Gamma = G(\mathbb{Z})$ | Arithmetic lattice |
| $K = \prod_v K_v$ | Maximal compact subgroup; $K_v = G(\mathbb{Z}_v)$ almost everywhere |
| $\mathcal{A}(G)$ | Space of automorphic forms |
| $R(g)$ | Right regular action, $(R(g)f)(x)=f(xg)$ |
| cuspidal | all constant terms $f_N$ vanish |
| $\mathfrak{z}$, $\mathfrak{g}$ | Centre of the universal enveloping algebra, Lie algebra of $G(\mathbb{R})$ |
| $Z$, $\omega$ | Centre of $G$ and a central character |
| $\pi = \otimes'_v \pi_v$ | Restricted tensor product of local representations |
| unramified, spherical | has a nonzero $K_v$-fixed vector; the $K_v$-fixed subspace |
| $t_{\pi_p}$ | Satake parameter, a semisimple class in ${}^L G$ |
| $\mathcal{H}_p$ | Spherical Hecke algebra, $\mathcal{H}(G(\mathbb{Q}_p),K_p)$ |
| $T_n$ | Classical Hecke operator |
| $M_k$, $S_k$ | Modular forms and cusp forms of weight $k$ |
| $L^2_{cusp}$, $L^2_{res}$, $L^2_{cont}$ | Cuspidal, residual and continuous spectra |
| $E(g,\varphi,s)$ | Eisenstein series |
| $L(s,\pi)$, $\Lambda(s,\pi)$ | Standard and completed $L$-function |
| $N_\pi$, $\varepsilon(\pi)$ | Conductor and root number of $\pi$ |
| $\pi \times \pi'$ | Rankin–Selberg convolution |







## Further Reading

- Goro Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions* (Princeton University Press, 1971), for the classical theory of modular forms and Hecke operators.
- André Weil, *Adeles and Algebraic Groups* (Birkhäuser, 1982), and J. T. Tate, "Fourier analysis in number fields and Hecke's zeta-functions", in *Algebraic Number Theory* (Academic Press, 1967), for the adelic setting and Tate's thesis.
- Daniel Bump, *Automorphic Forms and Representations* (Cambridge University Press, 1997), for a unified account of the classical and adelic theories.
- Armand Borel and Hervé Jacquet, "Automorphic forms and automorphic representations", in *Automorphic Forms, Representations and $L$-Functions* (AMS, 1979), for the definitions and the tensor product theorem.
- Hervé Jacquet and Joseph Shalika, "On Euler products and the classification of automorphic representations I, II", *American Journal of Mathematics* 103 (1981), 499–558 and 777–815, for strong multiplicity one and the $L$-functions.
- Hervé Jacquet and Robert P. Langlands, *Automorphic Forms on $GL(2)$* (Springer Lecture Notes 114, 1970), for the spectral decomposition and the Eisenstein series.
- Ichirō Satake, "Theory of spherical functions on reductive algebraic groups over $p$-adic fields", *Publications Mathématiques de l'IHÉS* 18 (1963), 5–69, for the Satake isomorphism.
- James Arthur, *The Endoscopic Classification of Representations: Orthogonal and Symplectic Groups* (AMS, 2013), and A. B. Venkov, "The spectral theory of automorphic functions", for the trace formula and the Weyl law.
- D. A. Hejhal, *The Selberg Trace Formula for $PSL(2,\mathbb{R})$* (Springer Lecture Notes 548 and 1001, 1976 and 1983), for the trace formula in the rank-one case.
