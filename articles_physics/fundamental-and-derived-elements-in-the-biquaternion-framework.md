# __Fundamental and Derived Elements in the Biquaternion Framework__

## Introduction

The framework presents a large collection of objects: the algebra $\mathbb{B}$, the scalar imaginary $i$, the quaternion units, the four conjugations, the four fixed-point subspaces, the two-sector split $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$, the biquaternion norm, the trace form, the roots of $-1$, the idempotents, the polar decompositions. The companion articles use them all. This article asks a different question about them: **which of these objects must be posited, and which follow from the others?**

The question is not decorative. Every derivation in the framework inherits the status of its inputs. If an object is silently promoted from derived to fundamental — or quietly derived in one place and posited in another — then the framework's account of *why* it has the structure it has is wrong, even when every formula is right. The purpose of this article is to fix a sorting criterion, state the base to which it applies, and apply the criterion to the framework's objects one at a time.

The article is therefore mostly bookkeeping, but the bookkeeping is the content. Three discipline rules are observed throughout:

- The criterion is stated explicitly and applied to every object of a given kind in the same way. A subspace that is derived may not become a posit because it is convenient; an element that is posited may not become derived because a formula exists that almost defines it.
- No list is presented as a derivation. For each derived object, the construction from the base is written out; the construction is what the entry asserts, not the entry itself.
- Where the sorting depends on the choice of base, that is said, and the base is fixed before the sorting begins.

Two findings deserve to be stated at the outset. First, the **scalar imaginary $i$ is not an independent fundamental element**. It is the central element of square $-e_t$ and is determined, up to a presentational sign, once the algebra is posited; what is fundamental is the complexification, not $i$ as an extra object. Second, the **two-sector split is forced** by the algebra together with its real structure, but only relative to that real structure; the choice of real form — equivalently, the complexification — is itself a substantive posit of the framework, and the split is sensitive to it. Both claims are argued below rather than assumed.

## The Sorting Criterion

The words "fundamental" and "derived" have no meaning without a base, so the criterion is stated relative to a fixed base $\mathcal{S}$ of posited structure. Let $\mathrm{Aut}(\mathcal{S})$ be the group of structure-preserving bijections of $\mathcal{S}$.

**Definition (derived).** An object $X$ is **derived** from $\mathcal{S}$ if $X$ is uniquely determined by $\mathcal{S}$: there is a construction that produces $X$ from the operations of $\mathcal{S}$ alone, and every element of $\mathrm{Aut}(\mathcal{S})$ preserves $X$. If the construction is unique, $X$ is **rigidly derived**. If the construction determines $X$ only up to the action of $\mathrm{Aut}(\mathcal{S})$, then $X$ is **derived up to presentation**.

**Definition (fundamental).** An object $X$ is **fundamental** with respect to $\mathcal{S}$ if it is not derived from $\mathcal{S}$: the base does not determine it, and it must be posited in addition. Equivalently, there are two structures satisfying $\mathcal{S}$ that agree on every derived object and disagree on $X$.

**Definition (presentation).** A **presentation** is a choice — a basis, a sign, a normalization — that is fixed by no construction from $\mathcal{S}$ but is moved by an element of $\mathrm{Aut}(\mathcal{S})$. A different presentation gives an isomorphic framework carrying the same structure. Presentations are neither fundamental nor derived in the strict sense: they carry no structural information, and the classification "derived up to presentation" records exactly this.

**Definition (interpretation).** An **interpretation** is an identification of a derived algebraic object with a physical entity. It is not a derivation, and not a theorem of the algebra; it is a separate posit, and this article records it as one.

Three remarks make the criterion usable.

1. **The derivedness test is invariance plus construction.** To show that $X$ is derived, both halves are needed: an explicit construction from $\mathcal{S}$, and the observation that automorphisms of $\mathcal{S}$ cannot move $X$. A formula that produces $X$ from data not in $\mathcal{S}$ does not make $X$ derived; it makes the extra data part of the base.

2. **The fundamentality test is a witness.** To show that $X$ is fundamental, it suffices to exhibit an automorphism of $\mathcal{S}$ that does not preserve $X$, or two bases agreeing on all previously posited structure but differing on $X$. The witness is what distinguishes a genuine posit from a presentation: a posit can be varied without changing the base; a presentation cannot be changed without changing the notation.

3. **Objects of the same type receive the same treatment.** If a subspace is derived, every subspace obtained the same way is derived; if an element is a presentation, every element obtained the same way is a presentation. This is the rule that the article is written to respect, and it is the rule most easily broken by a sorting that proceeds case by case.

## The Stipulated Base

The base $\mathcal{S}$ consists of two posits.

**(B1) The quaternion algebra.** The real algebra $\mathbb{H}$: a four-dimensional associative unital algebra with unit $e_t$, a basis $\vec e_x,\vec e_y,\vec e_z$, the relations $\vec e_k^2=-e_t$, and the cyclic products $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$. Its multiplication is posited. As a real division algebra it carries its standard involution ${}^{\natural}$, the unique linear map with $e_t$ fixed and $\vec e_x,\vec e_y,\vec e_z$ negated; this is intrinsic to $\mathbb{H}$ and is not an extra posit.

**(B2) The complexification.** A central element $i$ with $i^2=-e_t$ that commutes with every element of $\mathbb{H}$; equivalently, the complexified algebra

$$
\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}.
$$

The algebra $\mathbb{B}$ is eight-dimensional over $\mathbb{R}$ and four-dimensional over $\mathbb{C}$, with the multiplication extended $\mathbb{C}$-bilinearly from that of $\mathbb{H}$. Its centre is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_t$.

Nothing else is posited. In particular, no conjugation other than the two that the base supplies (${}^{\natural}$ from $\mathbb{H}$ and the real structure below) is assumed; no pairing, trace, norm, subspace, root of $-1$, or polar form is assumed.

**The isomorphism type is a theorem, the algebra is a posit.** The type of the algebra is not free: over $\mathbb{C}$ a finite-dimensional unital associative algebra that is simple with centre $\mathbb{C}$ is a full matrix algebra, and dimension $4=2^2$ forces $\mathbb{B}\cong M_2(\mathbb{C})$. So *that* the algebra is $M_2(\mathbb{C})$ is derived from (B1) and (B2); *which* algebra is posited is the content of the posits. This distinction is used throughout: derivedness of a *type* does not make the object derived.

**The quaternion basis is a presentation.** The units $\vec e_x,\vec e_y,\vec e_z$ are a choice of orthonormal unit pure imaginary triple. Automorphisms of $\mathbb{H}$ (conjugation by $g\in\mathbb{H}$ with $g\bar g=e_t$) rotate the triple among themselves. The individual units are therefore presentations, while the subspaces they determine — for instance the pure imaginary subspace $\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ and its multiples by $i$ — are derived. The same distinction governs $i$ below.

**The real structure.** The complexification singles out an involution. Define $\bar{\cdot}$ by

$$
(Q_te_t+Q_{1x}\vec e_x+Q_{1y}\vec e_y+Q_{1z}\vec e_z)^{*}=Q_{1t}^{*}e_t+Q_{1x}^{*}\vec e_x+Q_{1y}^{*}\vec e_y+Q_{1z}^{*}\vec e_z,
$$

where $Q_{1,\mu}^{*}$ is the complex conjugate of the coefficient. This is the **real structure**: the unique $\mathbb{C}$-antilinear algebra involution that fixes $\mathbb{H}_{\mathbb{B}}$ pointwise and negates $i$. Its fixed-point set is the real quaternion subspace

$$
\mathbb{H}_{\mathbb{B}}=\{q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z\ :\ q_\mu\in\mathbb{R}\},
$$

a real form of the complex algebra, isomorphic to $\mathbb{H}$. Given the complexification (B2), the real structure is canonical: it is the complex conjugation of the scalar factor. The posit is the complexification, and the real structure is the certificate of that posit.

**Why the real structure is a substantive posit.** It would be a mistake to conclude that the real structure is forced by the bare algebra. Forget the complexification and regard $\mathbb{B}$ only as an eight-dimensional real algebra $\mathbb{B}_{\mathbb{R}}$. The real structures on the complex algebra — the $\mathbb{C}$-antilinear algebra involutions — are not unique, and they need not have isomorphic fixed-point sets. Writing $\mathbb{B}\cong M_2(\mathbb{C})$ and letting $\bar{\ }$ denote entrywise conjugation, the maps

$$
\rho_1(\tilde{Q}_1)=\tilde{Q}_1^{\natural}, \qquad \rho_2(\tilde{Q}_1)=J\tilde{Q}_1^{\natural}J^{-1}, \qquad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$

are both $\mathbb{C}$-antilinear algebra involutions; the fixed set of $\rho_1$ is $M_2(\mathbb{R})$, while the fixed set of $\rho_2$ is the copy of $\mathbb{H}$ of matrices $\begin{pmatrix}a&b\\-\bar b&\bar a\end{pmatrix}$, whose determinant $|a|^2+|b|^2$ vanishes only at zero. The two real forms are not isomorphic: one is a division algebra, the other has zero divisors. So the algebra alone does not determine the real form, and the framework's choice — the complexification of $\mathbb{H}$, whose real form is the division algebra $\mathbb{H}_{\mathbb{B}}$ — is a genuine posit, not a consequence of dimension or simplicity. This choice is what will fix the two-sector split in the section after next.

## Derived: The Conjugations

From $\mathbb{H}$ and the complexification, four conjugations are obtained. Only two of them are supplied by the base; the other two are derived.

**Quaternion conjugation.** Extend the standard involution of $\mathbb{H}$ complex-linearly ($\bar{\imath}=i$):

$$
\tilde Q_1^{\natural}=Q_te_t-Q_{1x}\vec e_x-Q_{1y}\vec e_y-Q_{1z}\vec e_z.
$$

It is an involution and an anti-automorphism, and it is rigidly derived from $\mathbb{H}$ in the base (B1). Two identities make it usable. Since $\tilde Q_1^{\natural}=2\,\mathrm{Sc}(\tilde Q_1)e_t-\tilde Q_1$, it is linear in the scalar part and negates the vector part. And

$$
\tilde Q_1\tilde Q_1^{\natural}=Q_{1t}^2+Q_{1x}^2+Q_{1y}^2+Q_{1z}^2,
$$

a central element, so the product of a biquaternion with its quaternion conjugate is a complex scalar. This is not an assumption: it follows from the multiplication table of $\mathbb{H}$.

**Complex conjugation.** The real structure $\bar{\cdot}$ of the previous section. It is an involution and an algebra automorphism, and it is $\mathbb{C}$-antilinear. In the base it is derived from the complexification. Its two eigenspaces,

$$
\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}},
$$

are the fixed set and the $(-1)$-eigenspace, both of real dimension $4$; this **quaternion decomposition** is thus derived from the real structure.

**Hermitian conjugation.** Define

$$
\tilde Q_1^{*}=\overline{\tilde Q_1^{\natural}}.
$$

Because ${}^{\natural}$ and $\bar{\cdot}$ commute (the first negates the vector part and fixes $i$; the second conjugates the complex coefficients and fixes the quaternion units), the composition is an involution. It is an anti-automorphism, since it is the composition of an anti-automorphism with an automorphism. Its explicit form is

$$
\tilde Q_1^{*}=Q_{1t}^{*}e_t-Q_{1x}^{*}\vec e_x-Q_{1y}^{*}\vec e_y-Q_{1z}^{*}\vec e_z.
$$

Nothing here is posited: ${}^{*}$ is *defined* as the composition of the two available involutions. It is rigidly derived.

**Anti-Hermitian conjugation.** Define

$$
\tilde Q_1^{\flat}=-\tilde Q_1^{*}.
$$

It is an involution, since $(\tilde Q_1^\flat)^\flat=\tilde Q_1$; but it is *not* an anti-automorphism. Indeed

$$
(\tilde Q_1\tilde{Q}_2)^{\flat}=-(\tilde Q_1\tilde{Q}_2)^{*}=-\tilde{Q}_2^{*}\tilde Q_1^{*}=-\tilde{Q}_2^{\flat}\tilde Q_1^{\flat},
$$

whereas an anti-automorphism would give $\tilde{Q}_2^{\flat}\tilde Q_1^{\flat}$ with a *plus* sign. It also lies outside the Klein four-group generated by ${}^{\natural}$ and $\bar{\cdot}$: composing it with ${}^{*}$ gives $-1$, so it is ${}^{*}$ together with the central sign $-1$. The sign is the only freedom in its definition, and it is a convention rather than a presentation: no unital automorphism of the base carries ${}^{*}$ to $-{}^{*}$, since every such automorphism fixes $e_t$ while $(-{}^{*})(e_t)=-e_t$. Once the convention is fixed, $\flat$ is rigidly derived.

**Consistency of the sorting.** The four conjugations are not four posits. Two of them are supplied by the base — ${}^{\natural}$ by $\mathbb{H}$ and $\bar{\cdot}$ by the complexification — and the other two are defined from them. The framework's phrase "the four natural conjugations" is therefore accurate as a description but misleading as a count of posits: only ${}^{\natural}$ and $\bar{\cdot}$ are input.

## Derived: The Two-Sector Split

The Hermitian conjugation ${}^{*}$ is an involution, so it has a $\pm1$ eigenspace decomposition. Define

$$
\mathbb{M}_+=\{\tilde Q_1:\tilde Q_1^{*}=\tilde Q_1\}, \qquad \mathbb{M}_-=\{\tilde Q_1:\tilde Q_1^{*}=-\tilde Q_1\}.
$$

Both are derived: they are the eigenspaces of the derived involution ${}^{*}$, and they are preserved by every automorphism of the base (which commutes with ${}^{\natural}$ and $\bar{\cdot}$, hence with ${}^{*}$). The coordinate forms are obtained by solving the eigen-equations, and this is a derivation, so it is written out.

**Solving for $\mathbb{M}_+$.** Write $\tilde Q_1=\sum_\mu Q_{1,\mu} e_\mu$. The condition $\tilde Q_1^{*}=\tilde Q_1$ reads

$$
Q_{1t}^{*}e_t-Q_{1x}^{*}\vec e_x-Q_{1y}^{*}\vec e_y-Q_{1z}^{*}\vec e_z=Q_te_t+Q_{1x}\vec e_x+Q_{1y}\vec e_y+Q_{1z}\vec e_z.
$$

Comparing coefficients gives $Q_{1t}^{*}=Q_{1t}$ and $Q_k^{*}=-Q_k$ for $k=1,2,3$. Thus $Q_{1t}$ is real and the vector coefficients are purely imaginary, and

$$
\mathbb{M}_+=\{q_te_t+iq'_x\vec e_x+iq'_y\vec e_y+iq'_z\vec e_z\ :\ q_t,q'_k\in\mathbb{R}\}.
$$

**Solving for $\mathbb{M}_-$.** The condition $\tilde Q_1^{\flat}=\tilde Q_1$, that is $-\tilde Q_1^{*}=\tilde Q_1$, reads

$$
-Q_{1t}^{*}e_t+Q_{1x}^{*}\vec e_x+Q_{1y}^{*}\vec e_y+Q_{1z}^{*}\vec e_z=Q_te_t+Q_{1x}\vec e_x+Q_{1y}\vec e_y+Q_{1z}\vec e_z,
$$

so $Q_{1t}$ is purely imaginary and the vector coefficients are real:

$$
\mathbb{M}_-=\{iq'_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z\ :\ q'_t,q_k\in\mathbb{R}\}.
$$

Each is a real vector space of dimension $4$, and since ${}^{*}$ has eigenvalues $\pm1$ only,

$$
\boxed{\;\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-\;}.
$$

**Neither sector is a subalgebra.** This is a derived negative fact, with witnesses: $(e_t+i\vec e_x)(e_t+i\vec e_y)=e_t+i\vec e_x+i\vec e_y-\vec e_z\notin\mathbb{M}_+$, because the vector part contains the real term $-\vec e_z$; and $(ie_t+\vec e_x)^2=-2e_t+2i\vec e_x\notin\mathbb{M}_-$, because the scalar part is real. The sector decomposition is a decomposition of vector spaces, not of algebras, and this too follows from the multiplication table rather than being posited.

**The exchange between the sectors.** Multiplication by the central scalar $i$ exchanges the sectors,

$$
i\,\mathbb{M}_+=\mathbb{M}_-, \qquad i\,\mathbb{M}_-=\mathbb{M}_+,
$$

since ${}^{*}$ is $\mathbb{C}$-antilinear: $(i\tilde Q_1)^{*}=-i\tilde Q_1^{*}$ whenever $i$ is central. This is multiplication by $i$, not any conjugation; the conjugations ${}^{\natural}$, $\bar{\cdot}$, and ${}^{*}$ each preserve the sectors, and $\flat$ fixes $\mathbb{M}_-$. Because multiplication by $i$ is not an algebra map, it is not an isomorphism of the sectors as algebras, and because $\langle i\tilde Q_1\rangle_{\natural}=i^2\langle\tilde Q_1\rangle_{\natural}=-\langle\tilde Q_1\rangle_{\natural}$, it identifies them only as anti-isometric real quadratic spaces.

**Is the split forced or chosen?** Relative to the base, the split is forced: it is the eigenspace decomposition of the derived involution ${}^{*}$, and no automorphism of the base can move it. It is not an independent posit, and no further choice enters.

But the split is forced only *relative to the base*, and the real form the base fixes is a posit (it is the content of the complexification). If the algebra is regarded as a bare real algebra, its real structures include one whose fixed set is $M_2(\mathbb{R})$; that real form is not isomorphic to $\mathbb{H}_{\mathbb{B}}$, since $M_2(\mathbb{R})$ has zero divisors and $\mathbb{H}_{\mathbb{B}}$ does not, so no algebra automorphism carries it to the framework's real form. The Hermitian conjugation ${}^{*}$ is built from the real structure, so the sector decomposition inherits this dependence. The correct statement is therefore: **the two-sector split is a theorem about the algebra together with its real form, and the real form is an input.** The split is a consequence of the framework's posit of the quaternion real form, not a consequence of the algebra alone. This is the fact about the framework that the title of this section asks for.

**The naming is not derived.** Which of the two sectors is called "material" and which "informational" is not decided by the algebra. Since $i$ exchanges the sectors and $i\mapsto-i$ is a presentation, the assignment of the temporal coordinate $ict'$ to $\mathbb{M}_-$ rather than to $\mathbb{M}_+$ is a convention, pinned by the choice of sign of $i$. The physical identification of the four-vectors with $\mathbb{M}_-$ and of the qubit operators with $\mathbb{M}_+$ is an *interpretation* in the sense of the criterion: it is a separate posit, recorded in the companion articles, and not a derivation of this algebra.

## Derived: The Trace Form

The trace is not posited either. It is the algebra's own reduced trace, and its values follow from the multiplication table.

**Construction of the trace.** On any algebra $\mathbb{B}$, a linear functional vanishing on commutators is determined by its values on a basis of the commutator quotient. In $\mathbb{B}$, the unit $e_t$ has no commutator representation, while each vector unit is a commutator:

$$
\vec e_x=\tfrac12[\vec e_y,\vec e_z], \qquad \vec e_y=\tfrac12[\vec e_z,\vec e_x], \qquad \vec e_z=\tfrac12[\vec e_x,\vec e_y],
$$

as one checks from $[\vec e_y,\vec e_z]=2\vec e_x$ and its cyclic analogues. Therefore a trace functional, normalized by $\mathrm{Tr}(e_t)=2$ — the degree of the central simple algebra $\mathbb{B}\cong M_2(\mathbb{C})$ — is

$$
\boxed{\;\mathrm{Tr}(\tilde Q_1)=2Q_{1t}=2\,\mathrm{Sc}(\tilde Q_1)\;}.
$$

The normalization is rigidly derived rather than a presentation: the reduced trace of the degree-two matrix model fixes it, and every automorphism of the base fixes $e_t$ and hence the value $\mathrm{Tr}(e_t)$; the vanishing on the vector units is forced. Consequently, for any two biquaternions $\tilde Q_1,\tilde Q_2$,

$$
\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2).
$$

This is the trace formula of the framework, and it is derived, not assumed.

**The trace form on the sectors.** Substituting the coordinate forms derived above gives the values of the bilinear trace form $\mathrm{Tr}(\tilde Q_1\tilde Q_2)$ on each sector. For $\tilde H_1=h_{1t}e_t+i\vec h_1$ and $\tilde H_2=h_{2t}e_t+i\vec h_2$ in $\mathbb{M}_+$,

$$
\mathrm{Tr}(\tilde H_1\tilde H_2^{*})=2\bigl(h_{1t}h_{2t}+\vec h_1\cdot\vec h_2\bigr),
$$

which is real and positive definite; for $\tilde R_1=i r_{1t}e_t+\vec r_1$ and $\tilde R_2=i r_{2t}e_t+\vec r_2$ in $\mathbb{M}_-$,

$$
\mathrm{Tr}(\tilde R_1\tilde R_2)=-2\bigl(r_{1t}r_{2t}+\vec r_1\cdot\vec r_2\bigr),
$$

which is real and negative definite; and for one argument in each sector the value is purely imaginary. Hence the real part of the trace form is positive definite on $\mathbb{M}_+$, negative definite on $\mathbb{M}_-$, and the two sectors are orthogonal for it:

$$
\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-
$$

is an orthogonal decomposition of signature $(4,4)$ for $\mathrm{Re}\,\mathrm{Tr}$. This is a derived structural asymmetry between the two sectors: the operator sector carries a positive-definite form, the material sector a negative-definite one, and the sign is not put in by hand.

**The expectation-value form.** For a state $\tilde{Ϛ}=\tfrac12(e_t+\mu i)$ with $\mu$ a real unit pure quaternion and an observable $\tilde H=h_te_t+i\vec h$, the trace formula gives

$$
\mathrm{Tr}(\tilde{Ϛ}\tilde H^{*})=h_t+\mu\cdot\vec h,
$$

the Born-rule expectation value. This is an application of the derived trace, not a new posit.

## The Scalar Imaginary

The scalar imaginary deserves its own section because it is the one element whose status is genuinely ambiguous, and because the framework uses it both as a scalar (in the $\mathbb{C}$-algebra view) and as an element of the algebra (in the $\mathbb{R}$-algebra view).

**$i$ is not in $\mathbb{H}$.** The algebra $\mathbb{H}$ is four-dimensional with centre $\mathbb{R}e_t$, and no element of $\mathbb{H}$ outside $\mathbb{R}e_t$ is central; in particular there is no central square root of $-1$ in $\mathbb{H}$, since $\vec e_x,\vec e_y,\vec e_z$ are not central. So $i$ cannot be derived from the quaternion algebra alone. This is the sense in which the complexification is a genuine posit: it is not a consequence of (B1).

**Given the algebra, $i$ is determined up to sign.** Regard $\mathbb{B}$ as a real algebra. Its centre is

$$
Z(\mathbb{B})=\{z\in\mathbb{B}\ :\ z\tilde Q_1=\tilde Q_1 z \text{ for all }\tilde Q_1\}=\operatorname{span}_{\mathbb{R}}\{e_t,i\},
$$

which is a copy of $\mathbb{C}$ inside $\mathbb{B}$; this is read off from the requirement that a central element commute with $\vec e_x,\vec e_y,\vec e_z$, which forces its vector coefficients to vanish. The elements of the centre that square to $-e_t$ are exactly the solutions of $z_0^2=-1$ for $z=z_0e_t$ among these, namely

$$
\boxed{\;z=\pm i\;}.
$$

Thus the pair $\{i,-i\}$ is rigidly derived from the algebra, while each of the two elements is derived up to presentation.

**The sign is presentational.** The two choices are exchanged by the real structure itself: $\bar{\cdot}(i)=-i$. Since $\bar{\cdot}$ is an automorphism of the base, no structure distinguishes $i$ from $-i$, and the framework may fix the sign by convention. It never needs to.

**The non-central roots do not play $i$'s role.** The equation $\tilde{\Xi}^2=-e_t$ has, besides $\pm i$, a four-real-dimensional family of non-central solutions, of which $\vec e_k$ is the simplest ($\vec e_k^2=-e_t$). These are derived as well (they solve an equation with coefficients in the base), but they are not central, so they do not define the complex scalar structure of $\mathbb{B}$ and cannot replace $i$ in the complex-polar form. Their existence is a genuine feature of the algebra and is why two polar forms exist; it is not evidence that $i$ is fundamental.

**Verdict.** Relative to the framework's base — the complexified algebra $\mathbb{B}$ together with its real structure — the scalar imaginary is **derived**, up to the presentational sign. It is not an independent fundamental element. It is the certificate of the complexification: the posit is "adjoin a central square root of $-1$," and once that is done the square roots are the derived objects. The only honest qualification is that this is base-relative: if one insisted on a base of $\mathbb{H}$ alone, the complexification could not be derived and $i$ would be counted fundamental. The framework does not use that base, and this article does not either.

**A gap, flagged.** What the framework does *not* supply is a derivation of the complexification itself from $\mathbb{H}$, or any argument that the quaternion real form $\mathbb{H}_{\mathbb{B}}$ should be preferred to the alternative real form $M_2(\mathbb{R})$ available on the same abstract algebra. The sorting below therefore records the complexification as fundamental, with the real-form choice as its content. Whether that choice is physically motivated or merely conventional is not decidable from the algebra, and is left as an open question rather than smoothed over.

## Derived: The Polar Decompositions

The polar decompositions are the last family of objects whose status is settled here, and the verdict is that they introduce no new fundamental data.

**The inputs are already available.** The exponential $\exp(\tilde Q_1)=\sum_{n\ge0}\tilde Q_1^n/n!$ converges for every biquaternion because $\mathbb{B}$ is finite-dimensional, so it is rigged from the multiplication. The roots of $-1$ used by the polar forms are the solutions of $\tilde{\Xi}^2=-e_t$; the central ones are $\pm i$ (previous section) and the non-central ones are the real and non-trivial roots classified in the companion article. Both inputs are derived.

**The Hamilton polar form.** For a biquaternion whose vector part has non-vanishing general plain bilinear square $(\vec Q,\vec Q)=B^2\ne0$, put

$$
R=\sqrt{\langle\tilde Q_1\rangle_{\natural}},\qquad \tilde{\Xi}=\vec Q/B,\qquad \cos\Theta=Q_{1t}/R,\qquad \sin\Theta=B/R,
$$

so that $\tilde Q_1=R\exp(\tilde{\Xi}\Theta)$. The construction is a sequence of operations available in the base: the biquaternion norm from the multiplication and ${}^{\natural}$, the square root and the angle functions from the exponential, and the normalization of the axis from the division by $B$. That it reconstructs $\tilde Q_1$ is a computation,

$$
R(\cos\Theta+\tilde{\Xi}\sin\Theta)=R\cdot\frac{Q_{1t}}{R}+R\cdot\frac{\vec Q}{B}\cdot\frac{B}{R}=Q_{1t}+\vec Q=\tilde Q_1,
$$

which also shows that the construction is not merely formal. The domain condition $B\ne0$ and the uniqueness up to the correlated sign $(R,\Theta)\mapsto(-R,\Theta+\pi)$ are properties of the construction, hence derived.

**The complex polar form.** For a biquaternion with invertible real quaternion part $Q_r$, put $\tan\Psi=Q_r^{-1}Q_i$ and $Q=Q_r(\cos\Psi)^{-1}$, so that $\tilde Q_1=Q\exp(i\Psi)$ with $i$ the central root. Again every ingredient is derived, and the reconstruction

$$
Q\exp(i\Psi)=Q\cos\Psi+iQ\sin\Psi=Q_r+iQ_i=\tilde Q_1
$$

uses the commutativity of the functions of $\Psi$ and the inversion of $Q_r$ in $\mathbb{H}$. The domain condition $Q_r\ne0$ is likewise derived.

**No new posit.** The polar forms are constructions, and the choice between them is a matter of which is defined on the biquaternion at hand — a presentational matter, not a posit. That there are two rather than one is a consequence of the existence of central and non-central roots of $-1$, which is a theorem of the algebra, not an extra input. The polar decompositions therefore leave the base unchanged.

## The Sorting

The results are collected in one place. The statuses are those of the criterion, relative to the base $\mathcal{S}$ fixed above.

| Object | Status | Why |
|---|---|---|
| The quaternion algebra $\mathbb{H}$ and its multiplication | **Fundamental** | Posited in (B1); no construction produces the product. |
| Its standard involution ${}^{\natural}$ | Derived (rigid) | The unique involution fixing $e_t$ and negating $\vec e_x,\vec e_y,\vec e_z$; intrinsic to $\mathbb{H}$. |
| The complexification of $\mathbb{H}$ | **Fundamental** | $i\notin\mathbb{H}$; adjoined in (B2). This is the substantive posit. |
| The scalar imaginary $i$ | Derived (up to sign) | Unique central element with $i^2=-e_t$, up to the presentational sign exchanged by $\bar{\cdot}$. |
| The real structure $\bar{\cdot}$ | Derived from the complexification | Canonical $\mathbb{C}$-antilinear involution with fixed set $\mathbb{H}_{\mathbb{B}}$. |
| The quaternion units $\vec e_x,\vec e_y,\vec e_z$ | Presentation | A basis of the pure imaginary subspace; rotated by automorphisms of $\mathbb{H}$. |
| The real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ | Derived | Fixed set of $\bar{\cdot}$. |
| The complex subspace $\mathbb{C}_{\mathbb{B}}$ | Derived | Centre of $\mathbb{B}$; fixed set of ${}^{\natural}$. |
| Hermitian conjugation ${}^{*}$ | Derived (rigid) | Defined as ${}^{\natural}\circ\bar{\cdot}$. |
| Anti-Hermitian conjugation $\flat$ | Derived (rigid) | Defined as $-{}^{*}$; the central sign is a definitional convention, not a presentation — no automorphism of the base moves it. |
| The sectors $\mathbb{M}_+,\mathbb{M}_-$ | Derived | Eigenspaces of the derived involution ${}^{*}$. |
| The split $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ | Forced relative to the base | Eigen-decomposition of ${}^{*}$; the real form it uses is an input. |
| The biquaternion norm $\langle\tilde Q_1\rangle_{\natural}=\tilde Q_1\tilde Q_1^{\natural}$ | Derived | Multiplication plus ${}^{\natural}$. |
| The trace $\mathrm{Tr}(\tilde Q_1)=2\,\mathrm{Sc}(\tilde Q_1)$ | Derived (rigid) | Vanishes on the vector units because they are commutators; the normalization is the reduced trace of the degree-two matrix model, fixed by every automorphism of the base. |
| The trace form $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Derived | Consequence of the trace. |
| Exponential, roots of $-1$, idempotents, $SL(2,\mathbb{C})$ | Derived | Solving equations with coefficients in the base. |
| Polar decompositions | Derived | Constructions from the exponential and the roots of $-1$. |
| "Material"/"informational" naming and the four-vector identification | Interpretation | A separate physical posit; not a theorem of the algebra. |

## Summary

The framework's objects sort into a small fundamental core and a large derived family. The fundamental core is the quaternion algebra $\mathbb{H}$ with its multiplication, together with the complexification that adjoins a central square root of $-1$. Everything the companion articles call a natural conjugation, a fixed-point subspace, a form, or a polar decomposition is derived from these two posits, and the article has written out the construction in each case.

The two sorting questions raised in the Introduction are answered as follows.

- **The scalar imaginary is derived, not fundamental.** It is not in $\mathbb{H}$, so the complexification is a real posit; but within the complexified algebra it is the unique central square root of $-1$ up to sign, and the sign is exchanged by the real structure. What is fundamental is the complexification, of which $i$ is the certificate.
- **The two-sector split is forced relative to the base, but the base contains a substantive choice.** The split is the eigenspace decomposition of the derived Hermitian conjugation, so it is not an extra posit; but the choice of real form (equivalently, the complexification) that makes that conjugation available is a posit, and the same abstract algebra admits other real structures whose real forms are not isomorphic to $\mathbb{H}_{\mathbb{B}}$. The split is a theorem about the algebra *with its real structure*, not about the algebra alone.

The one gap is left visible rather than closed. The complexification — equivalently, the preference for the quaternion real form — is recorded as fundamental and not derived, and no algebraic argument for that preference is offered, because none is available from the algebra itself.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra (posited) |
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra (posited complexification) |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis (presentation) |
| $i$ | Scalar imaginary, $i^2=-1$, central; derived up to sign |
| ${}^{\natural}$ | Quaternion conjugation; derived from $\mathbb{H}$ |
| $\bar{\cdot}$ | Complex conjugation (real structure); derived from the complexification |
| ${}^{*}={}^{\natural}\circ\bar{\cdot}$ | Hermitian conjugation; derived |
| ${}^{\flat}=-{}^{*}$ | Anti-Hermitian conjugation; derived up to sign |
| $\mathbb{H}_{\mathbb{B}}$ | Real quaternion subspace; fixed set of $\bar{\cdot}$ |
| $\mathbb{C}_{\mathbb{B}}$ | Complex subspace; centre; fixed set of ${}^{\natural}$ |
| $\mathbb{M}_+$ | Hermitian subspace: real scalar, imaginary vector |
| $\mathbb{M}_-$ | Anti-Hermitian subspace: imaginary scalar, real vector |
| $\langle\tilde Q_1\rangle_{\natural}=\tilde Q_1\tilde Q_1^{\natural}=\sum_\mu Q_{1,\mu}^2$ | Biquaternion norm; derived |
| $\mathrm{Tr}(\tilde Q_1)=2\,\mathrm{Sc}(\tilde Q_1)$ | Trace; rigidly derived |
| $\mathrm{Tr}(\tilde Q_1\tilde Q_2)=2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | Trace form; derived |
| $\mathcal{S}$ | The base: (B1) $\mathbb{H}$, (B2) the complexification |

## Further Reading

- [Conventions in the Biquaternion Universe](conventions-in-the-biquaternion-universe.html), for the definitions of $\mathbb{B}$, the four conjugations, and the four fixed-point subspaces whose derivation is sorted here.
- [Biquaternion Automorphisms and Derivations](../articles_maths/biquaternion-automorphisms-and-derivations.html), for the automorphism group $\mathrm{Aut}_{\mathbb{C}}(\mathbb{B})=PGL(2,\mathbb{C})$ and the conjugate-linear coset, which are the source of the non-uniqueness of the real structure used in "The Stipulated Base."
- *The Polar Decomposition in Subspaces*, for the Hamilton, complex and Cartan representations whose status as derived constructions is settled here.
- [Element and Operator Representations: The Three Actions](the-element-and-operator-representations.html), for the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$ used to exhibit the real forms $\mathbb{H}_{\mathbb{B}}$ and $M_2(\mathbb{R})$ and the 4×4 regular image, and [The Polar Decomposition of a N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), §*The Operator Reading: the Twist*, for the spinor realization.
- [Algebras: A General Introduction](../articles_maths/algebras-a-general-introduction.html), for the notions of algebra, centre, simplicity, and base change that the criterion and the base presuppose.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html) and [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), for the physical interpretations that this article records as posits rather than derivations.
