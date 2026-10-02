
# __The Group Algebra as an Algebra of Operators__

## Introduction

The group algebra $L^1(G)$ multiplies its own elements by convolution, and that single fact makes it an algebra of operators in two senses at once: it acts on itself, the left and the right multiplications of *Convolution on a Group*, and it acts on the Hilbert space $L^2(G)$ by the integrated regular representation, whose norm closure is the reduced group $\mathrm{C}^*$-algebra and whose weak closure is the group von Neumann algebra. This article develops the second sense: the left and the right regular representations, their commutation and the von Neumann algebra they generate, the two $\mathrm{C}^*$-completions, and the enveloping von Neumann algebra $L(G)$ with its trace and its commutant description.

The article assumes the group $G$, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the algebra $L^1(G)$ and its involution from *The Convolution Algebra $L^1(G)$*; the convolution operators, their norms and their composition laws from *Convolution on a Group*; the characters, the abelian transform and Pontryagin duality from *Harmonic Analysis on Groups*; the unitary dual, the operator-valued transform, the group von Neumann algebra $L(G)$ and the direct-integral decomposition from *Noncommutative Harmonic Analysis* and *The Plancherel Theorem* (which owns the decomposition and the Plancherel measure); and the bounded operators, the $\mathrm{C}^*$-algebras, the von Neumann algebras and their topologies from *Operator Algebras*. The decomposition of $L(G)$ into a direct integral and the Plancherel measure are used, never reconstructed; the adjoint of a convolution operator belongs to the `- * Operator Theory` group of this category, and the measure algebra to *The Involution on the Measure Algebra*, later. No involution on the elements is introduced here beyond the involution of the algebra, which is cited.

Throughout, $G$ is a locally compact Hausdorff group with identity $e$, left Haar measure $dx$ and modular function $\Delta$; $G$ is **unimodular** when $\Delta \equiv 1$; $\mathcal{A} = L^1(G)$ is the group algebra with convolution $f*g$ and norm $\|f\|_1$; $L^2(G)$ carries the inner product $\langle\xi,\eta\rangle = \int_G\xi(x)\overline{\eta(x)}\,dx$; and the left and right regular representations are

$$
\bigl(\lambda(x)\xi\bigr)(y) = \xi(x^{-1}y), \qquad \bigl(\rho(x)\xi\bigr)(y) = \xi(yx),
$$

with integrated forms $\lambda(f) = \int_G f(x)\lambda(x)\,dx$ and $\rho(f) = \int_G f(x)\rho(x)\,dx$ in $B(L^2(G))$. The group $\mathrm{C}^*$-algebras are $C^*_r(G)$ and $C^*(G)$, and the group von Neumann algebra is $L(G) = \lambda(G)''$. The convolution operators $L_f, R_f$ on $\mathcal{A}$ are those of *Convolution on a Group*.

## The Group Algebra Acting on Itself

**Definition.** The **regular left module** of $\mathcal{A}$ is $\mathcal{A}$ with the action $f\cdot h = f*h$; the **regular right module** is $\mathcal{A}$ with $h\cdot f = h*f$. The associated operators are the left and right convolutions $L_f, R_f \in B(L^1(G))$.

**Theorem (the action is faithful and isometric).** The maps

$$
\mathcal{A} \to B(L^1(G)), \qquad f \mapsto L_f , \qquad f \mapsto R_f ,
$$

are injective and isometric, $\|L_f\| = \|R_f\| = \|f\|_1$, and the first is an algebra homomorphism while the second is an anti-homomorphism; their images $\mathcal{C}_L, \mathcal{C}_R$ are closed subalgebras of $B(L^1(G))$ isomorphic to $\mathcal{A}$ and to its opposite.

**Proof.** Injectivity and the norms are *Convolution on a Group*, §The Convolution Operators; the homomorphism and anti-homomorphism laws are $L_fL_g = L_{f*g}$ and $R_fR_g = R_{g*f}$ there. An isometric isomorphic embedding has closed image because the image of a complete space under an isometry is complete. $\square$

**Corollary (the module structure).** The left and the right actions commute, $L_fR_g = R_gL_f$, so that $\mathcal{A}$ is a bimodule over itself, and $\mathcal{C}_R \subseteq \mathcal{C}_L'$ and $\mathcal{C}_L \subseteq \mathcal{C}_R'$ inside $B(L^1(G))$.

**Proof.** The commutation law is associativity, $f*(h*g) = (f*h)*g$, from *Convolution on a Group*. $\square$

**Remark (why the regular module is not enough).** The algebra acts on its own Banach space faithfully, but a Banach space is not a Hilbert space and the module carries no inner product adapted to the involution; the representation on $L^2(G)$ repairs both defects, and it is the one whose weak closure is the von Neumann algebra of the next sections.

## The Regular Representation

**Definition.** The **left** and **right regular representations** of $G$ are the maps $\lambda, \rho : G \to \mathcal{U}(L^2(G))$ above. Their integrated forms $\lambda(f), \rho(f) \in B(L^2(G))$ extend the convolution operators from $L^1(G)$ to $L^2(G)$.

**Theorem (they are unitary representations that commute).** For all $x, y \in G$,

$$
\lambda(x)\lambda(y) = \lambda(xy), \qquad \rho(x)\rho(y) = \rho(yx), \qquad \lambda(x)\rho(y) = \rho(y)\lambda(x),
$$

and $\lambda(x), \rho(x)$ are unitary on $L^2(G)$ when $G$ is unimodular; in general $\lambda$ is unitary and $\rho$ is unitary for the weighted inner product with weight $\Delta$.

**Proof.** The composition laws are the associativity of the product on the argument $y\mapsto x^{-1}y$ and $y\mapsto yx$; unitarity of $\lambda$ is the left invariance of $dx$, and unitarity of $\rho$ on $L^2(G)$ holds exactly when $dx$ is also right-invariant, that is when $\Delta\equiv1$; the weighted form is the standard correction. $\square$

**Proposition (the integrated form and the products).** For $f, g \in L^1(G)$,

$$
\lambda(f)\lambda(g) = \lambda(f*g), \qquad \rho(f)\rho(g) = \rho(g*f), \qquad \lambda(f)\rho(g) = \rho(g)\lambda(f),
$$

and $\|\lambda(f)\| \leq \|f\|_1$, $\|\rho(f)\| \leq \|f\|_1$ in $B(L^2(G))$; on the invariant subspace $L^1(G)\cap L^2(G)$ the operator $\lambda(f)$ agrees with left convolution by $f$.

**Proof.** The products follow by integrating the group products $\lambda(x)\lambda(y) = \lambda(xy)$ against $f(x)g(y)$, and the bounds are the triangle inequality for the operator-valued integral; the agreement on $L^1\cap L^2$ is the convolution theorem. $\square$

**Corollary (the regular representation of $G\times G$).** The pair $(\lambda,\rho)$ is a unitary representation of $G\times G$ on $L^2(G)$ whose two factors commute; on a unimodular group it is the regular representation, and it is the representation whose decomposition is the content of the Plancherel theorem.

**Proof.** The product law of $G\times G$ and the commutation give the representation; the two factors being the left and right translations, the representation is standard. $\square$

## The Two $\mathrm{C}^*$-Completions

**Definition.** The **reduced group $\mathrm{C}^*$-algebra** is the norm closure

$$
C^*_r(G) = \overline{\lambda(L^1(G))}^{\ \|\cdot\|} \subseteq B(L^2(G)),
$$

and the **full (universal) group $\mathrm{C}^*$-algebra** $C^*(G)$ is the completion of $L^1(G)$ in the norm $\|f\|_{C^*} = \sup_\pi\|\pi(f)\|$ over all continuous unitary representations $\pi$, the supremum being finite because $\|\pi(f)\|\leq\|f\|_1$.

**Theorem (the completions and the algebra).** The map $f \mapsto \lambda(f)$ extends to a surjective $\mathrm{C}^*$-homomorphism $C^*(G)\to C^*_r(G)$, which is an isomorphism exactly when $G$ is amenable; the algebra $\mathcal{A} = L^1(G)$ is dense in both, and a nondegenerate $*$-representation of $\mathcal{A}$ extends uniquely to $C^*(G)$.

**Proof.** The reduced norm is dominated by the universal norm, giving the quotient map; the algebraic facts are the standard properties of the full and reduced completions and amenability is the standard criterion for the two norms to agree. The representation statement is the universal property of $C^*(G)$. $\square$

**Remark (the involution enters here).** The completions are $\mathrm{C}^*$-algebras for the involution $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$, which is the structure of the `- * Theory` group of this category and is cited, not developed; the equality of the involution on the elements with the adjoint on the operators is the content of *Hermitian Operators on a Group Algebra*, in the `- * Operator Theory` group.

## The Enveloping von Neumann Algebra

**Definition.** The **group von Neumann algebra** is the double commutant $L(G) = \lambda(G)'' = \lambda(L^1(G))''$, the **enveloping von Neumann algebra** of $\mathcal{A}$ in the regular representation; its elements are the operators on $L^2(G)$ generated by the left translations.

**Theorem (weak closure of the algebra).** The algebra $\lambda(L^1(G))$ is strongly dense in $L(G)$, and the strong, weak and ultraweak closures of $\lambda(L^1(G))$ coincide; hence $L(G)$ is the smallest von Neumann algebra containing the image of $\mathcal{A}$, and $\lambda : \mathcal{A}\to L(G)$ extends to a normal $*$-homomorphism $C^*_r(G)\to L(G)$.

**Proof.** The double commutant of a $*$-closed set is its closure in the weak (equivalently strong, equivalently ultraweak) topology by von Neumann's double-commutant theorem, and $\lambda(L^1(G))$ is $*$-closed because $\lambda(f^*) = \lambda(f)^*$ (proved in the `- * Operator Theory` group); the strong closure of $\lambda(L^1(G))$ is $\lambda(G)''$ because the approximate identity converges to the identity strongly. The normal extension is the standard one. $\square$

**Theorem (the commutant description).** On a unimodular group the right regular representation generates the commutant of the left one,

$$
L(G) = \lambda(G)'' = \rho(G)' , \qquad \lambda(G)' = \rho(G)'' ,
$$

so the von Neumann algebra generated by the left translations is exactly the algebra of operators commuting with the right translations.

**Proof.** Every $\rho(y)$ commutes with every $\lambda(x)$, so $\rho(G)\subseteq\lambda(G)'$ and $\lambda(G)\subseteq\rho(G)'$; the reverse inclusions $\lambda(G)''\supseteq\rho(G)'$ and $\rho(G)''\supseteq\lambda(G)'$ are the standard commutant theorem for the regular representation of a unimodular group, the unimodularity being needed for $\rho$ to be unitary on $L^2(G)$ and for the two representations to be in duality. $\square$

**Proposition (the trace and the weights).** On a unimodular group the algebra $L(G)$ carries the faithful normal semifinite trace

$$
\tau(T) = \int_{\operatorname{Irr}(G)} \operatorname{Tr}\bigl(T(\pi)\bigr)\,d\mu_P(\pi) \qquad (T \in L(G)^+),
$$

the Plancherel trace of *The Plancherel Theorem*, normalised by $\tau(\lambda(f)\lambda(g)^*) = \langle f,g\rangle_{L^2(G)}$; when $G$ is discrete and the left regular representation is irreducible-free in the sense of a factor, $\tau(T) = \langle T\delta_e,\delta_e\rangle$ is a finite trace with $\tau(1) = 1$.

**Proof.** The trace is integration of the ordinary trace against the Plancherel measure, established in *The Plancherel Theorem* and *Noncommutative Harmonic Analysis*; the normalisation is the definite Plancherel form; for discrete $G$ the vector $\delta_e$ is separating and the vector state is the same trace. $\square$

**Corollary (the centre and the factors).** The centre of $L(G)$ is $\lambda(G)'' \cap \rho(G)''$, and its spectrum is the space over which the left regular representation decomposes; $L(G)$ is a factor exactly when the centre is $\mathbb{C}$, which for a discrete group happens when every nontrivial conjugacy class is infinite (the ICC groups).

**Proof.** The centre is the intersection of the algebra with its commutant; the factor statement is the standard criterion for the reduced group von Neumann algebra of a discrete ICC group. $\square$

## The Passage from $L^1$ to $L(G)$

**Theorem (the chain of completions).** The inclusions

$$
\mathcal{A} = L^1(G) \ \subseteq \ C^*(G), \qquad \lambda(\mathcal{A}) \ \subseteq \ C^*_r(G) \ \subseteq \ L(G)
$$

exhibit three completions of the same algebra: the norm completion in the universal norm, the norm completion in the regular representation, and the weak closure in the regular representation. The convolution operators $L_f, R_f$ on $L^1(G)$ are the restrictions to $\mathcal{A}$ of the operators $\lambda(f), \rho(f)$, and the algebra $L(G)$ is the smallest von Neumann algebra on $L^2(G)$ containing them.

**Proof.** The inclusions are by definition; the identification of the convolution operators with the integrated representations is the agreement on $L^1\cap L^2$ together with density; the last statement is the weak-closure theorem. $\square$

**Remark (what the article does not do).** The article has used the involution only through its citation from *The Convolution Algebra $L^1(G)$* and the standard equality $\lambda(f^*) = \lambda(f)^*$; the equality is proved in the `- * Operator Theory` group of this category, and no adjoint is taken here. The direct-integral decomposition of $L(G)$, the Plancherel measure and the multiplicity theory are *Noncommutative Harmonic Analysis*, *The Plancherel Theorem* and *The Plancherel Operator* (immediately following); the Tomita–Takesaki modular theory of $L(G)$ for a non-unimodular group belongs to *Operator Algebras* and is not used.

## Summary

The group algebra $L^1(G)$ acts on itself by the left and right convolutions $L_f, R_f$, faithfully and isometrically, $\|L_f\| = \|R_f\| = \|f\|_1$, with $L_fR_g = R_gL_f$; it acts on $L^2(G)$ by the integrated regular representations $\lambda(f) = \int f\lambda$, $\rho(f) = \int f\rho$, which satisfy $\lambda(f)\lambda(g) = \lambda(f*g)$, $\rho(f)\rho(g) = \rho(g*f)$ and $\lambda(f)\rho(g) = \rho(g)\lambda(f)$, the left factor being unitary on a unimodular group. The norm closures give the two group $\mathrm{C}^*$-algebras, $C^*_r(G) = \overline{\lambda(L^1(G))}$ and the universal $C^*(G)$, joined by a quotient map that is an isomorphism exactly for amenable $G$; the weak closure gives the group von Neumann algebra $L(G) = \lambda(G)''$, the enveloping von Neumann algebra of $\mathcal{A}$, strongly generated by $\lambda(L^1(G))$ and equal on a unimodular group to the commutant $\rho(G)'$ of the right regular representation. The algebra $L(G)$ carries the faithful normal semifinite Plancherel trace $\tau$, whose centre is $\lambda(G)''\cap\rho(G)''$ and which is a factor for the discrete ICC groups. The three completions $L^1(G)\subseteq C^*(G)$, $\lambda(L^1(G))\subseteq C^*_r(G)\subseteq L(G)$ are the successive completions of one algebra in the universal norm, the regular norm and the weak topology. The decomposition of $L(G)$, the Plancherel measure and the modular theory of the non-unimodular case are not developed here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{A} = L^1(G)$ | The group algebra with convolution and involution |
| $L_f$, $R_f$ | Left and right convolutions on $\mathcal{A}$, $\|L_f\| = \|R_f\| = \|f\|_1$ |
| $\mathcal{C}_L$, $\mathcal{C}_R$ | Closed subalgebras of $B(L^1(G))$ isomorphic to $\mathcal{A}$ and its opposite |
| $\lambda(x)$, $\rho(x)$ | Left and right regular representations on $L^2(G)$ |
| $\lambda(f)$, $\rho(f)$ | Integrated forms, $\lambda(f) = \int_G f(x)\lambda(x)\,dx$ |
| $\lambda(f)\lambda(g) = \lambda(f*g)$, $\rho(f)\rho(g) = \rho(g*f)$ | Product laws |
| $C^*_r(G) = \overline{\lambda(L^1(G))}$ | Reduced group $\mathrm{C}^*$-algebra |
| $C^*(G)$ | Full (universal) group $\mathrm{C}^*$-algebra |
| $L(G) = \lambda(G)'' = \rho(G)'$ | Group von Neumann algebra, on a unimodular group |
| $\tau$ | Faithful normal semifinite Plancherel trace on $L(G)$ |
| $\operatorname{Irr}(G)$, $\mu_P$ | Unitary dual and Plancherel measure |
| $L^1(G)\subseteq C^*(G)$, $\lambda(L^1(G))\subseteq C^*_r(G)\subseteq L(G)$ | The chain of completions |

## Further Reading

- Jacques Dixmier, *von Neumann Algebras* (North-Holland, 1981), for the double-commutant theorem, the weak and strong closures and the commutant of the regular representation.
- Jacques Dixmier, *$\mathrm{C}^*$-Algebras* (North-Holland, 1977), for the full and reduced group $\mathrm{C}^*$-algebras and the quotient map between them.
- Masamichi Takesaki, *Theory of Operator Algebras I* (Springer, 1979), for the group von Neumann algebra, the trace and the modular theory of the non-unimodular case.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, second edition, 2015), for the regular representations and the group von Neumann algebra.
- Alain Connes, *Noncommutative Geometry* (Academic Press, 1994), for the group von Neumann algebra as the algebra of a measured groupoid and its trace.
