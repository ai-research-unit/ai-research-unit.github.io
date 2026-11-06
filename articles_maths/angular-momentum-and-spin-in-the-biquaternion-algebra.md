# __Angular Momentum and Spin in the Biquaternion Algebra__

## Introduction

The angular-momentum algebra is the Lie algebra $\mathfrak{su}(2)$ with a chosen basis. In the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ it appears in two normalisations: as the anti-Hermitian pure quaternions $g_k=-\tfrac12\vec e_k$, which are the elements of the Lie algebra, and as the Hermitian elements $\tilde S_k=\tfrac12 i\vec e_k=-ig_k$, which are the same generators multiplied by $-i$. The factor $-i$ is what makes them self-adjoint, and it is the only difference between the two pictures.

This article develops the module theory of that algebra inside $\mathbb{B}$: the Casimir, the highest-weight classification, the two module structures, the subcarriers of the regular module, the orbital realisation, the addition of angular momenta, the tensor products, and the four uses of the word spin. It is the pure-mathematical counterpart of *Angular Momentum and Spin in Biquaternionic Form*; the symbols are the same, and the difference is that the present article sets $\hbar=1$ and never leaves the algebra.

The constant $\hbar$ is a unit of action, not an element of $\mathbb{B}$. Every operator below is $\tilde S_k=\tfrac12 i\vec e_k$; the physical article writes the same operator with the dimensionful factor, $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$, and every algebraic statement is homogeneous in $\tilde S_k$. Restoring $\hbar$ is the substitution $\tilde S_k\mapsto\hbar \tilde S_k$, which multiplies every weight by $\hbar$ and the Casimir by $\hbar^2$.

The article also proves one statement that the dimension count does not give. The multiplication map $\mathbb{B}\otimes\mathbb{B}\to\mathbb{B}$ is equivariant for conjugation, and its kernel contains the whole spin-two summand of the tensor square. The product of two biquaternions therefore carries no spin two, and the reason is not arithmetic but a vanishing map.

## The Algebra and Its Conventions

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and the multiplication

$$
\vec e_k^2=-e_t,\qquad \vec e_\mu\vec e_\nu=\epsilon_{\mu\nu\lambda}\vec e_\lambda\quad(\mu\neq\nu),
$$

so that $\vec e_x\vec e_y=\vec e_z$ and $\vec e_y\vec e_x=-\vec e_z$. The matrix model is fixed by

$$
\mathsf{M}_2(e_t)=I_2,\qquad \mathsf{M}_2(\vec e_k)=-i\sigma_k,\qquad \mathsf{M}_2(i)=iI_2,
$$

with $\sigma_k$ the Pauli matrices. It follows that $\mathsf{M}_2(i\vec e_k)=\sigma_k$. The conjugation is the anti-automorphism

$$
e_t^*=e_t,\qquad \vec e_k^*=-\vec e_k,\qquad i^*=-i,
$$

and $\mathsf{M}_2(X^*)=\mathsf{M}_2(X)^\dagger$. The two sectors are

$$
\mathbb{M}_+=\operatorname{span}_{\mathbb{R}}\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\},\qquad
\mathbb{M}_-=\operatorname{span}_{\mathbb{R}}\{ie_t,\vec e_x,\vec e_y,\vec e_z\},
$$

the Hermitian and anti-Hermitian subspaces; $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_+=\mathbb{M}_-$.

The trace form is

$$
\langle X,Y\rangle=\operatorname{tr}(X^*Y),
$$

with $\operatorname{tr}$ the matrix trace. It is positive definite and $\mathbb{C}$-linear in $Y$. The group of unit real quaternions is

$$
G=\{u\in\mathbb{H}_{\mathbb{B}}:uu^*=e_t\},
$$

which is $SU(2)$; its Lie algebra is $\mathfrak{g}=\mathbb{H}_{\mathbb{B}}\cap\mathbb{M}_-=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$, with bracket $[\vec e_\mu,\vec e_\nu]=2\epsilon_{\mu\nu\lambda}\vec e_\lambda$. The complexification $\mathfrak{g}_{\mathbb{C}}=\operatorname{span}_{\mathbb{C}}\{\vec e_x,\vec e_y,\vec e_z\}$ is $\mathfrak{sl}_2(\mathbb{C})$, the traceless part under $\mathsf{M}_2$.

**Proposition.** $\mathsf{M}_2$ is an isomorphism of complex algebras, carries $*$ to the conjugate transpose, and carries the trace form to the Hilbert–Schmidt form.

*Proof.* The map is defined on the basis; on products of basis elements it is the standard Pauli multiplication, so it is an algebra homomorphism. The correspondence $*$ to the conjugate transpose is checked on the basis: $\mathsf{M}_2(\vec e_k^*)=\mathsf{M}_2(-\vec e_k)=i\sigma_k=(-i\sigma_k)^\dagger$. The trace form is then $\operatorname{tr}(\mathsf{M}_2(X)^\dagger\mathsf{M}_2(Y))$, the Hilbert–Schmidt form.

## The Rotation Generators

The Lie algebra has the anti-Hermitian basis

$$
g_k=-\tfrac12\vec e_k\in\mathfrak{g},\qquad [g_i,g_j]=-\epsilon_{ijk}g_k,\qquad g_k^*=-g_k,
$$

and the Hermitian basis

$$
\tilde S_k=\tfrac12 i\vec e_k\in\mathbb{M}_+,\qquad [\tilde S_i,\tilde S_j]=i\epsilon_{ijk}\tilde S_k,\qquad \tilde S_k^*=\tilde S_k.
$$

They are related by $\tilde S_k=-ig_k$. The bracket of the $\tilde S_k$ is the standard angular-momentum relation with $\hbar=1$; the bracket of the $g_k$ is its anti-Hermitian form. The triple is read as one vector, $\vec S$ with components $\tilde S_k$, so that $\vec u\cdot\vec S=u_k\tilde S_k$ for a unit $\vec u$; the glyph is arrowed and carries no tilde, because each component is a pure element (*Algebra and Element Conventions*, §*The Centre and the Vector Subspace*).

**Proposition (the exponential).** For a unit $\vec u\in\mathfrak{g}$ and real $\theta$, the rotation through $\theta$ about $\vec u$ is

$$
\exp(-\theta\,\vec u\cdot\vec g)=\cos\tfrac{\theta}{2}\,e_t+\sin\tfrac{\theta}{2}\,\vec u\cdot\vec e
=\exp(-i\theta\,\vec u\cdot\vec S),
$$

a unit real quaternion, whose adjoint action turns a vector through $+\theta$ about $\vec u$.

*Proof.* The element $\vec u\cdot\vec e$ is a pure real quaternion with square $-e_t$, so the power series splits into the cosine and sine series. The two expressions agree because $\tilde S_k=-ig_k$. The sense of the turn is that of $\operatorname{Ad}_{\tilde q}$ for $\tilde q=\cos\tfrac{\theta}{2}+\sin\tfrac{\theta}{2}\vec u$ (*Quaternion Rotations and Reflections*, §*The Adjoint Action*), which is the same element.

The group generated is $G=SU(2)$, which is the double cover of $SO(3)$.

**The action on a carrier.** A carrier is a pair $(W,\rho)$ with $W$ a finite-dimensional complex space and $\rho$ either an algebra homomorphism $\mathbb{B}\to\operatorname{End}_{\mathbb{C}}(W)$ or a Lie-algebra homomorphism $\mathfrak{g}\to\operatorname{End}_{\mathbb{C}}(W)$. In the first case the generator acts as $\rho(\tilde S_k)$ with $\tilde S_k\in\mathbb{B}$; in the second, $\rho$ extends $\mathbb{C}$-linearly to $\mathfrak{g}_{\mathbb{C}}$ and again $\rho(\tilde S_k)$ is defined. The two cases are kept apart: only the first is a module over the associative algebra. A carrier is **unitary** when $\rho(X^*)=\rho(X)^\dagger$ in the algebra case, equivalently $\rho(X)^\dagger=-\rho(X)$ for $X\in\mathfrak{g}$ in the Lie case. The carriers of this article are unitary for the trace form.

**Lemma (self-adjointness).** For $X\in\mathbb{B}$, the adjoint of $\operatorname{ad}_X$ with respect to the trace form is $\operatorname{ad}_{X^*}$.

*Proof.* Using $\operatorname{tr}((XY-YX)^*Z)=\operatorname{tr}((X^*Z-ZX^*)Y)$ by cyclicity and $(XY)^*=Y^*X^*$, one gets $\langle\operatorname{ad}_X Y,Z\rangle=\langle Y,\operatorname{ad}_{X^*}Z\rangle$.

Consequently $\operatorname{ad}_{\tilde S_k}$ is self-adjoint and $\operatorname{ad}_{g_k}$ is skew-adjoint; $L_{\tilde S_k}$ is self-adjoint on the defining module.

## The Casimir and the Definition of Spin

Let

$$
C=\tilde S_1^2+\tilde S_2^2+\tilde S_3^2\in U(\mathfrak{g}).
$$

**Proposition (centrality).** $[C,\tilde S_l]=0$ for $l=1,2,3$.

*Proof.* $\sum_i[\tilde S_i^2,\tilde S_l]=\sum_i\bigl(\tilde S_i[\tilde S_i,\tilde S_l]+[\tilde S_i,\tilde S_l]\tilde S_i\bigr)=\sum_i\bigl(i\epsilon_{ilj}\tilde S_i\tilde S_j+i\epsilon_{ilj}\tilde S_j\tilde S_i\bigr)$, which is antisymmetric under $i\leftrightarrow j$ and vanishes.

**Definition (spin).** Let $(W,\rho)$ be an irreducible unitary carrier. For a unit $\vec u\in\mathfrak{g}$, the operator $\rho(\vec u\cdot\vec S)$ is self-adjoint. The **spin** of the carrier is

$$
s=\max\operatorname{spec}\bigl(\rho(\vec u\cdot\vec S)\bigr),
$$

the maximum being independent of $\vec u$. The spin is a real number in $\tfrac12\mathbb{Z}_{\ge0}$; it is a scalar label, not a vector.

**Proposition (independence of the axis).** The spectrum of $\rho(\vec u\cdot\vec S)$ does not depend on the unit vector $\vec u$.

*Proof.* For $u\in G$, $\rho(u)\rho(\vec u\cdot\vec S)\rho(u)^{-1}=\rho\bigl(\operatorname{Ad}_u(\vec u\cdot\vec S)\bigr)=\rho\bigl((R\vec u)\cdot\vec S\bigr)$, with $R$ the rotation. The map $G\to SO(3)$ is surjective, so all unit vectors are conjugate, and conjugate operators have the same spectrum.

**Theorem (the Casimir value and the dimension).** Let $(W,\rho)$ be an irreducible unitary carrier of spin $s$. Then

$$
\rho(C)=s(s+1)\operatorname{id}_W,\qquad \dim_{\mathbb{C}}W=2s+1,\qquad s\in\tfrac12\mathbb{Z}_{\ge0}.
$$

*Proof.* Choose an eigenvector $v$ of $\rho(\tilde S_3)$ with the maximal eigenvalue $s$. Then $\rho(\tilde S_+)v=0$, since otherwise $\rho(\tilde S_+)$ would produce an eigenvector of weight $s+1$. Put $v_k=\rho(\tilde S_-)^kv$ and $m_k=s-k$. The span of the $v_k$ is invariant, so it is all of $W$. Since $\tilde S_+\tilde S_-=C-\tilde S_3^2+\tilde S_3$, one has $\rho(\tilde S_+\tilde S_-)v_k=(2s-k)(k+1)v_k$. If the string terminates, so that $v_{k+1}=0$ with $v_k\neq0$, then $0=\rho(\tilde S_+)v_{k+1}=(2s-k)(k+1)v_k$, so $k=2s$. Hence $v_0,\dots,v_{2s}$ are a basis and $\dim W=2s+1$. On $v_0$, $\rho(C)v_0=(s^2+2s)v_0=s(s+1)v_0$.

**Remark.** The algebra sees $SU(2)$ and not $SO(3)$: $s$ ranges over the half-integers. The integer values are the ones on which the centre $\pm e_t$ of $G$ acts trivially, and they are the representations that descend to $SO(3)$.

## The Ladder and the Classification

The ladder operators are

$$
\tilde S_\pm=\tilde S_1\pm i\tilde S_2,\qquad [\tilde S_3,\tilde S_\pm]=\pm\tilde S_\pm,\qquad [\tilde S_+,\tilde S_-]=2\tilde S_3.
$$

**Theorem (the irreducible modules).** For every integer $n\ge0$ there is, up to isomorphism, exactly one irreducible module $\mathcal{V}_n$ of dimension $n+1$. In a basis $v_0,\dots,v_n$,

$$
\tilde S_3v_k=\bigl(k-\tfrac{n}{2}\bigr)v_k,\qquad
\tilde S_+v_k=\sqrt{(n-k)(k+1)}\,v_{k+1},\qquad
\tilde S_-v_k=\sqrt{k(n-k+1)}\,v_{k-1},
$$

with $\tilde S_+v_n=0$ and $\tilde S_-v_0=0$. The spin is $s=n/2$ and the Casimir is $s(s+1)$.

*Proof.* The preceding theorem gives existence and the dimension. The formulas are the standard ones, and they satisfy the brackets directly. Uniqueness follows because a highest-weight vector generates the module and its weight fixes $n$.

The notation $\mathcal{V}_n$ is that of *Representations of Lie Algebras*, where these modules are written $V_n$; the letter $V$ is reserved here for the traceless part of $\mathbb{B}$.

**Corollary (the Clebsch–Gordan rule).** For nonnegative integers $m,n$,

$$
\mathcal{V}_m\otimes\mathcal{V}_n\cong\bigoplus_{k=|m-n|}^{m+n}\mathcal{V}_k,
$$

the sum over $k$ of the same parity as $m+n$.

*Proof.* The tensor product is completely reducible, and its highest weight is $m+n$, with multiplicity one; removing the highest summand and repeating gives the rule.

## The Left Module: Spin One Half

The operator carries the tilde, $\tilde S_k$; the simple module and its minimal left ideals do not, and are written $S$ and $S_\pm(\vec u)$.

Let

$$
\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),\qquad S_+=\mathbb{B}\tilde\Pi_+.
$$

Then $\tilde\Pi_+$ is an idempotent of trace $1$ and rank one, and $S_+$ is a minimal left ideal, hence a simple module, of complex dimension $2$. A basis is

$$
w_+=\tilde\Pi_+,\qquad w_-=\vec\Upsilon_{-+}=\tfrac12(i\vec e_x+\vec e_y),
$$

and the action of the generators is

$$
\tilde S_3w_\pm=\pm\tfrac12 w_\pm,\qquad \tilde S_+w_+=0,\qquad \tilde S_-w_+=w_-,\qquad \tilde S_+w_-=w_+,\qquad \tilde S_-w_-=0.
$$

**Proposition.** On $S_+$, $C=\tfrac34 e_t$ and $s=\tfrac12$.

*Proof.* The weights are $\pm\tfrac12$, so $s=\tfrac12$ and $C=s(s+1)=\tfrac34$; directly, $(\tilde S_1^2+\tilde S_2^2+\tilde S_3^2)w_+=\tfrac14(1+1+1)w_+$.

**The second plane.** The idempotent $\tilde\Pi_-=\tfrac12(e_t-i\vec e_z)$ is orthogonal to $\tilde\Pi_+$, and

$$
\mathbb{B}=S_+\oplus S_-,\qquad S_\pm=\mathbb{B}\tilde\Pi_\pm.
$$

The two summands are isomorphic as $\mathbb{B}$-modules and orthogonal for the trace form.

**The copies at an axis.** For a unit real $\vec u$, put

$$
\tilde\Pi_\pm(\vec u)=\tfrac12(e_t\pm i\vec u),\qquad S_\pm(\vec u)=\mathbb{B}\tilde\Pi_\pm(\vec u).
$$

Each $S_\pm(\vec u)$ is a minimal left ideal, and $\mathbb{B}=S_+(\vec u)\oplus S_-(\vec u)$ for every $\vec u$.

**Proposition (the sphere of minimal left ideals).** The map $\vec u\mapsto S_+(\vec u)$ is a bijection from the unit sphere of $\mathfrak{g}$ onto the set of minimal left ideals of $\mathbb{B}$.

*Proof.* The minimal left ideals of $M_2(\mathbb{C})$ are the sets of matrices whose rows lie in a fixed line of $\mathbb{C}^2$, and the lines are parametrised by $\mathbb{CP}^1\cong S^2$. The idempotent $\tilde\Pi_+(\vec u)$ is the orthogonal projection onto the $+1$ eigenspace of $\vec u\cdot\vec\sigma$, and $\vec u\mapsto$ that line is the standard identification.

**Proposition (the states in a copy).** In $S_+(\vec u)$,

$$
(\vec u\cdot\vec S)\tilde\Pi_+(\vec u)=+\tfrac12\tilde\Pi_+(\vec u),\qquad
(\vec u\cdot\vec S)\tilde\Pi_-(\vec u)=-\tfrac12\tilde\Pi_-(\vec u).
$$

*Proof.* $(\vec u\cdot\vec S)\tilde\Pi_+(\vec u)=\tfrac12(i\vec u)\tfrac12(e_t+i\vec u)=\tfrac12\tilde\Pi_+(\vec u)$, because $(i\vec u)^2=+e_t$ and $i\vec u$ commutes with $\tilde\Pi_+(\vec u)$. The other sign is the same computation with $\vec u$ replaced by $-\vec u$.

The idempotent $\tilde\Pi_+(\vec u)$ is the weight $+\tfrac12$ vector of $S_+(\vec u)$, and $\tilde\Pi_-(\vec u)$ is the weight $-\tfrac12$ vector of $S_-(\vec u)$: each is a vector of its own copy, and they are not two vectors of one module. In $S_+(\vec e_z)$ the weight $-\tfrac12$ vector is $w_-$, which is nilpotent, $w_-^2=0$. The distinction is the reason the two signs label two copies and not a doublet.

**The double cover.** On $S_+$, $\exp(-2\pi i\tilde S_3)=-e_t$. On the adjoint module of the next section, $\exp(-2\pi i\operatorname{ad}_{\tilde S_3})=\operatorname{id}$. The first is the spinor sign and the second is the vector sign; the algebra produces both, and the difference is the parity of the weights.

*Proof.* The eigenvalues of $\tilde S_3$ on $S_+$ are $\pm\tfrac12$, so the exponential is $e^{\pm\pi i}=-1$. The eigenvalues of $\operatorname{ad}_{\tilde S_3}$ on $\mathbb{B}$ are $0,\pm1$, so the exponential is $1$.

## The Adjoint Module: Spins Zero and One

Conjugation, $X\mapsto uXu^{-1}$, makes $\mathbb{B}$ a module over $G$ and, differentiating, over $\mathfrak{g}$. The action of $a\in\mathfrak{g}_{\mathbb{C}}$ is $\operatorname{ad}_a$. The centre $Z=\mathbb{C}e_t$ is fixed, and the trace-zero part

$$
V=\ker\operatorname{tr}=\operatorname{span}_{\mathbb{C}}\{\vec e_x,\vec e_y,\vec e_z\}
$$

is invariant, of dimension $3$. Thus

$$
\mathbb{B}=Z\oplus V,\qquad Z\cong\mathcal{V}_0,\qquad V\cong\mathcal{V}_2.
$$

A weight basis of $V$ is

$$
v_+=\vec e_x+i\vec e_y,\qquad v_-=\vec e_x-i\vec e_y,\qquad v_0=\vec e_z,
$$

with

$$
[\tilde S_3,v_\pm]=\pm v_\pm,\qquad [\tilde S_3,v_0]=0,\qquad [\tilde S_+,v_+]=0,\qquad [\tilde S_-,v_+]=-2v_0,\qquad [\tilde S_-,v_0]=v_-.
$$

**Proposition.** On $Z$ the Casimir is $0$ and the spin is $0$; on $V$ the Casimir is $2$ and the spin is $1$.

*Proof.* The weights of $V$ are $\pm1,0$, so $s=1$ and $C=s(s+1)=2$. Directly, $\sum_k\operatorname{ad}_{\tilde S_k}^2$ acts on $v_+$ as $2v_+$ and on $v_0$ as $2v_0$.

**Remark (the highest-weight vector is nilpotent).** The vector $v_+=\vec e_x+i\vec e_y$ is a highest-weight vector of the adjoint, and $v_+^2=0$ in the algebra. The highest-weight vector of the adjoint is a nilpotent element; the same vector is not null for the trace form, which is positive definite. The two notions of length, the product and the form, must be kept apart.

**Remark (why the shortcut fails).** One cannot compute the adjoint Casimir as $\operatorname{ad}_{\tilde S_k^2}$, because $\operatorname{ad}$ is a representation of the Lie algebra and not of the associative algebra. For example,

$$
\operatorname{ad}_{\vec e_x}^2\vec e_y=[\vec e_x,[\vec e_x,\vec e_y]]=[\vec e_x,2\vec e_z]=-4\vec e_y,
\qquad
\operatorname{ad}_{\vec e_x^2}\vec e_y=\operatorname{ad}_{-e_t}\vec e_y=0.
$$

The two differ, and only the first enters the Casimir.

## The Subcarriers of the Regular Module

A **subcarrier** of the regular module is a nonzero subspace $W\subseteq\mathbb{B}$, invariant and irreducible under left multiplication or under conjugation, with the restricted action.

**Theorem (the closure of the subcarriers).** The irreducible subcarriers of $\mathbb{B}$ are:

1. under left multiplication, the minimal left ideals $S_\pm(\vec u)$, $\vec u$ a unit real vector, all isomorphic to $S\cong\mathcal{V}_1$;
2. under conjugation, $Z\cong\mathcal{V}_0$ and $V\cong\mathcal{V}_2$.

*Proof.* The left ideals of $M_2(\mathbb{C})$ are the sets of matrices whose rows lie in a fixed subspace, and the minimal ones are those whose rows lie in a line; these are the $S_\pm(\vec u)$ by the proposition above; $\mathbb{B}=S_+(\vec u)\oplus S_-(\vec u)$ for every $\vec u$. For the adjoint action, let $W$ be invariant and irreducible. If $W\subseteq V$, then $W=V$, because the string $v_+,S_-v_+,S_-^2v_+$ spans $V$. If $W$ has a nonzero component in $Z$, then either $W=Z$ (when $W\cap V=0$) or $W$ contains $Z$ and a nonzero subspace of $V$, hence contains $V$, and then $W=\mathbb{B}$, which is reducible.

**Corollary.** The spins of the irreducible subcarriers are $0$, $\tfrac12$ and $1$, of complex dimensions $1$, $2$ and $3$.

**Corollary.** No irreducible subcarrier has dimension $4$ or more. The only four-dimensional invariant subspace is $\mathbb{B}$ itself, and it is reducible in both structures: $S_+\oplus S_-$ on the left, $Z\oplus V$ under conjugation.

**The arithmetic obstruction.** Suppose one structure on $\mathbb{B}$ contained all three subcarriers. They would be distinct irreducible submodules, since their dimensions differ, and distinct irreducibles intersect trivially; their dimensions would add:

$$
1+2+3=6>4=\dim_{\mathbb{C}}\mathbb{B}.
$$

This is impossible. The three spins are the union of the constituents of two structures, not the constituents of one.

**Remark (carriers and subcarriers).** The theorem classifies the subcarriers of the regular module, not the representations of $\mathfrak{g}$. The Lie algebra has an irreducible module of every dimension, so spin $\tfrac32$ and spin $2$ are carriers in the sense of the definition; no subspace of $\mathbb{B}$ carries them. The word *subcarrier* is what the closure theorem needs, and the distinction is not a technicality: it is the difference between a representation and a representation realised inside the algebra.

## The Orbital Realisation

Let $\mathbb{C}[x,y,z]$ be the polynomial algebra, with $x,y,z$ the coordinates of $\mathbb{R}^3$. The orbital generators are

$$
L_{\mathrm{orb},k}=-i\sum_{l,m}\epsilon_{klm}x_l\,\partial/\partial x_m,
$$

that is,

$$
L_1=-i(y\,\partial/\partial z-z\,\partial/\partial y),\quad L_2=-i(z\,\partial/\partial x-x\,\partial/\partial z),\quad L_3=-i(x\,\partial/\partial y-y\,\partial/\partial x).
$$

**Proposition.** The $L_{\mathrm{orb},k}$ are derivations of $\mathbb{C}[x,y,z]$ and satisfy $[L_{\mathrm{orb},i},L_{\mathrm{orb},j}]=i\epsilon_{ijk}L_{\mathrm{orb},k}$.

*Proof.* Each is a first-order derivation. The bracket is the commutator of the corresponding vector fields; the vector fields $D_k=\sum_{l,m}\epsilon_{klm}x_l\,\partial/\partial x_m$ satisfy $[D_i,D_j]=-\epsilon_{ijk}D_k$, and the factor $(-i)^2=-1$ changes the sign.

The Casimir is

$$
L^2=L_1^2+L_2^2+L_3^2
=-\left[\frac{1}{\sin\theta}\,\partial/\partial\theta\bigl(\sin\theta\,\partial/\partial\theta\bigr)
+\frac{1}{\sin^2\theta}\,\partial^2/\partial\phi^2\right],
$$

whose eigenfunctions are the spherical harmonics, with $L^2Y_l^m=l(l+1)Y_l^m$ and $L_3Y_l^m=mY_l^m$.

**Theorem (the harmonic decomposition).** Let $\mathcal{H}_l$ be the space of harmonic polynomials of degree $l$, that is, the kernel of $\Delta=\partial^2/\partial x^2+\partial^2/\partial y^2+\partial^2/\partial z^2$ on the degree-$l$ part. Then $\mathcal{H}_l\cong\mathcal{V}_{2l}$, of dimension $2l+1$, and

$$
\mathbb{C}[x,y,z]=\bigoplus_{l\ge0}\mathcal{H}_l
$$

as $G$-modules.

*Proof.* The Laplacian maps the degree-$l$ part onto the degree-$(l-2)$ part, so $\dim\mathcal{H}_l=\binom{l+2}{2}-\binom{l}{2}=2l+1$. The polynomial $(x+iy)^l$ is harmonic, has weight $l$, and is killed by $L_+$; it is therefore a highest-weight vector of spin $l$, and the module it generates is all of $\mathcal{H}_l$.

**Remark (the orbital part is outer).** The $L_{\mathrm{orb},k}$ are derivations of the polynomial algebra and are not inner: the algebra is commutative, so $\operatorname{ad}=0$ and no element of $\mathbb{C}[x,y,z]$ acts as $L_{\mathrm{orb},k}$. The orbital angular momentum is an outer derivation; the spin angular momentum is the inner derivation $\operatorname{ad}_{\tilde S_k}$ of $\mathbb{B}$. The biquaternion algebra supplies the second and only the second.

## The Total Angular Momentum

On the tensor product $\mathcal{H}_l\otimes S$ of an orbital module and the spin-half module, the total generator is

$$
\tilde S_{\mathrm{tot},k}=L_{\mathrm{orb},k}\otimes1+1\otimes \tilde S_k.
$$

Since the two summands commute and each satisfies the angular-momentum brackets, so does the sum. The Casimir expands as

$$
C_{\mathrm{tot}}=C_L\otimes1+1\otimes C_S+2\sum_k L_{\mathrm{orb},k}\otimes \tilde S_k.
$$

The last term is the spin–orbit operator,

$$
\vec L\cdot\vec S=\sum_k L_{\mathrm{orb},k}\otimes \tilde S_k=\tfrac12\bigl(C_{\mathrm{tot}}-C_L\otimes1-1\otimes C_S\bigr).
$$

**Theorem (the addition of angular momenta).** For $l\ge1$,

$$
\mathcal{H}_l\otimes S\cong\mathcal{V}_{2l-1}\oplus\mathcal{V}_{2l+1},
$$

and for $l=0$ it is $\mathcal{V}_1$. The total spin is $s_{\mathrm{tot}}=l\pm\tfrac12$.

*Proof.* By the Clebsch–Gordan rule, $\mathcal{V}_{2l}\otimes\mathcal{V}_1=\mathcal{V}_{2l-1}\oplus\mathcal{V}_{2l+1}$ for $l\ge1$, and $\mathcal{V}_0\otimes\mathcal{V}_1=\mathcal{V}_1$.

**Corollary (the spin–orbit eigenvalues).** On the summand of total spin $s_{\mathrm{tot}}$,

$$
\vec L\cdot\vec S=\frac12\Bigl[s_{\mathrm{tot}}(s_{\mathrm{tot}}+1)-l(l+1)-\tfrac34\Bigr],
$$

that is, $+\tfrac{l}{2}$ for $s_{\mathrm{tot}}=l+\tfrac12$ and $-\tfrac{l+1}{2}$ for $s_{\mathrm{tot}}=l-\tfrac12$.

*Proof.* Evaluate the Casimir expansion on the summand.

**Remark.** The total Casimir is central in $U(\mathfrak{g})$ acting on the tensor product, but it is not a central element of $\mathbb{B}$: it contains the cross term $\sum L_{\mathrm{orb},k}\otimes \tilde S_k$. The pure-spin Casimir $\tfrac34e_t$ is a central element of the algebra itself. The two senses of *central* are different, and only the second is a statement about $\mathbb{B}$.

## Tensor Products and the Absence of Spin Two

The adjoint module is $\mathbb{B}\cong\mathcal{V}_0\oplus\mathcal{V}_2$.

**Proposition.** Its tensor square decomposes as

$$
\mathbb{B}\otimes\mathbb{B}
\cong 2\mathcal{V}_0\oplus3\mathcal{V}_2\oplus\mathcal{V}_4,
$$

of dimension $2+9+5=16$.

*Proof.* $(\mathcal{V}_0\oplus\mathcal{V}_2)^{\otimes2}=\mathcal{V}_0\oplus2\mathcal{V}_2\oplus(\mathcal{V}_2\otimes\mathcal{V}_2)$, and $\mathcal{V}_2\otimes\mathcal{V}_2=\mathcal{V}_0\oplus\mathcal{V}_2\oplus\mathcal{V}_4$.

**Theorem (multiplication kills spin two).** The multiplication map

$$
m:\mathbb{B}\otimes\mathbb{B}\longrightarrow\mathbb{B},\qquad a\otimes b\longmapsto ab
$$

is equivariant for conjugation, surjective, and its kernel is

$$
\ker m\cong\mathcal{V}_0\oplus2\mathcal{V}_2\oplus\mathcal{V}_4.
$$

In particular the unique spin-two summand $\mathcal{V}_4$ lies in the kernel.

*Proof.* For $u\in G$, $m(uau^{-1}\otimes ubu^{-1})=(uau^{-1})(ubu^{-1})=u(ab)u^{-1}$, so $m$ is equivariant. It is surjective because $m(a\otimes e_t)=a$. Since $G$ is compact, the exact sequence $0\to\ker m\to\mathbb{B}\otimes\mathbb{B}\to\mathbb{B}\to0$ splits, and the multiplicities of $\ker m$ are the differences of those of the tensor square and of $\mathbb{B}=\mathcal{V}_0\oplus\mathcal{V}_2$. The image has no $\mathcal{V}_4$, so the $\mathcal{V}_4$-isotypic component maps to zero.

**Corollary.** No product of two biquaternions has a spin-two component.

*Proof.* The image is $\mathbb{B}=\mathcal{V}_0\oplus\mathcal{V}_2$.

**Example (the highest-weight check).** The highest-weight vector of $\mathcal{V}_4$ is $v_+\otimes v_+$, of weight $2$. Its product is

$$
v_+^2=(\vec e_x+i\vec e_y)^2=\bigl(-e_t+i\vec e_z\bigr)+\bigl(-i\vec e_z+e_t\bigr)=0,
$$

and the four descendants obtained by applying $\operatorname{ad}_{\tilde S_-}\otimes1+1\otimes\operatorname{ad}_{\tilde S_-}$ also multiply to zero. This is the five-dimensional summand, and it vanishes under the product.

**Remark (why the left picture does not give the theorem).** Under left multiplication $\mathbb{B}\cong2\mathcal{V}_1$ and $\mathbb{B}\otimes\mathbb{B}\cong4(\mathcal{V}_0\oplus\mathcal{V}_2)$, but $m$ is not equivariant for that action, because $(ga)(gb)\neq g(ab)$. The argument must be run in the adjoint picture, where conjugation is an algebra automorphism.

## Real Forms and the Rotation Subgroup

The algebra is real, and its complexification by the central root of $-1$, $\tilde{Ζ}_{\mathrm{ad}}$, with $\tilde{Ζ}_{\mathrm{ad}}^2=-e_t$, is

$$
\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}\cong\mathbb{B}\oplus\mathbb{B},\qquad e_\pm=\tfrac12(e_t\pm\chi),\qquad \chi=i\tilde{Ζ}_{\mathrm{ad}},\qquad \chi^2=+e_t.
$$

The idempotents $e_\pm$ split the doubled algebra into the two chiral halves. The doubled algebra is $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}$, the same notation as in *The Unpolarized Module of the Biquaternion Algebra*. Its central root of $-1$ is $\tilde{Ζ}_{\mathrm{ad}}$, an element of the double; the spin is the real number $s$.

The rotation subgroup acts by conjugation on $\mathbb{B}$, and the two module structures of this article are its two pictures: $2\mathcal{V}_1$ on the left and $\mathcal{V}_0\oplus\mathcal{V}_2$ on the adjoint. The Lorentz group acts by the sandwich $a\mapsto gag^*$, and the two sectors $\mathbb{M}_\pm$ are the two four-vectors; the left spinor is the $(\tfrac12,0)$ and the conjugate module the $(0,\tfrac12)$. The details are in *Biquaternion Rotations and Lorentz Transformations* and in *The Unpolarized Module of the Biquaternion Algebra*; nothing in the present article depends on them.

## The Four Uses of the Word Spin

Four objects in this corpus are called a spin. They are one definition applied to two module structures, and two signs that carry no weight at all.

| use | what it labels | structure | values |
|---|---|---|---|
| highest weight | the representation | either module structure | $0,\ \tfrac12,\ 1$ |
| adjoint action | the scalar and the vector carriers | conjugation by $G$ on the algebra | $0,\ 1$ |
| Peirce index | the copy | right multiplication by $i\vec u$ | $+$ or $-$ |
| chirality | the Lorentz half | a central sign in $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}$ | $+$ or $-$ |

The first two rows are one definition read twice: conjugation is the other module structure, and applying the definition to it gives $s=0$ on $Z$ and $s=1$ on $V$. The set $\{0,\tfrac12,1\}$ is the union of the lists $2\mathcal{V}_1$ and $\mathcal{V}_0\oplus\mathcal{V}_2$, and the arithmetic obstruction above says the two lists cannot be the constituents of one action.

### The Central Sign and the Integrality Class

The $2\pi$ signs of §*The Left Module: Spin One Half* are the two integrality classes: $-e_t$ acts as $-\mathrm{id}$ on the minimal left ideals and as the identity on $Z$ and on $V$. Half-integer carriers carry the first sign, integer carriers the second.

Neither sign is an eigenvalue read off one operator on $\mathbb{B}$. In the left regular module $-e_t$ acts as $-\mathrm{id}$ on all of $\mathbb{B}$; in the adjoint action it acts trivially on all of $\mathbb{B}$. The two signs are read in the two structures, not as the two eigenspaces of one operator on the algebra.

### The Peirce Sign Is Not the Central Sign

The central element $-e_t$ acts as $-\mathrm{id}$ on $S_+$ and on $S_-$ alike, so it cannot separate them. The Peirce sign is the right multiplication $P=R_{i\vec u}$ at a unit $\vec u$. Since $(i\vec u)^2=+e_t$, $P^2=\mathrm{id}$, and

$$
P\tilde\Pi_+(\vec u)=\tilde\Pi_+(\vec u),\qquad P\tilde\Pi_-(\vec u)=-\tilde\Pi_-(\vec u),
$$

so $P$ is $+1$ on $S_+(\vec u)$ and $-1$ on $S_-(\vec u)$. It is implemented by the element $i\vec u$, which is not central: at $\vec u=\vec e_z$, $i\vec e_z\vec e_x=+i\vec e_y$ while $\vec e_x i\vec e_z=-i\vec e_y$. The Peirce index is therefore an inner, non-central copy label, and it never changes a spin value.

At a fixed axis, right multiplication by the mixed unit $\vec\Upsilon_{+-}$ carries $S_+$ onto $S_-$ and is the module isomorphism: it sends $\tilde\Pi_+$ to $\vec\Upsilon_{+-}$ and $\vec\Upsilon_{-+}$ to $\tilde\Pi_-$. Right multiplication by $\vec\Upsilon_{-+}$ annihilates $S_+$, because $\tilde\Pi_+\vec\Upsilon_{-+}=0$ and $\vec\Upsilon_{-+}^2=0$. Neither is the grading: each mixed unit squares to zero, and a nilpotent cannot be an involution.

### Chirality Is Central but Not a Spin

In the double, the chirality has the central form $\chi=i\tilde{Ζ}_{\mathrm{ad}}$, with $\chi^2=+e_t$, and its two eigenspaces are the chiral halves $e_\pm=\tfrac12(e_t\pm\chi)$ of §*Real Forms and the Rotation Subgroup*. Both halves carry the same rotation content: chirality separates the two Lorentz chiralities, not two values of $s$.

The three signs are therefore distinct. A central sign in $\mathbb{B}$ marks integer against half-integer; an inner non-central sign separates two copies of one half-integer carrier; a central sign in the double separates two Lorentz halves. Only the first tracks the integrality of a spin, and none of the three is a value of $s$.

### The Dimensions One, Two and Three as Tensor Degrees

Two descriptions of one arithmetic.

**Matrix.** A left ideal of $M_2(\mathbb{C})$ is a sum of columns, each of dimension $2$. The centre is the line of scalar matrices, and the traceless part is the complement, of dimension $4-1=3$.

**Tensor degree.** The first three tensor powers of the simple module are

$$
\mathbb{C}\ (\text{degree }0),\qquad S\ (\text{degree }1),\qquad S\otimes S\ (\text{degree }2),
$$

of dimensions $1$, $2$ and $4$. The trace form identifies $S^{*}$ with $S$, so $S\otimes S\cong\operatorname{End}_{\mathbb{C}}(S)=\mathbb{B}$, and under $G$ it splits as

$$
S\otimes S=\Lambda^2S\oplus\operatorname{sym}^2S\cong\mathbf{1}\oplus\mathbf{3}.
$$

The trivial summand is $\Lambda^2S$, spanned under the identification by the identity endomorphism; the traceless symmetric part is the adjoint $V$. The dimensions $1$, $2$, $3$ are those of the degree-$0$ object, the degree-$1$ object, and the traceless part of the degree-$2$ object.

The truncation is the same fact from the other side. The algebra is the endomorphism object of $S$, of dimension $4$, and it splits as $\mathbf{1}\oplus\mathbf{3}$; degree $3$ is $S^{\otimes3}$, of dimension $8$, and it is not a subspace of $\mathbb{B}$. Spin above one is a carrier but not a subcarrier, which is the remark that closes §*The Subcarriers of the Regular Module*.

### What the Algebra Does Not Determine

**Which structure a particle uses.** The algebra carries both lists. It does not say that the electron uses the left module and the photon the adjoint; that assignment is physics.

**No dynamics.** The Casimir is a kinematical label. No mass, no Hamiltonian and no equation of motion follow from it.

**No statistics.** The algebraic split matches the two integrality classes. The spin–statistics theorem is not proved by the algebra.

**No full Lorentz label.** Under left multiplication by $SL(2,\mathbb{C})$ the algebra carries the chiral spinor $(\tfrac12,0)$ with multiplicity two; under the Lorentz sandwich $Q\mapsto\tilde U Q\tilde U^{*}$ it carries the four-vector $(\tfrac12,\tfrac12)$, and its split into $\mathbf{1}\oplus\mathbf{3}$ is the work of the compact subgroup $G$. The rotation spin is the little-group shadow of the Lorentz label, not the whole label.

## Summary

The rotation algebra inside $\mathbb{B}$ has two normalisations: the anti-Hermitian $g_k=-\tfrac12\vec e_k$ and the Hermitian $\tilde S_k=\tfrac12 i\vec e_k$, related by $\tilde S_k=-ig_k$. The Casimir is $C=\sum \tilde S_k^2$; on an irreducible unitary carrier it is $s(s+1)$, the dimension is $2s+1$, and $s$ is the maximal weight.

| Structure | Carrier | Spin | Dimension | Casimir |
|---|---|---|---|---|
| Left multiplication | $S_\pm(\vec u)\cong\mathcal{V}_1$ | $\tfrac12$ | $2$ | $\tfrac34$ |
| Conjugation | $Z\cong\mathcal{V}_0$ | $0$ | $1$ | $0$ |
| Conjugation | $V\cong\mathcal{V}_2$ | $1$ | $3$ | $2$ |

The subcarriers of the regular module are exactly these three, and $1+2+3=6>4$ shows that no single structure contains all three. The minimal left ideals are parametrised by the sphere, and each is a copy of the spin-half module. The orbital part is an outer derivation of the polynomial algebra; the spin part is the inner derivation $\operatorname{ad}_{\tilde S_k}$.

The tensor square of the adjoint module contains a spin-two summand, and the multiplication map kills it: the product of two biquaternions carries no spin two. That vanishing is why the tensor-square route yields no fourth type; the dimension count is why no other route can.

The word spin has four uses in this corpus, and only the first two record a value of $s$. The highest weight of a module structure is the definition; the adjoint action is its instance on $\mathbb{B}=Z\oplus V$; the Peirce index and the chirality are signs, one an inner copy label and one a central Lorentz label, and neither is a value of $s$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | Its basis; $\vec e_k^2=-e_t$ |
| $\mathbb{M}_\pm$ | The Hermitian and anti-Hermitian sectors |
| $Z=\mathbb{C}e_t$ | The centre |
| $V=\ker\operatorname{tr}$ | The traceless part |
| $G=SU(2)$ | The unit real quaternions |
| $\mathfrak{g}=\mathfrak{su}(2)$ | The real pure quaternions |
| $g_k=-\tfrac12\vec e_k$ | The anti-Hermitian generators |
| $\tilde S_k=\tfrac12 i\vec e_k$ | The Hermitian generators |
| $C=\tilde S_1^2+\tilde S_2^2+\tilde S_3^2$ | The Casimir |
| $s$ | The spin, the maximal weight |
| $\mathcal{V}_n$ | The irreducible module of dimension $n+1$ |
| $S_\pm(\vec u)=\mathbb{B}\tilde\Pi_\pm(\vec u)$ | The minimal left ideals at the axis $\vec u$ |
| $\tilde\Pi_\pm(\vec u)=\tfrac12(e_t\pm i\vec u)$ | The rank-one idempotents |
| $R_{Q}$ | Right multiplication by $Q$ |
| $\vec\Upsilon_{+-}=\tfrac12(i\vec e_x-\vec e_y)$ | The nilpotent weight $+\tfrac12$ vector of $S_-$ |
| $\vec\Upsilon_{-+}=\tfrac12(i\vec e_x+\vec e_y)$ | The nilpotent weight $-\tfrac12$ vector of $S_+$ |
| $v_+=\vec e_x+i\vec e_y$ | The highest-weight vector of $V$ |
| $L_{\mathrm{orb},k}=-i\sum_{l,m}\epsilon_{klm}x_l\,\partial/\partial x_m$ | The orbital generators |
| $\mathcal{H}_l$ | The harmonic polynomials of degree $l$ |

## Further Reading

- [The Category of Modules in the Biquaternion Algebra](the-category-of-modules.html), for the simple module and the classification of the modules.
- [The Polarized Module of the Biquaternion Algebra](the-polarized-module-of-the-biquaternion-algebra.html), for the decomposition ${}_\mathbb{B}\mathbb{B}\cong S\oplus S$; the spinor spaces and the ladder.
- [The Casimir Operator](the-casimir-operator.html), for the Casimir in the general theory.
- [Representations of Lie Algebras](representations-of-lie-algebras.html), for the highest-weight classification and the Clebsch–Gordan rule.
- [The Tensor Square of the Duo-Complex Numbers](the-tensor-square-of-c2.html), for the decomposition of the tensor square.
- [The Unpolarized Module of the Biquaternion Algebra](the-unpolarized-module-of-the-biquaternion-algebra.html), for the central sign and the conjugate module.
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the Lorentz action and its labels.
- [Angular Momentum and Spin in Biquaternionic Form](../articles_physics/angular-momentum-and-spin-in-biquaternionic-form.html), for the physics counterpart and the units.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the highest-weight theorem and the Casimir.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for $\mathfrak{sl}_2$, the Clebsch–Gordan rule and the harmonic decomposition.
