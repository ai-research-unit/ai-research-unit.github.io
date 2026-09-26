# __The Spinor Representation of the Lorentz Group in Biquaternionic Form__

## Introduction

The companion articles have established the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ as the home of the Lorentz rotors, and the spinor module $S=\mathbb{C}^2$, realized inside the algebra as the minimal left ideal $\mathbb{B}p$, as the module on which those rotors act one-sidedly. The present article treats the **spinor representation** as a representation in its own right: what it is, which representations sit beside it, and — the question this article is written to answer — how far the finite-dimensional representation theory of $SL(2,\mathbb{C})$ can be carried by the algebra $\mathbb{B}$ before a larger carrier is required.

Three claims organize the discussion. First, the spinor representation is the defining two-dimensional representation $(\tfrac12,0)$, and its complex conjugate $(0,\tfrac12)$ is the second, inequivalent fundamental representation; these two are the two **chiralities**, and they are the only two-dimensional irreducible representations. Second, the four-vector representation $(\tfrac12,\tfrac12)$ is the tensor product of the two chiralities, and the algebra $\mathbb{B}$ itself carries it, under conjugation rather than under multiplication. Third, the algebra stops there: the higher $(j,j')$ representations are not carried by $\mathbb{B}$ and each requires a larger module built from tensor powers of the spinor module.

The third claim is the one with content, and it is checked rather than assumed. The two parents already classify the finite-dimensional representations by the pair $(j,j')$ and develop the module and its bilinear pairings; neither asks which of those representations the algebra can actually carry. That is the subject of the last two sections.

Notation is that of the read-list companions. The quaternion basis is $e_0=1,e_1,e_2,e_3$, with $e_k^2=-e_0$ and $e_1e_2=e_3$; the scalar imaginary is $i$, commuting with the quaternion units; $\mathbb{M}_-$ is the anti-Hermitian subspace (the material sector, home of the four-vectors), $\mathbb{M}_+$ the Hermitian subspace (the informational sector), $\mathbb{H}_{\mathbb{B}}$ the real-quaternion subspace, and $\mathbb{C}_{\mathbb{B}}$ the scalar subspace. The algebra isomorphism is $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ with $\Phi(e_k)=-i\sigma_k$ and $\Phi(i)=iI_2$, so that $\Phi(ie_k)=\sigma_k$, and the norm form is the determinant, $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}=\det\Phi(\tilde{Q})$. The trace pairing on the Hermitian sector is $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$.

## The Spinor Representation and Its Carrier

A **spinor** is an element of the two-dimensional complex vector space $S=\mathbb{C}^2$, written as a column. The algebra acts on $S$ by matrix multiplication through $\Phi$, and the group of unit-norm biquaternions,

$$
SL(2,\mathbb{C})=\{\tilde{\Lambda}\in\mathbb{B}:\tilde{\Lambda}\bar{\tilde{\Lambda}}=e_0\}\cong\{g\in M_2(\mathbb{C}):\det g=1\},
$$

acts on it by **left multiplication**,

$$
\psi \;\longmapsto\; \Phi(\tilde{\Lambda})\,\psi,
\qquad \tilde{\Lambda}\in SL(2,\mathbb{C}),\quad \psi\in S .
$$

This is the **spinor representation** of the Lorentz group. Its carrier $S$ is the unique simple module of the algebra $\mathbb{B}\cong M_2(\mathbb{C})$, realized inside $\mathbb{B}$ as the minimal left ideal $\mathbb{B}p$ with $p=\tfrac12(e_0+ie_3)$; the detailed construction, together with the bilinear pairings on $S$, belongs to the companion article on the spinor module and is used here without repetition.

Three properties of the representation are worth stating at once, because they distinguish it from the representations a physics reader meets first.

**It is irreducible.** Since $\mathbb{B}$ is simple, it has exactly one simple module up to isomorphism, and Schur's lemma gives $\mathrm{End}_{\mathbb{B}}(S)=\mathbb{C}$. The module $S$ carries no proper submodule, so the spinor representation is irreducible.

**It is faithful.** The kernel of the action is trivial: $\Phi(-e_0)=-I_2$, so $\pm\tilde{\Lambda}$ act differently on every spinor. This is in contrast with the four-vector action $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^{\dagger}$ on $\mathbb{M}_-$, whose kernel is $\{\pm e_0\}$. The spinor representation is a representation of the double cover $SL(2,\mathbb{C})$ that does **not** descend to $SO^+(1,3)$.

**It is not unitary.** A finite-dimensional unitary representation of a real Lie algebra $\mathfrak{g}$ maps every generator to a skew-adjoint operator, because each one-parameter subgroup is unitary. Every finite-dimensional representation of $SL(2,\mathbb{C})$ is complex-linear, so the boost generator $K_k=ie_k$ is represented by $\rho(K_k)=i\rho(e_k)$. If $\rho(e_k)$ is skew-adjoint then

$$
\rho(K_k)^{\dagger}=(-i)\rho(e_k)^{\dagger}=(-i)\bigl(-\rho(e_k)\bigr)=i\rho(e_k)=\rho(K_k),
$$

so $\rho(K_k)$ is Hermitian; skew-adjointness then forces $\rho(K_k)=0$. The boost generators and their brackets generate the whole Lie algebra, so $\rho=0$. Hence the only finite-dimensional unitary representation of $SL(2,\mathbb{C})$ is the trivial one, and the spinor representation is non-unitary.

The obstruction is visible concretely on $S$. The standard Hermitian form $h(\psi,\phi)=\psi^{\dagger}\phi$ is invariant under the rotation subgroup $SU(2)$ but not under a boost $\tilde{\Lambda}=\cosh\tfrac{\psi}{2}+i\sinh\tfrac{\psi}{2}\hat{\mathbf{u}}$, because

$$
h(\tilde{\Lambda}\psi,\tilde{\Lambda}\phi)=\psi^{\dagger}\tilde{\Lambda}^{\dagger}\tilde{\Lambda}\,\phi,
\qquad \tilde{\Lambda}^{\dagger}\tilde{\Lambda}=\tilde{\Lambda}^{2}=\cosh\psi+i\sinh\psi\,\hat{\mathbf{u}}\neq e_0 .
$$

For example, on a boost along $e_3$ the operator $\tilde{\Lambda}^{\dagger}\tilde{\Lambda}$ is $\mathrm{diag}(e^{\psi},e^{-\psi})$, which differs from the identity for every $\psi\neq0$. The invariant bilinear form on $S$ is instead the antisymmetric $\varepsilon(\psi,\phi)=\psi^{T}\epsilon\phi$, which is symplectic rather than Hermitian.

## The Two Fundamental Representations Are the Two Chiralities

The **conjugate** of a representation $\rho$ on a complex vector space is the representation $\bar\rho$ on the same space with the conjugate complex structure, $\bar\rho(\tilde{\Lambda})=\overline{\rho(\tilde{\Lambda})}$. Applied to the spinor representation, conjugation gives a second two-dimensional irreducible representation, the **right-handed** spinor $\bar{S}$, with action

$$
\chi \;\longmapsto\; \overline{\Phi(\tilde{\Lambda})}\,\chi,
$$

which is equivalent to $\chi\mapsto\Phi(\tilde{\Lambda}^{*})\chi$, where $\tilde{\Lambda}^{*}$ is the complex conjugate of the biquaternion. The two modules $S$ and $\bar{S}$ are the two **chiralities**; they are exchanged by parity, and they are the two fundamental (defining) representations of $SL(2,\mathbb{C})$.

They are **inequivalent**. To see this without appealing to the label, complexify the Lie algebra and use the two commuting $\mathfrak{su}(2)$ halves generated by $N_k^{\pm}=\tfrac12(e_k\pm\mathsf{i}\,ie_k)$, where $\mathsf{i}$ is the complexification unit and is distinct from the scalar imaginary $i$ as an algebra element. On a complex module the complexification acts complex-linearly, so $\mathsf{i}$ acts by the module's own complex structure. With the generators of $SL(2,\mathbb{C})$ represented on $S$ by $e_k\mapsto-i\sigma_k$ and $ie_k\mapsto\sigma_k$, a direct computation gives

$$
N_k^{+}\mapsto 0, \qquad N_k^{-}\mapsto -i\sigma_k,
\qquad \text{so} \qquad C_+ = \sum_{k}(N_k^{+})^2 \mapsto 0, \quad C_-=\sum_{k}(N_k^{-})^2 \mapsto -3I_2 .
$$

On the conjugate module the two Casimirs are interchanged, $C_+\mapsto-3I_2$, $C_-\mapsto0$. Since $C_+$ and $C_-$ are invariants, the ordered pair of eigenvalues is an invariant; $(0,-3)$ and $(-3,0)$ differ, so $S$ and $\bar{S}$ are not isomorphic:

$$
S=\left(\tfrac12,0\right)\ncong\left(0,\tfrac12\right)=\bar{S}.
$$

One of the two $\mathfrak{su}(2)$ halves acts as spin $\tfrac12$ on $S$ and trivially on the conjugate half; on $\bar{S}$ the roles are interchanged. That a Weyl spinor has spin $\tfrac12$ under the rotation group and is annihilated by one of the two chiral Casimirs is exactly this statement.

A dimension count confirms that the two chiralities exhaust the elementary cases. An irreducible representation labelled $(j,j')$ has complex dimension $(2j+1)(2j'+1)$. Setting this equal to $2$ forces either $j=0,j'=\tfrac12$ or $j=\tfrac12,j'=0$. So $(0,\tfrac12)$ and $(\tfrac12,0)$ are the only two-dimensional irreducible representations, and every fundamental representation of the Lorentz group is one of the two chiralities.

Two cautions belong here, and both are developed in the companion on the spinor module. First, the two chiralities are **not** the two minimal left ideals $\mathbb{B}p$ and $\mathbb{B}q$: because $\mathbb{B}$ is simple, both ideals are isomorphic to $S$, and left multiplication acts by the *same* representation on each. Second, the right-handed chirality is **not** obtained by right multiplication either: as a right module $\mathbb{B}\cong S^{*}\oplus S^{*}$, and the dual of the defining representation is equivalent to it, $S^{*}\cong S$, via the invariant tensor $\epsilon$ ($g^{T}\epsilon g=\epsilon$ for $\det g=1$). The chirality distinction is therefore invisible to the complex algebra and requires the real structure — complex conjugation — to be seen. The **Dirac spinor** is the direct sum of the two halves, $\Delta=S\oplus\bar{S}=(\tfrac12,0)\oplus(0,\tfrac12)$, of complex dimension $4$.

## The Vector Representation Is the Tensor Product of the Two Chiralities

The two fundamental representations combine into the four-vector representation. With $S$ carrying $(\tfrac12,0)$ and $\bar{S}$ carrying $(0,\tfrac12)$, the outer tensor product is

$$
(\tfrac12,0)\otimes(0,\tfrac12)=(\tfrac12,\tfrac12),
\qquad \dim_{\mathbb{C}}(\tfrac12,\tfrac12)=2\times2=4,
$$

the four-vector representation. The biquaternion algebra carries this representation, not by multiplication but by **conjugation**,

$$
X \;\longmapsto\; \tilde{\Lambda}\,X\,\tilde{\Lambda}^{\dagger},
\qquad X\in\mathbb{B},
$$

and the correspondence with the tensor product is the outer product of a spinor and a conjugate spinor, $u\otimes\bar{v}\mapsto X=u\,v^{\dagger}$, written in matrix coordinates; the Hermitian part $\tfrac12(uv^{\dagger}+vu^{\dagger})$ is the element of $\mathbb{M}_+$ whose four-vector image is $iH$. That this map intertwines the tensor action with the conjugation action is recorded in the companion on the spinor module. What is not recorded there, and is checked here, is the tensor decomposition itself.

**Verification on a chosen case.** Take the diagonal generator $J_3=e_3$ and the third boost generator $K_3=ie_3$, represented on $S$ by $J_3\mapsto-i\sigma_3$, $K_3\mapsto\sigma_3$. On the four-dimensional space $S\otimes\bar{S}$ the diagonal generator acts by $-i\sigma_3\otimes I+I\otimes(i\sigma_3)$ — note that $\bar{S}$ carries $\overline{(-i\sigma_3)}=i\sigma_3$ — and its eigenvalues on the basis $e_a\otimes\bar{e}_b$ are

$$
-i s_a + i s_b, \qquad s_a,s_b\in\{+1,-1\},
\qquad\text{i.e.}\qquad \{0,\,0,\,+2i,\,-2i\}.
$$

On $\mathbb{B}$ the conjugation action of the same generator is $X\mapsto J_3X-XJ_3$ (the two signs are opposite because $J_3^{\dagger}=-J_3$). Its eigenvalues on the basis $I,\sigma_1,\sigma_2,\sigma_3$ are $0$ on $I$ and $\sigma_3$, and $\pm2i$ on the combinations of $\sigma_1,\sigma_2$ — the same multiset $\{0,0,\pm2i\}$. The boost generator agrees as well: on $\mathbb{B}$ the action is $X\mapsto K_3X+XK_3$ (the two signs are equal because $K_3^{\dagger}=K_3$), with eigenvalues $\{+2,-2,0,0\}$, matching $K_3\otimes I+I\otimes K_3$ on $S\otimes\bar{S}$. Both representations are four-dimensional and irreducible, so agreement of the Cartan eigenvalues identifies them: the algebra under conjugation **is** the tensor product of the two chiralities.

This identification is also what makes the tensor product concrete physically. Restricting the four-vector representation to the rotation subgroup $SU(2)\subset SL(2,\mathbb{C})$, the tensor product of two spin-$\tfrac12$ representations decomposes by the Clebsch–Gordan rule,

$$
(\tfrac12,\tfrac12)\big|_{SU(2)}\cong V_{\tfrac12}\otimes V_{\tfrac12}\cong V_1\oplus V_0
\qquad (\text{dimension } 3\oplus1),
$$

the three-dimensional adjoint (the spatial vector) plus the scalar (the time component). The weight multiset $\{0,0,\pm2i\}$ above splits as $\{0,\pm2i\}$ for the spin-1 piece and $\{0\}$ for the scalar, exactly the $3\oplus1$ of the four-vector.

## The $(j,j')$ Tower and Its Reality Structure

Every finite-dimensional irreducible representation of $SL(2,\mathbb{C})$ is an outer tensor product

$$
(j,j') = V_j\boxtimes V_{j'},
\qquad j,j'\in\tfrac12\mathbb{Z}_{\geq0},
\qquad
\dim_{\mathbb{C}}(j,j')=(2j+1)(2j'+1),
$$

where $V_j$ is the irreducible $\mathfrak{su}(2)$-module of dimension $2j+1$. In terms of the spinor module, $V_j$ is the symmetric power, so the carrier of $(j,j')$ is built from the spinor module and its conjugate by

$$
V_j \cong \operatorname{Sym}^{2j}(S),
\qquad
V_{j'} \cong \operatorname{Sym}^{2j'}(\bar{S}),
\qquad
(j,j')\cong \operatorname{Sym}^{2j}(S)\otimes\operatorname{Sym}^{2j'}(\bar{S}),
$$

with the **diagonal** action of the group on the tensor product, $v\mapsto\Phi(\tilde{\Lambda})v$ on each factor of $S$ and $w\mapsto\overline{\Phi(\tilde{\Lambda})}w$ on each factor of $\bar{S}$. This is the precise sense in which the whole tower is generated by the spinor module: each $(j,j')$ occurs in a tensor power of $S$ and $\bar{S}$, symmetrized. The dimensions are collected below.

| Representation | $\dim_{\mathbb{C}}$ | Object | Carrier |
|---|---|---|---|
| $(0,0)$ | $1$ | scalar | $\mathbb{C}$ |
| $(\tfrac12,0)$ | $2$ | left-handed Weyl spinor | $S=\mathbb{B}p$ |
| $(0,\tfrac12)$ | $2$ | right-handed Weyl spinor | $\bar{S}$ |
| $(\tfrac12,\tfrac12)$ | $4$ | four-vector | $\mathbb{B}$ (conjugation) |
| $(1,0)$ | $3$ | self-dual 2-form | $\operatorname{Sym}^2(S)$ |
| $(0,1)$ | $3$ | anti-self-dual 2-form | $\operatorname{Sym}^2(\bar{S})$ |
| $(1,1)$ | $9$ | symmetric traceless rank-2 tensor | $\operatorname{Sym}^2(S)\otimes\operatorname{Sym}^2(\bar S)$ |
| $(\tfrac32,0)$ | $4$ | chiral spin-$\tfrac32$ field | $\operatorname{Sym}^3(S)$ |

**Reality.** Complex conjugation exchanges the two factors of the complexified Lie algebra and hence the two indices:

$$
\overline{(j,j')}=(j',j).
$$

So $(j,j')$ is self-conjugate if and only if $j=j'$. For $j\neq j'$ the representation is of **complex type**: it is not isomorphic to its conjugate, it cannot be made real, and $(j,j')$ and $(j',j)$ form a conjugate pair, as the two chiralities $(\tfrac12,0)$ and $(0,\tfrac12)$ do. For $j=j'$ the representation is of **real type**: it occurs as the totally symmetric traceless tensors of rank $2j$ over the real four-vector space, and the symmetric traceless tensors of a real vector space are real. The first cases check out: $(\tfrac12,\tfrac12)$ has the real form $\mathbb{M}_-$, of real dimension $4$, equal to its complex dimension; $(1,1)$ has the real form of symmetric traceless real rank-2 tensors, of real dimension $9$, again equal to its complex dimension. No $(j,j')$ is of quaternionic type: the self-conjugate ones are all of real type, and the others are complex.

**Descent to the Lorentz group.** Since $-e_0$ acts on $(j,j')$ by $(-1)^{2j+2j'}$, the representation descends to $SO^+(1,3)$ when $j+j'\in\mathbb{Z}$ and is a genuine spin representation of the double cover otherwise. The vector representation and the two-form representations descend; the two chiralities and the $(\tfrac32,0)$ do not.

**Unitarity.** All of these finite-dimensional representations are non-unitary except the trivial one, by the argument of the second section: a finite-dimensional unitary representation would kill the boost generators and hence vanish. The finite-dimensional representation theory of the Lorentz group is thus a theory of *non-unitary* representations, and that is not a defect of the biquaternion realization but a property of the group.

## Where the Algebra Stops

The algebra $\mathbb{B}$ is a complex vector space of dimension $4$. Its natural self-actions are left multiplication, right multiplication, and conjugation; each carries a representation, and the list is short.

**Left multiplication.** As a left module over itself, $\mathbb{B}\cong S\oplus S$, of complex dimension $4$. Left multiplication therefore carries two copies of the defining representation,
$$
\mathbb{B}\cong 2\times(\tfrac12,0).
$$
The only irreducible representation realized by left multiplication on the algebra is the left-handed chirality.

**Right multiplication.** As a right module, $\mathbb{B}\cong S^{*}\oplus S^{*}$, and $S^{*}\cong S$. So right multiplication carries two copies of the *same* chirality, $2\times(\tfrac12,0)$; it does **not** produce the right-handed chirality. This is a precise statement of the caution of the companion on the spinor module: both one-sided multiplications see a single chirality.

**Conjugation.** Under $X\mapsto\tilde{\Lambda}X\tilde{\Lambda}^{\dagger}$ the algebra is irreducible,
$$
\mathbb{B}\cong(\tfrac12,\tfrac12),
$$
the four-vector representation, as verified in the preceding section.

Combining these, the irreducible representations carried by the four-dimensional algebra under its natural self-actions are
$$
(\tfrac12,0)\quad\text{(left or right multiplication)},
\qquad
(\tfrac12,\tfrac12)\quad\text{(conjugation)},
$$
with the left-handed chirality appearing with multiplicity two. The right-handed chirality $\bar{S}$ requires the conjugate complex structure; it is not a submodule of the left or right regular module.

**What the algebra does not carry.** The algebra cannot carry an irreducible representation of complex dimension greater than $4$ at all, since its carrier would not fit. This already excludes $(1,1)$ (dimension $9$) and $(\tfrac32,\tfrac12)$ (dimension $8$). But dimension is not the only obstruction, and it is not the operative one in the first interesting cases. The representations $(1,0)$, $(0,1)$ (dimension $3$) and $(\tfrac32,0)$, $(0,\tfrac32)$ (dimension $4$) all fit inside a four-dimensional space, and yet none of them is carried by $\mathbb{B}$ under the actions the algebra provides:

- under left or right multiplication the only irreducible submodules are copies of $S$, of dimension $2$;
- under conjugation the algebra is irreducible, of dimension $4$, and has no proper invariant subspace.

So $(1,0)$, the self-dual two-form, has no home inside $\mathbb{B}$, even though it is smaller than $\mathbb{B}$. Its carrier is the symmetric square $\operatorname{Sym}^2(S)$, of complex dimension $3$. That carrier is a representation of the group under the diagonal action, but it is **not** a module over the algebra $\mathbb{B}$: the finite-dimensional modules of $\mathbb{B}\cong M_2(\mathbb{C})$ are the direct sums of copies of $S$ alone, and their dimensions are even, whereas $\operatorname{Sym}^2(S)$ has dimension $3$. Likewise the chiral spin-$\tfrac32$ field $(\tfrac32,0)$ lives on $\operatorname{Sym}^3(S)$, of dimension $4$ — the same dimension as the algebra, but a different object, and not a $\mathbb{B}$-module.

This is the boundary of the biquaternion form of the spinor representation, and it is sharper than a size bound. The algebra $\mathbb{B}$ carries the spinor representation, and it carries the four-vector representation as the tensor product of the two chiralities; but it does **not** carry the higher $(j,j')$, and not merely because it is small. The module category of the algebra contains only the left-handed chirality and its multiples; the rest of the tower lives in the tensor category generated by $S$ and $\bar{S}$, whose objects are representations of the group but not modules over the algebra. The generating module and the algebra that acts on it are different objects, and the algebra is the carrier of the elementary representations only. Any statement that "the biquaternion algebra contains the Lorentz representations" must be read with this restriction: the algebra provides the fundamental representation and the vector representation, and the remainder of the finite-dimensional tower is built from it rather than contained in it.

## Summary

The spinor representation is the action of the unit-norm biquaternions on the two-dimensional complex module $S=\mathbb{C}^2$, $\psi\mapsto\Phi(\tilde{\Lambda})\psi$. It is irreducible (the unique simple module of the simple algebra $\mathbb{B}\cong M_2(\mathbb{C})$), faithful ($-e_0$ acts as $-I_2$, so it does not descend to $SO^+(1,3)$), and non-unitary: the invariant Hermitian form is preserved only by $SU(2)$, and $\tilde{\Lambda}^{\dagger}\tilde{\Lambda}=\tilde{\Lambda}^2\neq e_0$ for a boost.

Its complex conjugate $\bar{S}$ is the right-handed chirality. The two chiralities $(\tfrac12,0)$ and $(0,\tfrac12)$ are the only two-dimensional irreducible representations, and they are inequivalent: the two chiral Casimirs take the values $(0,-3)$ and $(-3,0)$ on them. They are not the two minimal left ideals (both carry $S$), and the conjugate chirality is not obtained by right multiplication, since $S^{*}\cong S$; it requires the real structure.

The four-vector representation is their tensor product, $(\tfrac12,\tfrac12)=(\tfrac12,0)\otimes(0,\tfrac12)$, of complex dimension $4$, carried by the algebra under conjugation. The identification is verified by matching the Cartan eigenvalues of the two actions, $\{0,0,\pm2i\}$ for $J_3$ and $\{2,-2,0,0\}$ for $K_3$; on restriction to $SU(2)$ it splits as $3\oplus1$.

The higher representations are $(j,j')=V_j\boxtimes V_{j'}$, $\dim=(2j+1)(2j'+1)$, generated by symmetric powers of the spinor module, $\operatorname{Sym}^{2j}(S)\otimes\operatorname{Sym}^{2j'}(\bar{S})$. They are real when $j=j'$ and complex otherwise, and they descend to the Lorentz group when $j+j'\in\mathbb{Z}$, being genuine spin representations otherwise. The algebra carries only $(\tfrac12,0)$ (with multiplicity two, under left or right multiplication) and $(\tfrac12,\tfrac12)$ (under conjugation). It carries no $(1,0)$, no $(1,1)$, no $(\tfrac32,0)$: the first is excluded by structure, not by size, and the carriers of the others are group representations but not modules over the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_1e_2=e_3$ |
| $i$ | Scalar imaginary, $i^2=-1$, commuting with $e_k$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}$ | Real-quaternion and scalar subspaces |
| $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ | Matrix isomorphism, $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$ |
| $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}=\det\Phi(\tilde{Q})$ | Norm form |
| $p=\tfrac12(e_0+ie_3)$ | Primitive idempotent; $\mathbb{B}p\cong S$ |
| $S=\mathbb{C}^2$ | Spinor module, the defining representation $(\tfrac12,0)$ |
| $\bar{S}$ | Conjugate spinor module, the right-handed chirality $(0,\tfrac12)$ |
| $\Delta=S\oplus\bar{S}$ | Dirac spinor module, $\dim_{\mathbb{C}}=4$ |
| $\psi\mapsto\Phi(\tilde{\Lambda})\psi$ | Lorentz action on the spinor module (left multiplication) |
| $g^{T}\epsilon g=\epsilon$ | Invariance of the symplectic form; $S^{*}\cong S$ |
| $N_k^{\pm}=\tfrac12(e_k\pm\mathsf{i}\,ie_k)$ | Generators of the two $\mathfrak{su}(2)$ halves ($\mathsf{i}$ = complexification unit) |
| $C_\pm=\sum_k(N_k^{\pm})^2$ | Chiral Casimirs; $(0,-3)$ vs $(-3,0)$ on $S$ vs $\bar{S}$ |
| $(j,j')=V_j\boxtimes V_{j'}$ | Irreducible representation, $\dim=(2j+1)(2j'+1)$ |
| $\operatorname{Sym}^{2j}(S)\otimes\operatorname{Sym}^{2j'}(\bar{S})$ | Carrier of $(j,j')$ from symmetric powers of the spinor |
| $X\mapsto\tilde{\Lambda}X\tilde{\Lambda}^{\dagger}$ | Conjugation action carrying $(\tfrac12,\tfrac12)$ on $\mathbb{B}$ |
| $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace pairing on the Hermitian sector |

## Further Reading

- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the construction of the Lorentz representations from two Weyl spinors and the non-unitarity of the finite-dimensional ones.
- Wu-Ki Tung, *Group Theory in Physics* (World Scientific, 1985), for the $(j,j')$ labelling, the two $\mathfrak{su}(2)$ halves, and the reality classification.
- I. M. Gel'fand, R. A. Minlos, and Z. Ya. Shapiro, *Representations of the Rotation and Lorentz Groups and Their Applications* (Pergamon, 1963), for the classical treatment of the finite- and infinite-dimensional representations.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for symmetric powers, highest weights, and the Clebsch–Gordan rule.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for the real forms, complexification, and the classification of unitary representations.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the two-component spinor calculus, self-duality, and the chiral projectors.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for spinors as minimal left ideals and the Clifford-algebra origin of chirality.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor picture of the Lorentz group and the spinor–four-vector correspondence.
