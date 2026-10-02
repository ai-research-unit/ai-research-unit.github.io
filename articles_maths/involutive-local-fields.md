
# __Involutive Local Fields__

## Introduction

A local field is a field that is locally compact and non-discrete for a topology making it a topological field — the archimedean fields $\mathbb{R}$ and $\mathbb{C}$ and the non-archimedean fields that are finite extensions of $\mathbb{Q}_p$ or of the Laurent series field $\mathbb{F}_q((t))$. An involutive local field is a local field with an involution, and on a local field the isometry hypothesis is automatic: the topology is the unique non-discrete locally compact field topology, so every automorphism is continuous, hence isometric, and the involution always preserves the valuation ring, induces a residue involution, and has a fixed field that is again a local field of index at most two. This article treats involutive local fields: it records the classification of local fields, proves that every involution is isometric, classifies the isometric involutions into the identity, the unramified quadratic one with the Frobenius as residue involution, and the ramified quadratic one with trivial residue involution, computes the fixed field, the norm group and the compact group of norm-one elements, and identifies the archimedean case $\mathbb{C}/\mathbb{R}$ as the model.

The article assumes the local field, its valuation ring, maximal ideal, uniformiser, residue field, ramification index and residue degree, and the standard classification of local fields from *Local Fields*; the valuation, its uniqueness and the topology from *Absolute Values, Valuations and Completions*; the residue operator from *The Residue Operator of a Valued Field*; the isometric involution, its residue involution, the fixed field of index two, the norm form and the ramification dichotomy $ef = 2$ from *Involutive Valued Fields*; the involution and its fixed subring from *Involutive Rings*; and the reflexivity and completeness of the local fields from *Reflexive Topological Rings and Fields* and *The Completion Operator*. The central simple algebras over a local field with an involution, their classification by the Brauer group and the involutions, and the Hermitian and skew-Hermitian forms are the subject of *The Book of Involutions* and of *Local Class Field Theory*, and are named at the boundary and not developed.

Throughout, $F$ is a local field with valuation $v$, valuation ring $\mathcal{O}$, maximal ideal $\mathrm{M}$, uniformiser $\pi$, residue field $k = \mathbb{F}_q$, value group $\Gamma\cong\mathbb{Z}$ (in the non-archimedean case) and finite residue cardinality $q = p^f$; $\sigma$ is an involution of $F$; the fixed field is $F^\sigma$, the norm form is $N(x) = x\sigma(x)$, the norm-one group is $U(F,\sigma) = \{x\in F^\times : N(x) = 1\}$, and $\bar\sigma$ is the residue involution.

## Local Fields and Their Involutions

**Proposition (the classification of local fields, recalled).** A local field is one of: $\mathbb{R}$ and $\mathbb{C}$ in the archimedean case; a finite extension of $\mathbb{Q}_p$ in characteristic zero; and the field $\mathbb{F}_q((t))$ of formal Laurent series in characteristic $p$. Each carries a unique non-discrete locally compact field topology, the topology of the valuation in the non-archimedean case and the usual one in the archimedean case, and each is complete for it.

**Proof.** Recalled from *Local Fields*: the locally compact non-discrete fields are classified as the finite extensions of $\mathbb{Q}_p$, of $\mathbb{R}$, and of $\mathbb{F}_p((t))$, and the topology of a locally compact field is unique.

**Theorem (every involution of a local field is isometric).** Let $\sigma$ be an involution of the local field $F$. Then $\sigma$ is continuous for the topology of $F$, hence isometric, hence preserves $\mathcal{O}$, $\mathrm{M}$, every power $\mathrm{M}^n$ and the value group, and induces a residue involution $\bar\sigma$ of $k$.

**Proof.** An automorphism of a locally compact field is continuous: the image of the topology under $\sigma$ is another locally compact field topology on $F$, and the topology of a locally compact field is unique, so $\sigma$ is a homeomorphism. Continuity of $\sigma$ gives continuity of $x\mapsto \lvert\sigma(x)\rvert$; the two absolute values $\lvert \cdot \rvert$ and $\lvert \cdot \rvert_\sigma = \lvert\sigma(\cdot)\rvert$ induce the same topology and are therefore equivalent, and for a local field equivalent absolute values coincide up to a power; since $\sigma$ has finite order the power is $\pm1$ and the positive power is $1$, so $\sigma$ is isometric. The preservation of the filtration and the residue involution are then *Involutive Valued Fields*.

**Corollary (the involution of the ring of integers).** The involution restricts to an involution of the compact ring $\mathcal{O}$ and of each ideal $\mathrm{M}^n$, and it acts on the finite residue field $k$ by $\bar\sigma$; the fixed ring $\mathcal{O}^\sigma$ is the ring of integers of $F^\sigma$ when the extension is unramified and is a proper subring with the same residue field when the extension is ramified.

**Proof.** Preservation of the filtration is the theorem; $\mathcal{O}$ is compact because $F$ is locally compact and $\mathcal{O}$ is closed and bounded, and an involution preserves it. The statements about the fixed ring follow from the ramification dichotomy of *Involutive Valued Fields*.

## The Isometric Involutions

**Theorem (classification of the isometric involutions).** Let $F$ be a local field with an involution $\sigma$. Then exactly one of the following holds:

1. $\sigma = \mathrm{id}$ and $F^\sigma = F$;
2. $\sigma \neq \mathrm{id}$, the fixed field $F^\sigma$ is a local field of index two, the extension $F/F^\sigma$ is **unramified**, $e = 1$, $f = 2$, and the residue involution $\bar\sigma$ is the nontrivial involution of $\mathbb{F}_{q}$, which requires $f$ even and is $x\mapsto x^{p^{f/2}}$;
3. $\sigma \neq \mathrm{id}$, the extension $F/F^\sigma$ is **ramified**, $e = 2$, $f = 1$, and the residue involution is the identity of $\mathbb{F}_p$.

**Proof.** The fixed field has index at most two by *Involutive Valued Fields*, and the ramification dichotomy $ef = 2$ gives cases (2) and (3) according to whether $f = 2$ or $e = 2$. In case (2) the residue involution is a nontrivial automorphism of $\mathbb{F}_q$ of order two, and the automorphisms of $\mathbb{F}_q$ are the powers of the Frobenius $x\mapsto x^p$, so the order-two one exists exactly when $f$ is even and equals $x\mapsto x^{p^{f/2}}$. In case (3) the residue degree is one, so the residue involution is the identity of $\mathbb{F}_p$.

**Corollary (the archimedean case).** For $F = \mathbb{C}$ the only nontrivial involution is the complex conjugation, with fixed field $\mathbb{R}$, residue field trivial, and norm form $N(z) = z\bar z = \lvert z\rvert^2$; for $F = \mathbb{R}$ the only involution is the identity. The conjugation is the archimedean model of case (2) with an infinite residue field.

**Proof.** The automorphisms of $\mathbb{C}$ that are continuous are the identity and the conjugation, and every automorphism of $\mathbb{C}$ as a local field is continuous, so these are the only involutions; the fixed field and norm form are standard.

## The Residue Involution

**Proposition (the residue involution on a local field).** The residue involution $\bar\sigma$ is an involution of the finite field $\mathbb{F}_q$; it is the identity when $f$ is odd or when the extension is ramified, and it is $x\mapsto x^{p^{f/2}}$ when the extension is unramified with $f$ even. Its fixed field $\mathbb{F}_q^{\bar\sigma}$ is $\mathbb{F}_{p^{f/2}}$ in the unramified case and $\mathbb{F}_q$ in the ramified and identity cases, and it is the residue field of the fixed field.

**Proof.** The fixed field of an order-two automorphism of $\mathbb{F}_q$ is the subfield of index two $\mathbb{F}_{p^{f/2}}$ when the automorphism is nontrivial and the whole field when it is trivial; the identification with the residue field of $F^\sigma$ is *Involutive Valued Fields*.

**Corollary (the Teichmüller lift and the residue involution).** When the local field is of characteristic zero and the extension is unramified, the Teichmüller section identifies the residue field with the group of roots of unity of order prime to $p$ in $F$, and the residue involution $\bar\sigma$ corresponds under this identification to the restriction of $\sigma$ to those roots of unity; the involution is therefore determined on the inertial part of $F$ by $\bar\sigma$.

**Proof.** The Teichmüller lift is multiplicative and equivariant for automorphisms by uniqueness, so it intertwines $\bar\sigma$ with $\sigma$ restricted to the prime-to-$p$ roots of unity.

## The Fixed Field and the Norm Group

**Theorem (the norm group and the norm-one group).** Let $\sigma \neq \mathrm{id}$ with fixed field $F^\sigma$. Then the norm form is a continuous multiplicative map $N : F^\times\to (F^\sigma)^\times$ with image of index at most two, the norm-one group $U(F,\sigma) = \ker N$ is a compact group, and it is the set of elements of the form $x/\sigma(x)$ by Hilbert's theorem 90; the norm group is all of $(F^\sigma)^\times$ when the extension is ramified and has index two in the unramified case.

**Proof.** The norm is continuous and multiplicative; its image has index at most two because the norm of the quadratic extension has cokernel of order at most two by Hilbert's theorem 90 and the structure of the local norm group. The norm-one group is closed and bounded, hence compact because $F$ is locally compact; the parametrisation $x/\sigma(x)$ is Hilbert's theorem 90 for the cyclic extension of degree two.

**Corollary (the involution on the uniformiser).** In the ramified case the involution sends the uniformiser to $\sigma(\pi) = \epsilon\pi$ with $\epsilon$ a unit satisfying $N(\epsilon) = \epsilon\sigma(\epsilon) = 1$, and the norm of the uniformiser is $N(\pi) = \epsilon\pi^2$, a uniformiser of $F^\sigma$; in the unramified case one may choose the uniformiser in $F^\sigma$, and then $N(\pi) = \pi^2$ is a unit of $F^\sigma$.

**Proof.** If $\sigma(\pi) = \epsilon\pi$ then applying $\sigma$ gives $\pi = \sigma(\epsilon)\sigma(\pi) = \sigma(\epsilon)\epsilon\pi$, so $\epsilon\sigma(\epsilon) = 1$ and $\epsilon$ is a norm-one unit. Hence $N(\pi) = \pi\sigma(\pi) = \epsilon\pi^2$, and $v(N(\pi)) = 2$ with $\pi^2$ a uniformiser of $F^\sigma$ in the ramified case, so $N(\pi)$ is a uniformiser. In the unramified case the uniformiser of $F^\sigma$ is also a uniformiser of $F$ because $e = 1$, and choosing it in $F^\sigma$ gives $\sigma(\pi) = \pi$ and $N(\pi) = \pi^2$, a unit of $F^\sigma$.

**Remark (reflexivity).** A local field is complete, hence reflexive as a one-dimensional space over itself by *Reflexive Topological Rings and Fields*; the involution transfers to the dual and the canonical map is equivariant, so an involutive local field is a reflexive involutive topological field, and the duality theory of the locally compact field applies, including the Haar measure and the Fourier transform, which are named at this boundary and not used.

## Classification

**Theorem (the involutive local fields).** Up to isomorphism, the involutive local fields $(\sigma \neq \mathrm{id})$ are:

1. $(\mathbb{C}, \text{conjugation})$, with fixed field $\mathbb{R}$;
2. $(F, \sigma)$ where $F/F_0$ is an unramified quadratic extension of local fields of characteristic zero, $\sigma$ the nontrivial automorphism, fixed field $F_0$, residue involution the Frobenius $x\mapsto x^{p^{f/2}}$; the family is parametrised by the quadratic unramified extensions of the local fields;
3. $(F, \sigma)$ where $F/F_0$ is a ramified quadratic extension of local fields, fixed field $F_0$, residue involution the identity; in characteristic zero these are the extensions $F_0(\sqrt{\pi_0 u})$ with $\pi_0$ a uniformiser and $u$ a unit;

together with the identity involution on every local field. The quadratic unramified extensions of a given local field are classified by the square classes of the residue field, and the ramified ones by the square classes of $F_0$ modulo the units.

**Proof.** The case analysis is the classification theorem for the isometric involutions; the parametrisation of the quadratic extensions of a local field by square classes is local class field theory, quoted from *Local Fields*, which also gives the existence of the extensions in each class. The archimedean case is the corollary above.

**Corollary (functions of the classification).** The involutive local fields of case (2) have an unramified fixed field and a nontrivial residue involution; those of case (3) have a ramified fixed field and a trivial residue involution; the norm form is anisotropic over $\mathbb{R}$ in case (1), and in cases (2) and (3) it is the norm of the quadratic extension, which is the standard Hermitian form over the local field.

**Proof.** Read off the ramification dichotomy and the norm form computed above; the Hermitian interpretation is the norm form of the quadratic extension regarded as a form over the fixed field.

## Examples

**Example ($(\mathbb{C}, \text{conjugation})$).** The archimedean involutive local field; fixed field $\mathbb{R}$, norm form $z\bar z$, norm-one group the circle $U(1)$, which is compact; the model of case (2) with an infinite residue field.

**Example ($\mathbb{Q}_p(\sqrt{u})$ unramified).** For $p$ odd and $u$ a nonsquare unit, $F = \mathbb{Q}_p(\sqrt u)$ is unramified of degree two, the involution is $\sqrt u\mapsto -\sqrt u$, the fixed field is $\mathbb{Q}_p$, and the residue involution is the Frobenius $x\mapsto x^p$ on $\mathbb{F}_{p^2}$; the norm group is the subgroup of $p$-adic squares times the norm-one group, and the norm-one group is compact.

**Example ($\mathbb{Q}_2(\sqrt{5})$).** For $p = 2$ the extension $\mathbb{Q}_2(\sqrt 5)$ is unramified of degree two, the residue involution is the Frobenius $x\mapsto x^2$ on $\mathbb{F}_4$, and the fixed field is $\mathbb{Q}_2$; this is case (2) in characteristic zero with $p = 2$ and $f = 2$.

**Example ($\mathbb{Q}_p(\sqrt{p})$ ramified).** The extension is ramified of degree two, the involution is $\sqrt p\mapsto -\sqrt p$, the residue involution is the identity on $\mathbb{F}_p$, and the norm of the uniformiser $\sqrt p$ is $-p$, a uniformiser of $\mathbb{Q}_p$; this is case (3).

**Example ($\mathbb{F}_q((t))$ and its quadratic involutions).** The characteristic-$p$ local field with the identity involution; its nontrivial involutions arise from the quadratic extensions of $\mathbb{F}_q((t))$, which is unramified with residue involution $x\mapsto x^{p^{f/2}}$ when the residue degree is two (so $q = p^f$ with $f$ even), and ramified with trivial residue involution otherwise, giving the characteristic-$p$ instances of cases (2) and (3).

## Summary

A local field carries a unique non-discrete locally compact field topology, so every involution of a local field is continuous, hence isometric: it preserves the valuation ring, the maximal ideal and the whole filtration, and it induces an involution $\bar\sigma$ of the finite residue field. The classification of the involutions is by the ramification of the quadratic extension $F/F^\sigma$: the identity, the unramified case $e = 1$, $f = 2$ with residue involution the Frobenius $x\mapsto x^{p^{f/2}}$ on $\mathbb{F}_q$ (which requires $f$ even), and the ramified case $e = 2$, $f = 1$ with trivial residue involution; the archimedean model is $\mathbb{C}$ with the complex conjugation. The fixed field is a local field of index at most two, the norm form $N(x) = x\sigma(x)$ is multiplicative and continuous with image of index at most two in $(F^\sigma)^\times$, the norm-one group is compact and consists of the elements $x/\sigma(x)$ by Hilbert's theorem 90, and the norm of a uniformiser is a uniformiser in the ramified case and a unit in the unramified case.

An involutive local field is complete, hence reflexive, and the involution transfers to the dual with an equivariant canonical map, so the duality theory of the locally compact field applies; the quadratic extensions that realise the classification are parametrised by square classes, by local class field theory, and the central simple algebras over a local field with an involution, together with the Hermitian and skew-Hermitian forms, are the neighbouring subject.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $v$, $\mathcal{O}$, $\mathrm{M}$, $\pi$, $k = \mathbb{F}_q$ | Local field and its valuation data |
| $\sigma$ | An involution, automatically isometric |
| $F^\sigma$ | Fixed field, a local field, $[F:F^\sigma]\leq 2$ |
| $N(x) = x\sigma(x)$, $v(N(x)) = 2v(x)$ | The norm form |
| $U(F,\sigma) = \ker N$ | Compact norm-one group |
| $\bar\sigma$ | Residue involution of $\mathbb{F}_q$ |
| $x\mapsto x^{p^{f/2}}$ | The nontrivial residue involution, unramified case |
| $ef = 2$ | Unramified $(1,2)$ or ramified $(2,1)$ |
| $(\mathbb{C}, \text{conjugation})$ | The archimedean involutive local field |
| $\mathbb{Q}_p(\sqrt u)$ | The unramified quadratic extension |

## Further Reading

- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for the structure of local fields, quadratic extensions, square classes and Hilbert's theorem 90.
- Jürgen Neukirch, *Algebraic Number Theory* (Springer, 1999), for valuations, ramification, the norm group and local class field theory.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for involutions over local fields, the central simple algebras with involution and the Hermitian forms.
- Seth Warner, *Topological Fields* (North-Holland, 1989), for locally compact fields, the uniqueness of the topology and isometric involutions.
- André Weil, *Basic Number Theory* (Springer, 3rd ed. 1995), for Haar measure, the Fourier transform and the duality of locally compact fields.
