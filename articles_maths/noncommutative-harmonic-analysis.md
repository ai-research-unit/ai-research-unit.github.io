
# __Noncommutative Harmonic Analysis__

## Introduction

For a locally compact abelian group the Fourier transform is a scalar-valued function on a dual **group**, and the whole theory — inversion, Plancherel, the convolution theorem, the Gelfand picture — rests on that. For a general locally compact group none of this survives unchanged. The convolution algebra $L^1(G)$ is non-commutative, so it has no Gelfand transform; the equivalence classes of irreducible unitary representations form a set $\operatorname{Irr}(G)$ that need not be a group and may be a wildly non-separable object; and the transform of a function is an operator-valued field on $\operatorname{Irr}(G)$ rather than a function. Noncommutative harmonic analysis is the theory that replaces the missing dual group by the unitary dual, the missing Gelfand transform by the operator-valued transform, and the missing decomposition of $C_0(G^\vee)$ by the direct-integral decomposition of $L^2(G)$. The result is the same analysis, rewritten in the language of operator algebras and fibre spaces over the dual.

The article develops that replacement. It begins with the three failures — non-commutativity, the non-group dual, and the wild dual for groups that are not of type I — then develops the operator-valued transform and the coefficient algebra, the direct-integral decomposition of the regular representation, the operator-algebraic picture through the group $\mathrm{C}^*$-algebras and the group von Neumann algebra, the noncommutative form of the Gelfand theory, and the standard examples. The Plancherel theorem, which is the quantitative core of the decomposition, has its own article,and the compact case has *Analysis on Compact Groups* and *The Peter–Weyl Theorem*; the present article is the general frame in which both sit.

The boundaries. The **representation theory** of locally compact groups — unitary representations, irreducibility, intertwiners, induced representations, Mackey theory, the unitary dual as an object, type I groups and the Borel structure of the dual, property (T), weak containment — is Part II's: *Representation Theory of Locally Compact Groups*, *Induced Representations of Locally Compact Groups*, *Mackey Theory*, *Type I Groups* and *Property (T)*. Their statements are used here as established facts, and the analysis built on them is here. The **Haar measure** is *Locally Compact Groups and Haar Measure*, the **integration theory and the $L^p$ theory** are *Measure Theory and Integration* and *Modes of Convergence*, and the **operator algebras** are *Operator Algebras*, the underlying Banach- and Hilbert-space theory being standard and quoted as it is used and developed. The **convolution algebra**, its involution, its approximate identities and its completions are *The Convolution Algebra $L^1(G)$*, and the **abelian** theory is *Harmonic Analysis on Groups*. The vector-valued integration used throughout is taken as given, and the direct integrals are the standard disintegration of a von Neumann algebra over its centre, treated in *Operator Algebras*. No physics is invoked.

Throughout, $G$ is a locally compact Hausdorff group with left Haar measure $dx$, modular function $\Delta$ and identity $e$; it is **unimodular** when $\Delta \equiv 1$, and the operator-valued theory is stated for unimodular $G$ except where a statement is explicitly general. The convolution and involution are those of *The Convolution Algebra $L^1(G)$*:

$$
(f*g)(x) = \int_G f(y)g(y^{-1}x)\,dy , \qquad f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1} .
$$

The abelian dual is $G^\vee$ and the unitary dual — the set of equivalence classes of irreducible unitary representations — is $\operatorname{Irr}(G)$; for $\pi \in \operatorname{Irr}(G)$ the space is $\mathcal{H}_\pi$, the transform is $\hat f(\pi) = \int_G f(g)\pi(g)\,dg$, and the matrix coefficients are $c^\pi_{\xi,\eta}(g) = \langle\pi(g)\xi,\eta\rangle$. The reduced and full group $\mathrm{C}^*$-algebras are $C^*_r(G)$ and $C^*(G)$, and the group von Neumann algebra is $L(G) = \lambda(G)''$. The hat is never used for a dual.

## The Failure of the Commutative Framework

### $L^1(G)$ is Not Commutative

**Theorem.** $L^1(G)$ is commutative if and only if $G$ is abelian, and if $G$ is non-abelian then $L^1(G)$ has no nonzero complex homomorphism into $\mathbb{C}$ unless $G$ has an abelian quotient of finite or infinite index — in particular, the Gelfand spectrum of $L^1(G)$ is the set of characters of $G$ and sees only the abelianisation $G/[G,G]$.

**Proof.** If $G$ is abelian, the substitution $y \mapsto xy^{-1}$ gives $f*g = g*f$. If $G$ is non-abelian, choose $x, y \in G$ with $xy \neq yx$ and approximate the point masses at $x$, $y$; the corresponding functions do not commute. A complex homomorphism $h$ of $L^1(G)$ extends to a one-dimensional representation of $G$ through the correspondence of *The Convolution Algebra $L^1(G)$*, §Representations and Completions, and hence is a character; characters factor through the commutator subgroup, so the Gelfand spectrum is the character group of the abelianisation. $\square$

For $G = S_3$ the Gelfand spectrum is the two-element group $S_3/[S_3,S_3] \cong \mathbb{Z}/2$, while the unitary dual has three elements, one of dimension $2$. The Gelfand transform therefore loses the representation of dimension $2$, and with it the whole of the non-abelian analysis; the operator-valued transform of the next section is what recovers it.

### The Dual Is Not a Group

For a non-abelian group the unitary dual $\operatorname{Irr}(G)$ carries no group structure: the tensor product of two irreducible representations is generally a direct sum, so the "product" of two classes is set-valued, and there is no Pontryagin-type duality. The dual is a set with a topology — the **Fell topology**, the weakest topology making the matrix coefficients continuous in the appropriate sense — and, for second countable $G$, a Borel structure.

**Definition.** Let $G$ be second countable and locally compact. The **Mackey Borel structure** on $\operatorname{Irr}(G)$ is the smallest $\sigma$-algebra for which all maps $\pi \mapsto \operatorname{Tr}(\hat f(\pi))$, $f \in L^1(G)$, are measurable. The group is **of type I** if this Borel structure is countably separated, equivalently if the equivalence relation of unitary equivalence on $\operatorname{Irr}(G)$ is smooth.

The theory of this Borel structure, of the equivalence of type I with the countable separation, and of the examples is *Type I Groups*, and is quoted. What matters here is the consequence: type I is exactly the hypothesis under which the decomposition of the regular representation is indexed by $\operatorname{Irr}(G)$ with a measurable multiplicity function, and hence under which a Plancherel theorem exists.

**Example ($SU(2)$ and the tensor product).** The dual of $K = SU(2)$ is $\{V_j : j \in \frac{1}{2}\mathbb{Z}_{\geq 0}\}$ with $d_j = 2j+1$, and $V_j\otimes V_l = \bigoplus_{m=|j-l|}^{j+l}V_m$; the "product" is multivalued, and the Clebsch–Gordan multiplicities are all $0$ or $1$. The dual is a discrete set with a tensor structure, not a group, and this is exactly the case in which the compact theory of *Analysis on Compact Groups* replaces the dual group by the dual set. For an abelian group the same tensor product is $V_\chi\otimes V_\psi = V_{\chi\psi}$ with multiplicity one, and the set is the group; so the group structure of the abelian dual is the special feature, not the general one.

### The Wild Dual: The Free Group

Type I can fail, and the fundamental example is the free group on two generators $F_2$. By *Type I Groups*, §Examples and Non-Examples: $\operatorname{Irr}(F_2)$ is not countably separated; there is a Borel set of cardinality continuum of pairwise inequivalent irreducibles; the regular representation is not a direct integral of irreducibles; and the group von Neumann algebra $L(F_2)$ is a factor of type $\mathrm{II}_1$, not a direct sum of type I factors. The dual is a wild object, and its description is a problem in the theory of operator algebras and of Borel equivalence relations rather than in commutative analysis. This is the boundary of the present theory: everything below holds for type I groups and is false in general.

## The Operator-Valued Transform

### Definition and the Convolution Theorem

**Definition.** For $f \in L^1(G)$ and a unitary representation $\pi$ of $G$ on $\mathcal{H}_\pi$, the **Fourier transform** of $f$ at $\pi$ is

$$
\hat f(\pi) = \int_G f(g)\,\pi(g)\,dg \in B(\mathcal{H}_\pi),
$$

the integral converging in the norm of $B(\mathcal{H}_\pi)$ because $\|\pi(g)\| = 1$ and $f \in L^1(G)$, with $\|\hat f(\pi)\| \leq \|f\|_1$. For $\pi$ irreducible the operator $\hat f(\pi)$ is the noncommutative "value of the transform" at the point $\pi$ of the dual.

**Theorem (convolution theorem).** For $f, h \in L^1(G)$ and every unitary representation $\pi$,

$$
\widehat{f*h}(\pi) = \hat f(\pi)\,\hat h(\pi), \qquad \widehat{f^*}(\pi) = \hat f(\pi)^* .
$$

*Proof.* Same computation as in the abelian and compact cases: substitute $x = yz$ and use left invariance and multiplicativity. The involution statement uses the modular factor in $f^*$ and the unitarity of $\pi$. $\square$

Thus the transform is a $*$-homomorphism of the Banach $*$-algebra $L^1(G)$ into the algebra of operator fields on the dual with pointwise multiplication, and it is exactly the integrated form of the representation correspondence of *The Convolution Algebra $L^1(G)$*, §Representations and Completions.

### Matrix Coefficients and Functions of Positive Type

**Definition.** A **matrix coefficient** of the unitary representation $\pi$ is the continuous function $c^\pi_{\xi,\eta}(g) = \langle\pi(g)\xi,\eta\rangle$. A continuous function $\varphi$ on $G$ is **of positive type** if $\sum_{i,j}c_i\overline{c_j}\varphi(x_j^{-1}x_i) \geq 0$ for every finite family and every choice of coefficients.

**Theorem (Godement).** A continuous function $\varphi$ on $G$ is of positive type if and only if there is a unitary representation $\pi$ of $G$ and a vector $\xi \in \mathcal{H}_\pi$ with $\varphi(g) = c^\pi_{\xi,\xi}(g)$; the representation may be taken cyclic with $\xi$ cyclic, and then it is unique up to unitary equivalence (the GNS construction). Every matrix coefficient is a linear combination of four functions of positive type, and a function of positive type satisfies $\varphi(e) = \|\varphi\|_\infty$, $\varphi(g^{-1}) = \overline{\varphi(g)}$ and $\|\varphi\|_\infty = \|\varphi\|_{C^*}$.

**Proof sketch.** Given $\varphi$ of positive type, the sesquilinear form on $C_c(G)$ given by $\langle f,h\rangle_\varphi = \int\int f(x)\overline{h(y)}\varphi(y^{-1}x)\,dx\,dy$ is positive semidefinite; completing and factoring gives a Hilbert space, the group acts unitarily by left translation because of the invariance of the kernel, and the class of an approximate identity concentrated near $e$ is the cyclic vector $\xi$ whose associated coefficient is $\varphi$. Conversely a diagonal coefficient is of positive type because $\sum c_i\overline{c_j}\langle\pi(x_j^{-1}x_i)\xi,\xi\rangle = \|\sum_i c_i\pi(x_i)\xi\|^2 \geq 0$. Uniqueness is the standard uniqueness in the GNS construction. This is the noncommutative form of Bochner's theorem; in the abelian case the cyclic representations are the characters and the theorem reduces to *Harmonic Analysis on Groups*, §Positive-Definite Functions and Bochner's Theorem. $\square$

**Corollary (the noncommutative Bochner theorem).** The functions of positive type are the "noncommutative Fourier–Stieltjes transforms": each is the diagonal matrix coefficient of a cyclic unitary representation, and the correspondence is a bijection up to unitary equivalence. The measure of the abelian theorem has become the representation.

### The Coefficient Algebra

**Definition.** The **coefficient space** of $G$ is the linear span of the matrix coefficients of all continuous unitary representations; its elements are the functions of the form $g \mapsto \operatorname{Tr}(\pi(g)A)$ with $\pi$ finite-dimensional or with $A$ of finite rank.

**Theorem.** The coefficient space is an algebra under pointwise multiplication and under convolution, it is invariant under left and right translation and under the involution $f \mapsto f^*$, and it is dense in $C_0(G)$ in the uniform norm; for $G$ compact it is dense in $C(G)$ and its completion is the algebra of *Analysis on Compact Groups*. The transform identifies the completion of $L^1(G)$ acting on this space with the algebra of operator fields.

**Proof.** Products of coefficients are coefficients of tensor products; conjugates are coefficients of contragredient representations; translation invariance and the convolution statement follow from the representation identities; density is the Stone–Weierstrass argument when $G$ is compact and the general analogue for $G$ of type I. $\square$

## The Decomposition of the Regular Representation

### The Direct Integral over the Dual

The central structural theorem of noncommutative harmonic analysis is that the regular representation decomposes as a direct integral over the unitary dual, with the Plancherel measure as the measure and the dimension as the multiplicity. The precise statement needs the direct-integral calculus of von Neumann algebras.

**Theorem (abstract decomposition).** Let $G$ be a second countable unimodular group of type I. Then there is a unique (up to equivalence) Radon measure $\mu_P$ on $\operatorname{Irr}(G)$, the **Plancherel measure**, and a measurable field $\pi \mapsto \mathcal{H}_\pi$ of Hilbert spaces, such that the left regular representation is unitarily equivalent to the direct integral

$$
\lambda \;\cong\; \int_{\operatorname{Irr}(G)}^{\oplus} \bigl(\pi \otimes \pi^*\bigr)\, d\mu_P(\pi) ,
\qquad\text{equivalently}\qquad
\lambda \;\cong\; \int_{\operatorname{Irr}(G)}^{\oplus} d_\pi\,\pi\, d\mu_P(\pi),
$$

where $d_\pi = \dim\mathcal{H}_\pi$ is the multiplicity function and $d_\pi$ is finite $\mu_P$-almost everywhere. The measure and the multiplicity function are unique up to $\mu_P$-null sets. This is the special case, for the group algebra, of the general direct-integral decomposition of a representation of a type I $\mathrm{C}^*$-algebra, quoted from *Type I Groups*, §Uniqueness of Decomposition.

**Remark (the measure is determined by the trace).** The Plancherel measure is determined by the requirement that the trace of the group von Neumann algebra be integration against it; this fixes $\mu_P$ uniquely once the normalisation of the Haar measure is fixed, exactly as the dual Haar measure is fixed by inversion in the abelian case. The explicit form of $\mu_P$ for the standard groups is.

### Central Decomposition and Multiplicities

Because $\lambda$ and $\rho$ commute, the algebra generated by the regular representation is a von Neumann algebra with a large centre, and the direct integral above is its **central decomposition**: the dual is the spectrum of the centre, and the multiplicity function is the dimension of the fibre.

**Theorem (the group von Neumann algebra of a type I group).** For $G$ unimodular of type I,

$$
L(G) = \lambda(G)'' \;\cong\; \int_{\operatorname{Irr}(G)}^{\oplus} B(\mathcal{H}_\pi)\,d\mu_P(\pi) ,
$$

a direct integral of type I factors, with centre $Z(L(G)) \cong L^\infty(\operatorname{Irr}(G),\mu_P)$ and faithful normal semifinite trace

$$
\tau(a) = \int_{\operatorname{Irr}(G)} \operatorname{Tr}\bigl(a(\pi)\bigr)\,d\mu_P(\pi) .
$$

The representation $\lambda$ is the image of the identity field under this isomorphism, and the multiplicity $d_\pi$ of the irreducible $\pi$ in $\lambda$ is the dimension of the fibre $\mathcal{H}_\pi$; the integrand is zero only for $\pi$ outside the support of $\mu_P$.

**Proof.** The commutant of the direct integral of the $\pi$ is the direct integral of the commutants, and each commutant is $\mathbb{C}1$ because $\pi$ is irreducible; hence the algebra generated is the whole direct integral of $B(\mathcal{H}_\pi)$, which is the identity $\lambda(G)' = \rho(G)''$ and hence, by taking commutants, $L(G) = \rho(G)' = \int^\oplus B(\mathcal{H}_\pi)d\mu_P$. The centre is the algebra of scalar fields, namely $L^\infty(\operatorname{Irr}(G),\mu_P)$, and the trace is the integral of the operator trace, finite for the integrable fields. $\square$

**Remark (the abelian and compact cases).** For abelian $G$, $d_\pi = 1$ for all $\pi$, $B(\mathcal{H}_\pi) = \mathbb{C}$, and the direct integral is the spectral representation of the algebra $L^\infty(G^\vee,\mu_P)$ with $\mu_P = d\chi$ the dual Haar measure; this is the Fourier transform of *Harmonic Analysis on Groups*. For compact $G$, the dual is discrete, the measure is the weighted counting measure $d\mu_P = d_\pi\,\#$, the direct sum is $\bigoplus_\pi\operatorname{End}(\mathcal{H}_\pi)$, and the theory is *The Peter–Weyl Theorem*, §Consequences.

### The Non-Type-I Case: $F_2$ and the Type $\mathrm{II}_1$ Factor

For $G = F_2$ the decomposition fails at its first step: there is no measure on $\operatorname{Irr}(F_2)$ for which $\lambda$ is a direct integral of irreducibles, because the dual is not countably separated. The regular representation still decomposes as a direct integral of **factor representations** over a standard Borel space, and the algebra $L(F_2)$ is a factor of type $\mathrm{II}_1$ with its unique normalised trace $\tau(a) = \langle a\delta_e,\delta_e\rangle$; the decomposition is into factors of type $\mathrm{II}_1$ rather than into type I factors, and it is the central decomposition of that factor. The operator-algebraic theory is *Operator Algebras*, §Factors and the Classification into Types; what matters here is that the noncommutative analysis survives the failure of type I only in the weaker form of the factor decomposition, and that no Plancherel formula of the stated kind can hold.

## The Operator-Algebraic Picture

### The Group $\mathrm{C}^*$-Algebras and the Spectrum

The noncommutative replacement for the Gelfand spectrum of a commutative Banach algebra is the **spectrum** of a $\mathrm{C}^*$-algebra: the set $\operatorname{Irr}(A)$ of equivalence classes of irreducible $*$-representations with the Fell topology. For $A = C^*(G)$ the spectrum is the unitary dual $\operatorname{Irr}(G)$, by the correspondence between nondegenerate $*$-representations of $L^1(G)$ and unitary representations of $G$ established in *The Convolution Algebra $L^1(G)$*, so that

$$
\operatorname{Irr}\bigl(C^*(G)\bigr) = \operatorname{Irr}(G) ,
\qquad
\operatorname{Irr}\bigl(C^*_r(G)\bigr) \subseteq \operatorname{Irr}(G),
$$

the inclusion being an equality exactly in the amenable case. The Gelfand–Naimark theorem, which for a commutative $\mathrm{C}^*$-algebra gives $A \cong C_0(\operatorname{Prim}(A))$, becomes for a general $A$ the statement that $A$ is the completion of its image in the universal representation, i.e. that $A$ acts faithfully on the Hilbert space direct sum of its irreducible representations. This is the **noncommutative Gelfand theory**: the primitive ideal space $\operatorname{Prim}(A)$, the space of kernels of irreducible representations, replaces the maximal ideal space, and for separable type I $A$ it is a standard Borel space with a canonical Borel isomorphism to $\operatorname{Irr}(A)$.

**Theorem (noncommutative Gelfand–Naimark).** A $\mathrm{C}^*$-algebra $A$ is commutative if and only if every irreducible representation is one-dimensional; in that case $A \cong C_0(\operatorname{Prim}(A))$. For general $A$, the map $A \to \bigoplus_{\pi\in\operatorname{Irr}(A)}\pi(A)$ is an isometric $*$-isomorphism onto its image, so $A$ is recovered from its spectrum. Consequently the harmonic analysis of $G$ is exactly the spectral theory of the $\mathrm{C}^*$-algebra $C^*(G)$.

**Proof.** The first statement is Gelfand–Naimark and Schur's lemma: irreducibles of a commutative $\mathrm{C}^*$-algebra are the characters. The isometric embedding is the Gelfand–Naimark–Segal construction applied to the universal representation, which is faithful. $\square$

### Weak Containment and Amenability

**Definition.** For unitary representations $\sigma, \pi$ of $G$, $\sigma$ is **weakly contained** in $\pi$, written $\sigma \prec \pi$, if every positive-definite function associated with $\sigma$ is a limit, uniformly on compacta, of sums of positive-definite functions associated with $\pi$; equivalently, $\ker\pi \subseteq \ker\sigma$ on $C^*(G)$.

**Theorem (Hulanicki).** A locally compact group $G$ is amenable if and only if the trivial representation is weakly contained in the regular representation, $\mathbf{1} \prec \lambda$.

**Proof sketch.** If $\mathbf{1} \prec \lambda$, then the constant function $1$ is a limit of sums of coefficients of $\lambda$, and integrating against an invariant mean constructed from these coefficients gives amenability; the translation of the condition into Reiter's property $P_1$ is immediate. Conversely, amenability gives approximately invariant unit vectors $\xi_\alpha \in L^2(G)$ (the square roots of the Reiter functions of *The Convolution Algebra $L^1(G)$*, §Reiter's Property and Amenability), and the associated coefficient $\langle\lambda(g)\xi_\alpha,\xi_\alpha\rangle$ of $\lambda$ converges uniformly on compacta to $1$, which is the coefficient of the trivial representation. This is Hulanicki's theorem and is quoted. $\square$

**Corollary (the spectral gap of a (T) group).** If $G$ has property (T), then $\mathbf{1}$ is not weakly contained in $\lambda$, and there is a neighbourhood $Q$ of $e$ and $\varepsilon > 0$ with $\sup_{g\in Q}\|\lambda(g)\xi - \xi\| \geq \varepsilon\|\xi\|$ for every $\xi \in L^2(G)$ orthogonal to the constants; equivalently $\|\lambda(f)\| < \|f\|_1$ for suitable $f$. This is the spectral gap used for expanders in *Property (T)* and for the ergodic theorems.

### The Coefficient Transform as a Noncommutative $L^\infty$

The map $f \mapsto (\hat f(\pi))_\pi$ sends $L^1(G)$ onto a dense subalgebra of the algebra of fields of operators; the closure in the appropriate norm is $C^*(G)$, and the weak closure is $L(G) = \int^\oplus B(\mathcal{H}_\pi)d\mu_P$. Under this correspondence:

- $L^1(G)$ corresponds to the integrable operator fields $\int\|\hat f(\pi)\|_1\,d\mu_P(\pi) < \infty$ up to the ambiguity of the transform's kernel;
- $C^*(G)$ or $C^*_r(G)$ corresponds to the fields vanishing at infinity in the Fell sense;
- $L(G)$ corresponds to the essentially bounded measurable operator fields, $L^\infty(\operatorname{Irr}(G),\mu_P)$ in the sense of direct integrals;
- the centre $Z(L(G))$ corresponds to the scalar fields, and $\operatorname{Irr}(G)$ is its spectrum.

This dictionary is the exact noncommutative analogue of the chain $L^1(G) \subset C^*_r(G) \subset L^\infty(G^\vee)$ of the abelian case, and it is the organising principle of the whole block.

## The Standard Examples

### The Heisenberg Group

Let $H$ be the three-dimensional Heisenberg group with the multiplication $(x,y,z)(x',y',z') = (x+x', y+y', z+z'+xy')$. It is a connected nilpotent Lie group, hence unimodular and of type I. Its unitary dual consists of the characters of the abelianisation, parametrised by $\mathbb{R}^2$, together with one infinite-dimensional representation $\pi_\lambda$ for each $\lambda \in \mathbb{R}\smallsetminus\{0\}$, the **Schrödinger representation** on $L^2(\mathbb{R})$,

$$
\pi_\lambda(x,y,z)\xi(t) = e^{2\pi i \lambda(z + ty)}\xi(t+x),
$$

which by the Stone–von Neumann theorem is the unique irreducible representation with central character $e^{2\pi i\lambda z}$. The Plancherel measure is supported on the infinite-dimensional part , with the Haar measure normalised as in the formula above, has density proportional to $|\lambda|\,d\lambda$; this is the explicit form of the abstract theorem of the previous section, and its derivation is.

### $SL_2(\mathbb{R})$

The group $SL_2(\mathbb{R})$ is unimodular, connected semisimple and of type I (Harish-Chandra). Its unitary dual consists of the **principal series** $\pi_{it,\varepsilon}$, $t \in \mathbb{R}$, $\varepsilon \in \{0,1\}$, induced from the upper triangular subgroup; the **complementary series**, an interval of parameters for which the induced representation remains irreducible and unitarisable; and the **discrete series** $D_n$, $n \geq 1$, of positive formal degree. The Plancherel measure is absolutely continuous on the principal series with density $t\tanh(\pi t)$ on the spherical part and $t\coth(\pi t)$ on the sign part, together with a sum of point masses at the discrete series; this is Harish-Chandra's explicit Plancherel formula, quoted from the literature and treated. The decomposition of $L^2(SL_2(\mathbb{Z})\backslash SL_2(\mathbb{R}))$ into a discrete spectrum (Maass forms and holomorphic forms) and a continuous spectrum (Eisenstein series) is the first instance of the automorphic spectral theory.

### Compact Groups

For compact $K$ the dual is discrete, the Plancherel measure is the weighted counting measure, and the decomposition is the Peter–Weyl direct sum; the entire theory is the content of *Analysis on Compact Groups* and *The Peter–Weyl Theorem*, and it is the case in which every statement of the present article is fully explicit.

### Semidirect Products and the Mackey Machine

For a semidirect product $G = N \rtimes Q$ with $N$ abelian, the dual is computed by the **Mackey machine**: the irreducible unitary representations are classified by the orbits of $Q$ on the dual $N^\vee$, the little-group representations and the induction, and the analysis inherits the structure of a fibre space over the orbit space $N^\vee/Q$. The classification is Part II's (*Mackey Theory* and *Induced Representations of Locally Compact Groups*); what the present article adds is the analytic reading: the Plancherel measure of the semidirect product is computed from the decomposition of the orbits and the Plancherel measures of the little groups, and the transform is the corresponding fibre-wise transform. The Heisenberg group and the affine group are the smallest non-trivial instances, the former type I and the latter non-unimodular; the affine group is of type I by the Auslander–Kostant theorem for simply connected solvable groups, but it is non-unimodular, so the unimodular Plancherel theory of the previous sections does not apply to it; it is used throughout the block as the standard warning that the unimodularity hypothesis is not automatic.

## Summary

Noncommutative harmonic analysis replaces the dual group of the abelian theory by the unitary dual $\operatorname{Irr}(G)$, the scalar Gelfand transform by the operator-valued transform $\hat f(\pi) = \int_G f(g)\pi(g)\,dg$, which satisfies $\widehat{f*h}(\pi) = \hat f(\pi)\hat h(\pi)$ and $\widehat{f^*}(\pi) = \hat f(\pi)^*$, and the decomposition of $L^2(G)$ into characters by a direct integral over the dual with respect to the Plancherel measure. The three failures of the commutative frame are the non-commutativity of $L^1(G)$, the loss of a group structure on the dual — visible already for $S_3$ and $SU(2)$ — and the wildness of the dual for non-type-I groups, exhibited by $F_2$, whose group von Neumann algebra is a type $\mathrm{II}_1$ factor and whose regular representation is not a direct integral of irreducibles. For a unimodular type I group the regular representation is $\lambda \cong \int^\oplus(\pi\otimes\pi^*)d\mu_P(\pi)$, the multiplicity of $\pi$ being $d_\pi = \dim\mathcal{H}_\pi$, and the group von Neumann algebra is $L(G) = \int^\oplus B(\mathcal{H}_\pi)d\mu_P$, a direct integral of type I factors with centre $L^\infty(\operatorname{Irr}(G),\mu_P)$ and trace $\tau(a) = \int\operatorname{Tr}(a(\pi))d\mu_P(\pi)$; this central decomposition is the noncommutative analogue of the Fourier representation, with the abelian and compact cases as the two exactly computable ends. The representational content is organised by the GNS and Godement theorems — the functions of positive type are the diagonal matrix coefficients, which is the noncommutative Bochner theorem — and by the correspondence between nondegenerate $*$-representations of $L^1(G)$ and unitary representations of $G$, which identifies $\operatorname{Irr}(C^*(G))$ with $\operatorname{Irr}(G)$ and makes noncommutative harmonic analysis the spectral theory of the group $\mathrm{C}^*$-algebra. The sharp criterion at the boundary of the theory is Hulanicki's: $G$ is amenable if and only if the trivial representation is weakly contained in the regular representation, with property (T) giving the opposite spectral gap. The standard examples are the Heisenberg group, with its Schrödinger representation and Plancherel density $|\lambda|$; $SL_2(\mathbb{R})$, with principal, complementary and discrete series and Harish-Chandra's Plancherel formula; the compact groups, where the direct integral becomes the Peter–Weyl direct sum; and the semidirect products, where the Mackey machine supplies the fibre structure of the dual.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $dx$, $\Delta$, $e$ | Locally compact group, left Haar measure, modular function, identity |
| $\operatorname{Irr}(G)$ | Unitary dual, with the Fell topology |
| $\mathcal{H}_\pi$ | Hilbert space of the representation $\pi$ |
| $\hat f(\pi) = \int_G f(g)\pi(g)\,dg$ | Operator-valued Fourier transform |
| $c^\pi_{\xi,\eta}(g) = \langle\pi(g)\xi,\eta\rangle$ | Matrix coefficients |
| positive type | $\sum_{i,j}c_i\overline{c_j}\varphi(x_j^{-1}x_i)\geq0$ |
| $\mu_P$ | Plancherel measure on $\operatorname{Irr}(G)$ |
| $d_\pi = \dim\mathcal{H}_\pi$ | Dimension/multiplicity function |
| $\int^\oplus$ | Direct integral of Hilbert spaces or von Neumann algebras |
| $L(G) = \lambda(G)'' = \rho(G)'$ | Group von Neumann algebra |
| $\tau(a) = \int\operatorname{Tr}(a(\pi))\,d\mu_P(\pi)$ | Trace on $L(G)$ |
| $C^*(G)$, $C^*_r(G)$ | Full and reduced group $\mathrm{C}^*$-algebras |
| $\operatorname{Prim}(A)$ | Primitive ideal space (noncommutative spectrum) |
| $\sigma \prec \pi$ | Weak containment of representations |
| $\pi_\lambda$ | Schrödinger representation of the Heisenberg group |
| $\pi_{it,\varepsilon}$, $D_n$ | Principal and discrete series of $SL_2(\mathbb{R})$ |
| $F_2$ | Free group on two generators; non-type-I example |
| $\lvert\lambda\rvert\,d\lambda$ | Heisenberg Plancherel density (normalisation-dependent) |



## Further Reading

- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, 2nd ed. 2015), for the operator-valued transform, the coefficient algebra and the group $\mathrm{C}^*$-algebras.
- Jacques Dixmier, *$\mathrm{C}^*$-Algebras* (North-Holland, 1977), for the spectrum, the primitive ideal space and the type I decomposition of a representation.
- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for the direct-integral decomposition and the group von Neumann algebra.
- George W. Mackey, *The Theory of Unitary Group Representations* (Chicago, 1976), for the dual object, the Borel structure and the Mackey machine.
- Robert J. Zimmer, *Ergodic Theory and Semisimple Groups* (Birkhäuser, 1984), for the spectral-gap and weak-containment consequences used in ergodic theory.
- A. A. Kirillov, *Elements of the Theory of Representations* (Springer, 1976), for the orbit method and the classification of the dual of nilpotent groups.
- Anthony W. Knapp, *Representation Theory of Semisimple Groups* (Princeton, 1986), for the principal, complementary and discrete series and the Harish-Chandra Plancherel formula.
- M. A. Naimark, *Normed Algebras* (Wolters-Noordhoff, 1972), for the Banach $*$-algebra foundations of the noncommutative transform.
- Walter Rudin, *Functional Analysis* (McGraw–Hill, 2nd ed. 1991), for the Hilbert-space spectral theory, the compact and Hilbert–Schmidt operators and the Banach-algebra foundations quoted as standard.
