# __The Weights of a Carrier__

## Introduction

A carrier is a module, and a module is described by what a fixed generator does on it. Fix a unit real vector $\vec u$ and the element $\tilde S(\vec u)=\tfrac12 i\vec u\cdot\vec e$; its action on each of the three carriers is diagonalisable, its eigenvalues are symmetric about zero and spaced by one, and the number of them is the dimension of the representation space.

This article computes the three spectra, states the criterion that turns the spectrum into a proof of irreducibility, and evaluates the quadratic element $\sum_k\tilde S_k^2$ on each carrier. The spectra are $\{0\}$, $\{\pm\tfrac12\}$ and $\{0,\pm1\}$; the element is central and acts by the scalars $0,\tfrac34,2$.

The carriers and their types are *The Carriers of the Biquaternion Algebra*, and the products are *The Tensor Square of the Adjoint Module*. The bracket on the algebra is *The Commutator Bracket of the Biquaternion Algebra*, its structure *The Lie Algebra of the Biquaternion Algebra*, and the action of the group by conjugation *The Adjoint Action and the Inner Derivations of the Biquaternion Algebra*.

Nothing below is a statement of physics. The Hermitian generators are $\tilde S_k=\tfrac12 i\vec e_k$ and the anti-Hermitian ones $g_k=-\tfrac12\vec e_k=\tfrac{i}{2}\sigma_k$, with $\sigma_k$ the Pauli matrices of the $M_2(\mathbb{C})$ representation; the pure quaternion units $\vec e_x,\vec e_y,\vec e_z$ are the axis convention of the whole group of articles.

## The Generator

**Definition (the generators).** The three Hermitian elements

$$
\tilde S_k=\tfrac12 i\vec e_k,\qquad \tilde S_k^{*}=\tilde S_k,\qquad [\tilde S_i,\tilde S_j]=i\epsilon_{ijk}\tilde S_k,
$$

form a basis of the complex span of $\mathfrak{k}$; the three anti-Hermitian elements $g_k=-\tfrac12\vec e_k$ satisfy $g_k^{*}=-g_k$, $[g_i,g_j]=-\epsilon_{ijk}g_k$ and $\tilde S_k=-ig_k$. For a unit real $\vec u$,

$$
\tilde S(\vec u)=u_k\tilde S_k=\tfrac12 i\,\vec u\cdot\vec e,\qquad g(\vec u)=u_kg_k=-\tfrac12\vec u\cdot\vec e .
$$

**Definition (weight).** Let $(W,\rho)$ be a carrier, let $V_W$ be its representation space, extended to a complex space if it is real, and let $\tilde S(\vec u)$ act on $V_W$ through $\rho$. A vector $v\in V_W$ has **weight** $\lambda$ when $\rho(\tilde S(\vec u))v=\lambda v$. The **weight string** of the carrier is the multiset of the weights of a basis of eigenvectors, and the **highest weight** is its largest element.

**Remark (why the Hermitian generator).** The element $g(\vec u)$ is the one in the real Lie algebra, and its eigenvalues are purely imaginary; the element $\tilde S(\vec u)=-ig(\vec u)$ is the one whose eigenvalues are real, because $i$ times a skew-adjoint operator is self-adjoint for the trace form. The weights are therefore the eigenvalues of $\tilde S(\vec u)$, and the eigenvalues of $g(\vec u)$ are $-i$ times the weights. The two are the same information, and the real numbers are the convenient ones.

**Lemma (self-adjointness).** Let $\langle Y,Z\rangle=\operatorname{tr}(YZ)$ be the trace form. For $X$ with $X^{*}=\pm X$,

$$
\langle \operatorname{ad}_X Y,Z\rangle=\langle Y,\operatorname{ad}_{X^{*}}Z\rangle .
$$

Hence $\operatorname{ad}_{\tilde S_k}$ is self-adjoint and diagonalisable with real eigenvalues, and $\operatorname{ad}_{g_k}$ is skew-adjoint; $L_{\tilde S_k}$ is self-adjoint on the defining module.

*Proof.* By cyclicity, $\operatorname{tr}([X,Y]Z)=\operatorname{tr}(XYZ)-\operatorname{tr}(YXZ)=\operatorname{tr}(YZX)-\operatorname{tr}(YXZ)=\operatorname{tr}\bigl(Y(ZX-XZ)\bigr)=-\operatorname{tr}(Y[X,Z])$. For $X^{*}=-X$ one has $\operatorname{ad}_{X^{*}}Z=X^{*}Z-ZX^{*}=-XZ+ZX=-[X,Z]$, so the last term is $\langle Y,\operatorname{ad}_{X^{*}}Z\rangle$; for $X^{*}=X$ one has $-\operatorname{tr}(Y[X,Z])=\operatorname{tr}(Y(Z X-X Z))$, and $X^{*}Z-ZX^{*}=\operatorname{ad}_XZ$ because the signs of the two factors cancel. A self-adjoint operator on a finite-dimensional complex space with an inner product has real eigenvalues and an eigenbasis.

## The Three Spectra

Fix the axis $\vec e_z$ and write $\tilde S=\tilde S_3=\tfrac12 i\vec e_z$.

**Theorem (the centre).** On the centre $Z=\mathbb{C}e_t$ the action is trivial and the weight string is $\{0\}$.

*Proof.* $\operatorname{Ad}_u(e_t)=e_t$ for every unit, and $\operatorname{ad}_{\tilde S}(e_t)=[\tilde S,e_t]=0$ by centrality; the space is a line and its weight is $0$.

**Theorem (a minimal left ideal).** On a minimal left ideal $S_{+}=\mathbb{B}\tilde\Pi_{+}(\vec e_z)$, with left multiplication as the action, the weight string is $\{+\tfrac12,-\tfrac12\}$.

*Proof.* With $\tilde\Pi_{+}=\tfrac12(e_t+i\vec e_z)$ and $\tilde S=\tfrac12 i\vec e_z$, one has $\tilde S\tilde\Pi_{+}=\tfrac12\tilde\Pi_{+}$, because $i\vec e_z\tilde\Pi_{+}=\tilde\Pi_{+}$; hence $\tilde\Pi_{+}$ is an eigenvector of weight $+\tfrac12$. The companion nilpotent $\vec\Upsilon_{-+}=\tfrac12(i\vec e_x+\vec e_y)$ lies in $S_{+}$ and satisfies $\tilde S\vec\Upsilon_{-+}=-\tfrac12\vec\Upsilon_{-+}$, so it is an eigenvector of weight $-\tfrac12$. The two are independent and $S_{+}$ is two complex-dimensional, so the string is complete. The other ideal has the same string with the two vectors exchanged.

**Theorem (the traceless part).** On the traceless part $\mathfrak{k}$ of the material sector, complexified to $V=\mathfrak{k}_{\mathbb{C}}$ and acted on by $\operatorname{ad}$, the weight string is $\{+1,0,-1\}$, with eigenvectors

$$
v_{+}=\vec e_x+i\vec e_y,\qquad v_{0}=\vec e_z,\qquad v_{-}=\vec e_x-i\vec e_y .
$$

*Proof.* The brackets are $[\vec e_z,\vec e_x]=2\vec e_y$ and $[\vec e_z,\vec e_y]=-2\vec e_x$, so $\operatorname{ad}_{\tilde S}\vec e_x=i\vec e_y$ and $\operatorname{ad}_{\tilde S}\vec e_y=-i\vec e_x$; hence $\operatorname{ad}_{\tilde S}v_{+}=v_{+}$ and $\operatorname{ad}_{\tilde S}v_{-}=-v_{-}$, while $\operatorname{ad}_{\tilde S}\vec e_z=0$. The three vectors form a basis of $V$.

**Corollary (the same generator on the whole algebra).** On $\mathbb{B}$ itself, of complex dimension $4$, the adjoint action of $\tilde S$ has the weight string $\{+1,0,0,-1\}$: one zero from the centre and one from the vector subspace.

*Proof.* $\mathbb{B}=\mathbb{B}_{C}\oplus\mathbb{B}_{V}$ and the two summands are invariant. The centre is fixed, so it contributes a single zero. The vector subspace contributes $\{+1,0,-1\}$ by the theorem, one of whose vectors is $\vec e_z$, fixed. The two zeros are of different origins: one is the trivial module, the other is the middle rung of the adjoint string.

**Remark (the real form of the adjoint carrier).** On the real triple $\mathfrak{k}$ the Hermitian generator does not act: $\operatorname{ad}_{\tilde S}\vec e_x=i\vec e_y\notin\mathfrak{k}$, so the eigenvalues are read after complexification. The real generator is $g_3=-\tfrac12\vec e_z$, anti-Hermitian, and it does preserve $\mathfrak{k}$; its eigenvalues there are $0,\pm i$, and the weights are $-i$ times these, that is $\{0,\pm1\}$ again, because $\tilde S=-ig$. The real form $\mathfrak{p}=i\mathfrak{k}$ carries the same matrix, and the two copies are the real and imaginary parts of one complex weight vector.

**Table of the spectra.**

| carrier | action | module | weights | $\#$ |
|---|---|---|---|---|
| $\mathbb{B}_{C}$ | conjugation, trivial | $\mathcal{V}_1$ | $0$ | $1$ |
| $S_{\pm}$ | left multiplication | $\mathcal{V}_2$ | $+\tfrac12,-\tfrac12$ | $2$ |
| $\mathfrak{k}$ | adjoint | $\mathcal{V}_3$ | $+1,0,-1$ | $3$ |

## The Criterion

**Theorem (irreducibility from the string).** Let $V$ be a finite-dimensional complex module for the rotation algebra, and suppose the weights of $\tilde S(\vec u)$ on $V$ are simple and spaced by one, $\lambda,\lambda-1,\dots,\lambda-n$. Then $V$ is irreducible, its highest weight is $\lambda$, and $\dim_{\mathbb{C}}V=2\lambda+1$.

*Proof.* Let $v$ be an eigenvector of the largest weight. The submodule generated by $v$ is spanned by the images of $v$ under the algebra, and the algebra is spanned by $\tilde S(\vec u)$ and the two ladder elements $\tilde S_{\pm}=\tilde S_x\pm i\tilde S_y$; the ladder elements lower the weight by one and never raise it, so the generated space is spanned by the descending chain from $v$, whose length is $n+1$. If $n+1=\dim V$ the chain is a basis and the module is irreducible. A simple module has a one-dimensional highest-weight space, so the string is simple, and the dimension formula follows from the count.

**Corollary (the three carriers are irreducible, and the string fixes the highest weight).** The strings $\{0\}$, $\{\pm\tfrac12\}$ and $\{0,\pm1\}$ are simple and spaced by one, with highest weights $0$, $\tfrac12$ and $1$; hence the highest weight is the largest eigenvalue and the length of the string is $2s+1$, where $s$ is that eigenvalue.

**Remark (the highest weight and the dimension).** Write $s$ for the highest weight. Because the string is symmetric about $0$ and spaced by one, it runs from $s$ down to $-s$ in $2s+1$ steps, so $s=(d-1)/2$ with $d$ the length of the string. The number is therefore a function of the dimension alone, and the dimension is a function of the number.

**Remark (what a string that is not simple would mean).** A repeated weight would signal a direct sum, not a carrier: the eigenspaces of a self-adjoint operator on an irreducible module are one-dimensional, so a repeated weight is a sum of two carriers of the same type. The two ideals are the example: they carry the same string, twice, over the whole algebra.

## The Central Element and Its Values

**Definition (the quadratic element).** The element

$$
C=\sum_{k=1}^{3}\tilde S_k^{2}=\tilde S_x^{2}+\tilde S_y^{2}+\tilde S_z^{2}
$$

is the **quadratic element** of the triple $\tilde S_k$. It is computed in $\mathbb{B}$ by the algebra product, and in the enveloping algebra of the bracket by composition of the operators.

**Proposition (the value in the algebra).** $C=\tfrac34 e_t$, a central multiple of the unit.

*Proof.* $\tilde S_k^{2}=\tfrac14 i^2\vec e_k^{2}=\tfrac14(-\vec e_k^{2})$ and $\vec e_k^{2}=-e_t$, so $\tilde S_k^{2}=\tfrac14 e_t$ and the sum of three is $\tfrac34 e_t$.

**Proposition (the values on the carriers).** Acting in the module of each carrier, the quadratic element is the scalar

$$
C\big|_{Z}=0,\qquad C\big|_{S_{\pm}}=\tfrac34,\qquad C\big|_{\mathfrak{k}}=2 .
$$

*Proof.* On $Z$ the action of $C=\tfrac34e_t$ is trivial, because $C$ is central and the carrier is the trivial module. On $S_{\pm}$ left multiplication by $\tfrac34 e_t$ is the scalar $\tfrac34$. On $\mathfrak{k}$ the operator $\operatorname{ad}_{\tilde S_k}^{2}$ is the orthogonal projection onto the plane perpendicular to $\vec e_k$: for $k=x$ it kills $\vec e_x$ and fixes $\vec e_y$ and $\vec e_z$, since $\operatorname{ad}_{e_x}\vec e_y=2\vec e_z$, $\operatorname{ad}_{e_x}\vec e_z=-2\vec e_y$ and $\operatorname{ad}_{\tilde S_x}^{2}=-\tfrac14\operatorname{ad}_{e_x}^{2}$. The three projections sum to $2$ on a three-dimensional space, one axis being killed by each and the other two fixed.

**Remark (two elements, one scalar).** The element $C=\tfrac34 e_t$ of $\mathbb{B}$ and the element $\sum_k\tilde S_k\otimes\tilde S_k$ of the enveloping algebra are different objects; they agree on the two-dimensional carrier because that carrier is the defining module, on which the algebra product and the symmetrised product coincide. On the adjoint module they do not: the algebra product gives the scalar $0$, because $C$ is central and the adjoint action kills the centre, and the composed operators give $2$. The value $2$ is the one attached to the carrier, and it is $s(s+1)$ with $s=1$; the value $\tfrac34$ is $s(s+1)$ with $s=\tfrac12$; the value $0$ is $s(s+1)$ with $s=0$. One polynomial, three carriers.

**Remark (what the scalar does not determine).** The value $\lambda=s(s+1)$ is quadratic, so it determines $s$ only up to sign; and the values $0,\tfrac34,2$ are distinct, so on the carriers of this algebra the sign ambiguity does not occur. It occurs in general, which is why the Casimir is a reading of the highest weight and not its definition.

## The Integrality Class

**Proposition.** $-e_t$ acts as $-\mathrm{id}$ on the representation spaces of the two ideals and as $+\mathrm{id}$ on those of the centre and of the traceless part.

*Proof.* On $S_{\pm}$, left multiplication by $-e_t$ is the scalar $-1$. On $Z$ and on $\mathfrak{k}$ the action is by conjugation, and $-e_t$ is central, so $\operatorname{Ad}_u(-e_t)=-e_t$ acts trivially.

**Corollary (half-integer and integer carriers).** The sign of $-e_t$ distinguishes the two classes: $-1$ when $s$ is a half-integer, $+1$ when $s$ is an integer.

**Remark (a sign, not a weight).** The sign is a property of the copy of the action and not a value of $s$; it happens to agree with the integrality of $2s$, and the agreement is a theorem of the representation theory of the rotation group, not a second definition.

## Summary

Fix a unit real axis $\vec u$ and the Hermitian generator $\tilde S(\vec u)=\tfrac12 i\,\vec u\cdot\vec e$. It acts on the three carriers with the spectra $\{0\}$, $\{\pm\tfrac12\}$ and $\{0,\pm1\}$, and the three strings are simple and spaced by one, which is what irreducibility of a carrier means for this algebra.

The length of the string is the dimension of the representation space and the largest element is the highest weight: $1$, $2$ and $3$ for $d$, and $0$, $\tfrac12$, $1$ for $s$. The real generators differ from the Hermitian ones by the factor $i$ and the weights are the real eigenvalues, read after complexification when the carrier is a real subspace.

The quadratic element $\sum_k\tilde S_k^{2}$ is $\tfrac34 e_t$ in the algebra and acts on the three carriers by $0$, $\tfrac34$ and $2$, the values of $s(s+1)$. The central sign $-e_t$ separates the half-integer carriers from the integer ones.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde S_k=\tfrac12 i\vec e_k$ | the Hermitian generators of the rotation triple |
| $g_k=-\tfrac12\vec e_k$ | the anti-Hermitian generators, $g_k=-i\tilde S_k$ |
| $\tilde S(\vec u)=u_k\tilde S_k$ | the generator about the axis $\vec u$ |
| $\lambda$ | a weight, an eigenvalue of $\tilde S(\vec u)$ |
| weight string | the multiset of weights on a carrier |
| $v_{\pm},v_0$ | the weight vectors $\vec e_x\pm i\vec e_y$ and $\vec e_z$ of the traceless part |
| $\tilde S_{\pm}=\tilde S_x\pm i\tilde S_y$ | the ladder elements, lowering the weight by one |
| $\vec\Upsilon_{-+},\vec\Upsilon_{+-}$ | the companion nilpotents, the lowest-weight vectors of the two ideals |
| $C=\sum_k\tilde S_k^{2}$ | the quadratic element, equal to $\tfrac34e_t$ in the algebra |
| $s(s+1)$ | the value of $C$ on a carrier of highest weight $s$ |

## Further Reading

- [The Carriers of the Biquaternion Algebra](the-carriers-of-the-biquaternion-algebra.html), for the three carriers and their types
- [The Spin of a Carrier](the-spin-of-a-carrier.html), for the section that names the number $s$ and chooses the sector
- [The Companion Nilpotents of the Biquaternion Algebra](the-companion-nilpotents-of-the-biquaternion-algebra.html), for $\vec\Upsilon_{-+}$ and its weight
- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the ideals and their bases
- *The Bracket on the Subspaces of the Biquaternion Algebra*, for the brackets $[\vec e_z,\vec e_x]=2\vec e_y$ and their cyclic analogues
- [The Tensor Square of the Adjoint Module](the-tensor-square-of-the-adjoint-module.html), for the products of carriers and the multiplicities
- *The Adjoint Action and the Inner Derivations of the Biquaternion Algebra*, for the derived action and the self-adjointness of the adjoints
- [The Unitary Lie Algebra](the-unitary-lie-algebra.html), for the general theory of the skew-Hermitian part, its closure and its inner derivations
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for the highest-weight classification of the modules of $\mathfrak{su}(2)$.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the weight strings and the Casimir element.
