
# __Real Spinors and Reality Conditions__

## Introduction

The complex spinor module of the previous article is defined over $\mathbb{C}$, but the quadratic form that produced it may be real. The passage from complex to real spinors is a **reality condition**: an antilinear map on the complex module whose fixed points, or whose quaternionic structure, cut the complex module down to the real Clifford module. Whether such a map exists, and whether its square is $+1$ or $-1$, is decided by the class of the form modulo eight, and the resulting trichotomy — real, complex and quaternionic spinors — is the reality-theoretic content of the eightfold way. This article supplies the antilinear structures, the sign table, and the explicit low-dimensional cases in dimensions two, three and four.

The spinor module $\Delta=\Lambda^{\bullet}W$ built from a maximal isotropic subspace, the complex classification $\mathbb{C}\mathrm{l}_{2m}\cong M_{2^m}(\mathbb{C})$ and $\mathbb{C}\mathrm{l}_{2m+1}\cong M_{2^m}(\mathbb{C})\times M_{2^m}(\mathbb{C})$, the chirality operator and the half-spin splitting are taken from *Spin Representations and Clifford Modules*. The eightfold table is taken from *Bott Periodicity and the Classification*. The conventions are those of the category: $\mathrm{Cl}_{p,q}$ has $p$ generators of square $+1$, $d=p-q$, and $n=p+q$.

## Antilinear Structures

Complex conjugation is not $\mathbb{C}$-linear, so the notion of a real form of a complex module is carried by antilinear maps.

**Definition.** Let $S$ be a complex vector space. An **antilinear map** $J\colon S\to S$ satisfies $J(\lambda s+\mu t)=\bar\lambda J(s)+\bar\mu J(t)$ for $\lambda,\mu\in\mathbb{C}$ and $s,t\in S$. An antilinear map with $J^2=\varepsilon\,\mathrm{id}$, $\varepsilon=\pm1$, is an **antilinear involution** if $\varepsilon=+1$ and an **antilinear anti-involution** if $\varepsilon=-1$.

**Definition.** Let $S$ be a complex module over $\mathrm{Cl}(V,q)$. A **reality structure** on $S$ is an antilinear map $J$ with $J^2=\pm1$ that commutes with the Clifford action,

$$
J\,c(v)=c(v)\,J \qquad (v\in V),
$$

and that is compatible with the spin representation, that is, $J\rho(x)=\rho(x)J$ for $x\in\mathrm{Spin}(V,q)$. A reality structure with $J^2=+1$ is a **real structure**; one with $J^2=-1$ is a **quaternionic structure**.

**Proposition.** If $S$ carries a real structure $J$ then $S$ is the complexification of the real vector space $S_{\mathbb{R}}=\{s:J(s)=s\}$, and $S_{\mathbb{R}}$ is a real Clifford module. If $S$ carries a quaternionic structure $J$ then $S$ is a vector space over $\mathbb{H}$ with the $j$-action $s\cdot j=J(s)$, and it is a quaternionic Clifford module.

**Proof.** For a real structure, $J$ is an antilinear involution, so the fixed space $S_{\mathbb{R}}$ is a real subspace with $S=S_{\mathbb{R}}\oplus iS_{\mathbb{R}}$ and $S_{\mathbb{R}}\otimes_{\mathbb{R}}\mathbb{C}\cong S$; since $J$ commutes with the Clifford action, the action preserves $S_{\mathbb{R}}$. For a quaternionic structure, define $i$ as multiplication by the complex scalar and $j$ as $J$; then $ij=J\circ(i\,\cdot)$ and $ji=-J\circ(i\,\cdot)$, so $i,j,k=ij$ obey the quaternion relations and $S$ is an $\mathbb{H}$-module. The Clifford action is $\mathbb{C}$-linear and commutes with $J$, hence is $\mathbb{H}$-linear. $\square$

**Remark.** In some parities of $n$ the natural conjugation operator anticommutes with the Clifford action rather than commuting with it, $Jc(v)=-c(v)J$. This happens when the volume element is used to normalise $J$, and the two conventions are exchanged by composing $J$ with the chirality operator, which is available in even dimensions. The sign of $J^2$ is affected by this conjugation: composing $J$ with the volume element multiplies $J^{2}$ by $\omega^{2}$, which is $+1$ precisely in the classes $d\equiv0,1,4,5\bmod8$ and $-1$ in the others. The classification below is therefore stated for the commuting normalisation, fixed once and for all, and the passage between the two conventions is accounted for in the following remark.

**Remark (normalisation and the KO-dimension).** The definition above requires $J$ to *commute* with the Clifford action, which is the normalisation adapted to the classification of the real forms of the module. In the spectral-triple setting the real structure is normalised instead by an order-one condition and by a commutation rule with the operator $D$, and there the charge conjugation anticommutes with Clifford multiplication in the dimensions where the volume element is central. The two normalisations are related by composition with the volume element (, in even dimensions, with the chirality operator), which changes the sign of $J^{2}$ exactly when the volume element satisfies $\omega^{2}=-1$. The two sign tables therefore agree in the classes $d\equiv0,1,4,5\bmod8$, exactly those in which the volume element satisfies $\omega^{2}=+1$ and the twist is trivial, and they differ by the twist in the remaining classes; each is the standard normalisation in its own context. The type table below is the commuting one, appropriate to the reality conditions of the Clifford module.

## The Sign Table

The existence and the square of the reality structure are read from the congruence class of the form.

**Definition.** The **type** of the complex spinor module is **real** if it carries a real structure, **quaternionic** if it carries a quaternionic structure, and **complex** if it carries no reality structure. The **KO-dimension** of the module is the residue $d\bmod 8$ that governs the type; in the positive definite family $\mathrm{Cl}_{n,0}$, where $d=n$, it is the residue of $n\bmod8$.

**Theorem.** Let $V$ be a real quadratic space of dimension $n$ and signature difference $d=p-q$, and let $\Delta$ be its complex spinor module. The type of $\Delta$ is determined by $d\bmod8$ as follows.

| $d \bmod 8$ | type of $\Delta$ | reality structure | spinors |
|---|---|---|---|
| $0$ | real | $J^2=+1$ | Majorana |
| $1$ | real | $J^2=+1$ | Majorana |
| $2$ | real | $J^2=+1$ | Majorana |
| $3$ | complex | none | Weyl, conjugate pair |
| $4$ | quaternionic | $J^2=-1$ | symplectic |
| $5$ | quaternionic | $J^2=-1$ | symplectic |
| $6$ | quaternionic | $J^2=-1$ | symplectic |
| $7$ | complex | none | conjugate pair |

For the definite positive family $\mathrm{Cl}_{n,0}$ the same table is read with $d=n$; for the definite negative family $\mathrm{Cl}_{0,n}$ it is read with $d=-n\equiv8-n\bmod8$. The three types occur with multiplicities $3,2,3$ in each cycle of eight.

**Proof.** By Schur's lemma and the structure of modules over a simple algebra, the irreducible complex module of $\mathrm{Cl}_{p,q}$ is self-conjugate exactly when the commutant of the Clifford action is preserved by complex conjugation as a real algebra; this fails precisely when the division algebra of the real module is $\mathbb{C}$, that is, for $d\equiv3,7\bmod8$, giving the complex type. When the division algebra is $\mathbb{R}$ the fixed points of the conjugation are a real form of the module, giving $J^2=+1$; when it is $\mathbb{H}$ the conjugation is a quaternionic structure, giving $J^2=-1$. The identification of the division algebra from $d\bmod8$ is the eightfold table of the classification. $\square$

**Corollary (Majorana).** A **Majorana spinor** — a spinor that is a fixed point of a real structure — exists exactly when the type is real, that is, for $d\equiv0,1,2\bmod8$. A **Weyl spinor** — an eigenvector of the chirality operator — exists exactly when $n$ is even. A **Majorana–Weyl spinor**, one that is simultaneously real and chiral, exists when the type is real and $n$ is even, which for the definite family $\mathrm{Cl}_{n,0}$ means $n\equiv0,2\bmod8$.

**Proof.** The Majorana condition is the existence of a real structure, which is the table. The Weyl condition is the eigenvector of $\omega$, which exists as a chirality splitting exactly in even dimension by the previous article. The last statement combines the two: for $\mathrm{Cl}_{n,0}$ one has $d=n$, and $n$ even with $n\equiv0,1,2\bmod8$ means $n\equiv0,2\bmod8$. $\square$

## Dimension Two

In two dimensions the two definite forms have different reality types, and the difference is visible in the quaternions.

**The form $\mathrm{Cl}_{2,0}\cong M_2(\mathbb{R})$, $d=2$.** In the matrix model

$$
e_1=\begin{pmatrix}1&0\\0&-1\end{pmatrix}, \qquad e_2=\begin{pmatrix}0&1\\1&0\end{pmatrix}, \qquad \omega=e_1e_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix}, \qquad \omega^{2}=-1,
$$

the generators satisfy $e_1^{2}=e_2^{2}=1$ and $e_1e_2+e_2e_1=0$, and the complex spinor module is $\Delta=\mathbb{C}^2$, of complex dimension $2^{1}=2$, with the chirality operator $\omega$ splitting it into two half-spin spaces of complex dimension one. The type is real: the real structure is componentwise complex conjugation in a suitable basis, and its fixed space is $\mathbb{R}^2$, which is the irreducible real module of $M_2(\mathbb{R})$. The spin representation of $\mathrm{Spin}(2)\cong U(1)$ on $\mathbb{C}^2$ is the sum of the two characters of weight $\pm\tfrac12$: the diagonal circle of $SO(2)$ through the angle $\theta$ acts as $e^{\pm i\theta/2}$, and complex conjugation exchanges the two, which is exactly the statement that the representation is real.

**The form $\mathrm{Cl}_{0,2}\cong\mathbb{H}$, $d=-2\equiv6$.** The complex spinor module is again $\mathbb{C}^2$, but its type is quaternionic. The reality structure has $J^2=-1$, so $\mathbb{C}^2$ becomes a one-dimensional quaternionic space $\mathbb{H}$; the Clifford action is left multiplication by the quaternions and the spin group is the unit quaternions acting on $\mathbb{H}$ by left multiplication. The identification with the previous article is that the irreducible real module of $\mathbb{H}$ is $\mathbb{H}$ itself, of real dimension four.

**Remark.** The same complex module $\mathbb{C}^2$ therefore carries two inequivalent reality structures, one real and one quaternionic, corresponding to the two real forms $M_2(\mathbb{R})$ and $\mathbb{H}$ of $\mathbb{C}\mathrm{l}_2$. The choice of reality condition is precisely the choice of the real quadratic form within its complexification, and it is not determined by the complex spin representation alone. This is the sharpest low-dimensional illustration of the fact that complexification forgets the signature.

## Dimension Three

In three dimensions the type is complex for the definite positive form and quaternionic for the definite negative form.

**The form $\mathrm{Cl}_{3,0}\cong M_2(\mathbb{C})\cong\mathbb{B}$, $d=3$.** The complex spinor module is $\Delta=\mathbb{C}^2$, of dimension two, and its type is complex: there is no antilinear map commuting with the Clifford action whose square is $\pm1$. The complexification $\mathbb{C}\mathrm{l}_3=\mathrm{Cl}_{3,0}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})\times M_2(\mathbb{C})$ has two simple factors, whose irreducible modules are $\mathbb{C}^2$ and its conjugate $\overline{\mathbb{C}^2}$, inequivalent because the conjugation of the complexification, $x\otimes\lambda\mapsto x\otimes\bar\lambda$, swaps the two central idempotents $\tfrac12(1\pm i\omega)$ and so exchanges the two factors rather than fixing them. The biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is itself simple and has a single irreducible complex module up to isomorphism, so the pair of conjugate spinor modules appears only after complexification; the absence of a real structure on the defining module is the algebraic statement that $\mathbb{B}$ has no antilinear involution preserving it. This is the reality condition relevant to the spinor module of the biquaternion algebra.

**The form $\mathrm{Cl}_{0,3}\cong\mathbb{H}\times\mathbb{H}$, $d=-3\equiv5$.** The type is quaternionic. The complex spinor module is $\mathbb{C}^2$ with a quaternionic structure $J^2=-1$, making it a one-dimensional quaternionic space; the two simple factors of $\mathrm{Cl}_{0,3}\cong\mathbb{H}\times\mathbb{H}$ give two non-isomorphic simple modules, each a copy of the quaternionic line. The spin group $\mathrm{Spin}(3)\cong Sp(1)$ acts on $\mathbb{H}$ by left multiplication.

**Remark.** The three real forms of $\mathbb{C}\mathrm{l}_3$ are $\mathrm{Cl}_{3,0}\cong M_2(\mathbb{C})$, $\mathrm{Cl}_{2,1}\cong M_2(\mathbb{R})\times M_2(\mathbb{R})$ and $\mathrm{Cl}_{0,3}\cong\mathbb{H}\times\mathbb{H}$, of complex, real and quaternionic type respectively. All three have complex spinor module $\mathbb{C}^2$; the reality condition distinguishes them. This is the three-dimensional instance of the general fact that the real forms of $\mathbb{C}\mathrm{l}_n$ fall into the three reality types.

## Dimension Four

In four dimensions the two chiralities separate and the reality conditions act on them.

**The form $\mathrm{Cl}_{4,0}\cong M_2(\mathbb{H})$, $d=4$.** The complex spinor module is $\Delta=\mathbb{C}^4$, of dimension $2^{2}=4$, splitting into half-spinors $\Delta_\pm$ of dimension two each. The type is quaternionic: the reality structure has $J^2=-1$, and $\mathbb{C}^4$ becomes the two-dimensional quaternionic space $\mathbb{H}^2$. The chirality operator $\omega$ is a product of an even number of Clifford generators, and $J$ commutes with each Clifford generator, so $c(\omega)$ commutes with $J$; the quaternionic structure therefore preserves each half-spin space, and each half-spin space is a quaternionic line, of complex dimension two. The half-spin representations are the two-dimensional complex representations of the two factors of $\mathrm{Spin}(4)\cong Sp(1)\times Sp(1)$.

**The form $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$, $d=-2\equiv6$.** The complex spinor module is again $\mathbb{C}^4$ with quaternionic structure, of type quaternionic as well, and the chiral splitting is present. The two forms $\mathrm{Cl}_{4,0}$ and $\mathrm{Cl}_{1,3}$ have the same underlying algebra and the same quaternionic type, since $4$ and $-2\equiv6$ both lie in the quaternionic block $d\equiv4,5,6\bmod8$ of the type table; the distinction between them is not visible in the type of the complex spinor module, which is quaternionic in both cases, but in the further invariant that separates the two classes within the quaternionic block, namely the square of the volume element. With $\omega^{2}=(-1)^{n(n-1)/2}\prod_iq(e_i)$ and $n=4$ one gets $\omega^{2}=+1$ for the form $(+,+,+,+)$ and $\omega^{2}=-1$ for $(+,-,-,-)$, so in $\mathrm{Cl}_{1,3}$ the volume element is a complex structure on each half-spin space commuting with the quaternionic structure, and it is this extra structure, not the reality type, that distinguishes $\mathrm{Cl}_{1,3}$ from $\mathrm{Cl}_{4,0}$.

**The form $\mathrm{Cl}_{0,4}\cong M_2(\mathbb{H})$, $d=-4\equiv4$.** Again quaternionic, with $\mathbb{C}^4=\mathbb{H}^2$, and chirality present.

**Remark.** In dimension four every definite form gives quaternionic spinors; there is no Majorana spinor in the definite four-dimensional cases. The four-dimensional half-spin modules are the ones used in the application layer when the biquaternion algebra is combined with the two-sided quaternionic action.

## The Conjugation Operator and the Biquaternion Module

In the applications the reality conditions are computed with an explicit conjugation, and it is convenient to record its form.

**Definition.** Let $\Delta$ be the complex spinor module and suppose a reality structure $J$ exists. The **conjugation** of a spinor $\psi\in\Delta$ is $\psi^{c}=J(\psi)$. When the reality structure is real, the Majorana spinors are those with $\psi^{c}=\psi$; when it is quaternionic, the quaternionic structure identifies $\Delta$ with a quaternionic space and conjugation is the action of the quaternionic unit $j$.

**Proposition.** The conjugation is antilinear, satisfies $(\psi^{c})^{c}=\pm\psi$, and is equivariant for the spin representation: $\rho(x)(\psi^{c})=(\rho(x)\psi)^{c}$ for $x\in\mathrm{Spin}(V,q)$. Consequently the space of Majorana spinors, when it exists, is a real submodule of $\Delta$, and it is the real spinor module of the classification.

**Proof.** Immediate from the properties of $J$ and the compatibility with the Clifford action. $\square$

**The biquaternion case.** For $\mathrm{Cl}_{3,0}\cong\mathbb{B}\cong M_2(\mathbb{C})$, the type is complex, so the defining module $\mathbb{C}^2$ carries no reality structure and there are no Majorana spinors. What is available instead is the **conjugate module**: the antilinear map $\kappa$ given by componentwise conjugation on $\mathbb{B}\cong M_2(\mathbb{C})$ is an $\mathbb{R}$-linear automorphism of the algebra, and it satisfies $\kappa\,c(v)\,\kappa^{-1}=\overline{c(v)}$, the matrix obtained from $c(v)$ by conjugating its entries. Since $\kappa$ is an automorphism and the Clifford relations are real, $v\mapsto\overline{c(v)}$ is again a representation of $\mathrm{Cl}_{3,0}$ on $\mathbb{C}^2$; it is isomorphic to the original as a real representation, with an antilinear intertwiner, but it defines a different complex module. The two simple factors of the complexification of $\mathrm{Cl}_{3,0}$, whose irreducible modules are $\mathbb{C}^2$ and its conjugate, are exchanged by the conjugation of the complexification and the two modules are inequivalent; this is the statement that the complexification of the biquaternion algebra has a pair of conjugate spinor modules rather than a single self-conjugate one. When the algebra is complexified further, or when a real form of the form is chosen in a signature with $d\equiv0,1,2\bmod8$, the conjugation becomes a reality structure and Majorana spinors appear.

## The Role of the Signature

The reality condition depends on the signature and not only on the dimension, and the dependence is exactly the eightfold one.

**Theorem.** Two real quadratic forms of the same dimension $n$ have complex spinor modules of the same complex dimension $2^{\lfloor n/2\rfloor}$; their reality conditions agree whenever their signature differences are congruent modulo eight, the type being a function of $d\bmod8$ alone.

**Proof.** The complexification of the Clifford algebra depends only on $n$, so the complex spinor modules agree as complex modules. The reality condition is the module-theoretic form of the real form of the algebra, which is determined by $d\bmod8$ by the eightfold table; the map from the eight classes to the three types is not injective, since the real block contains three classes and the quaternionic block three, so forms with different signature differences may share a type. $\square$

**Example.** In dimension four the forms $\mathrm{Cl}_{4,0}$ and $\mathrm{Cl}_{1,3}$ have the same complex spinor module $\mathbb{C}^4$ and both are quaternionic, in agreement with $d\equiv4$ and $d\equiv-2\equiv6$, both of quaternionic type. In dimension two, by contrast, $\mathrm{Cl}_{2,0}$ is real and $\mathrm{Cl}_{0,2}$ is quaternionic, with $d\equiv2$ and $d\equiv6$; the two forms have the same complex spinor module $\mathbb{C}^2$ but different reality types. The eightfold way of reality conditions is thus a refinement of the two-fold complex periodicity, and it is the reason the real classification is of period eight.

## Summary

A reality condition on the complex spinor module is an antilinear map $J$ with $J^2=\pm1$ that commutes with the Clifford and spin actions; $J^2=+1$ is a real structure and $J^2=-1$ a quaternionic structure. A real structure exhibits the module as the complexification of a real Clifford module; a quaternionic structure makes it a module over $\mathbb{H}$. The combinatorial content is the trichotomy real, complex, quaternionic, determined by the signature difference $d=p-q$ modulo eight: real for $d\equiv0,1,2$, complex for $d\equiv3,7$, quaternionic for $d\equiv4,5,6$.

Majorana spinors exist exactly when the type is real, Weyl spinors exactly when the dimension is even, and Majorana–Weyl spinors when both conditions hold, which for the definite positive family means $n\equiv0,2\bmod8$. In low dimensions the cases are transparent: in dimension two the module $\mathbb{C}^2$ is real for $\mathrm{Cl}_{2,0}$ and quaternionic for $\mathrm{Cl}_{0,2}$; in dimension three it is complex for $\mathrm{Cl}_{3,0}\cong\mathbb{B}$ and quaternionic for $\mathrm{Cl}_{0,3}$; and in dimension four it is quaternionic for the definite forms, splitting into half-spinors. The biquaternion algebra has no real structure on its defining module, so its two spin representations are conjugate and inequivalent, and the conjugate module is the algebraic source of the two-sided spinor structure of the applications.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Delta$ | Complex spinor module, dimension $2^{\lfloor n/2\rfloor}$ |
| $J$ | Reality structure: antilinear, $J^2=\pm1$, commuting with the Clifford action |
| $J^2=+1$ | Real structure; fixed points are a real Clifford module |
| $J^2=-1$ | Quaternionic structure; $\Delta$ is an $\mathbb{H}$-module |
| $\kappa$ | Componentwise conjugation on $\mathbb{B}\cong M_2(\mathbb{C})$, an algebra automorphism with $\kappa c(v)\kappa^{-1}=\overline{c(v)}$ |
| $\psi^{c}=J(\psi)$ | Conjugation of a spinor |
| $\Delta_\pm$ | Half-spin spaces, chirality eigenspaces (even $n$) |
| $d=p-q$, $n=p+q$ | Signature difference and dimension |
| KO-dimension | The residue $d\bmod8$ that governs the reality type |
| Majorana | Real spinor, a fixed point of a real structure |
| Weyl | Chirality eigenvector, available for even $n$ |
| Majorana–Weyl | Simultaneously real and chiral |
| $\mathbb{B}\cong M_2(\mathbb{C})$ | Biquaternion algebra; its defining module is of complex type |
| $\mathrm{Cl}_{2,0}\cong M_2(\mathbb{R})$, $\mathrm{Cl}_{0,2}\cong\mathbb{H}$ | Real and quaternionic two-dimensional cases |
| $\mathrm{Cl}_{3,0}\cong\mathbb{B}$, $\mathrm{Cl}_{0,3}\cong\mathbb{H}\times\mathbb{H}$ | Complex and quaternionic three-dimensional cases |
| $\mathrm{Cl}_{4,0}\cong\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$ | Quaternionic four-dimensional cases |



## Further Reading

- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for real spinors, reality structures and the relation between the signature and the type.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for explicit reality structures and the low-dimensional spinor modules.
- Michael F. Atiyah, Raoul Bott and Arnold Shapiro, "Clifford modules," *Topology* **3** (1964), supplement 1, 3–38, for the period-eight classification of the reality types.
- Paolo Budinich and Andrzej Trautman, *The Spinorial Chessboard* (Springer, 1988), for the real, complex and quaternionic structures on spinor modules in each dimension modulo eight.
- Max Karoubi, *K-Theory: An Introduction* (Springer, 1978), for the KO-dimension and the antilinear structures on Clifford modules.
