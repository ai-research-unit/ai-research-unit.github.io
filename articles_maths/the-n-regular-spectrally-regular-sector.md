# __The N-Regular, Spectrally Regular Sector__

## Introduction

This is cell $11$ of the four-sector arrangement of the two quadratic conditions

$$
\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2,\qquad B^2=Q_x^2+Q_y^2+Q_z^2,
$$

the sector on which neither vanishes. It is the complement of the union of the two cones,

$$
\Sigma_{11}=\mathbb{B}\setminus(\mathcal N\cup\mathcal S),
$$

and it is the **generic** sector: the open dense cell in which both problems of the arrangement receive the positive answer. The other three cells are the mixed sectors $\Sigma_{10}=\mathcal S\setminus\mathcal N$ and $\Sigma_{01}=\mathcal N\setminus\mathcal S$, and the doubly degenerate cell $\Sigma_{00}=\mathcal N\cap\mathcal S$, treated in *The N-Regular, Spectrally Degenerate Sector*, *The N-Degenerate, Spectrally Regular Sector* and *The N-Degenerate, Spectrally Degenerate Sector*. The vocabulary, the two cones and the naming convention are those of *N-Regularity and N-Degeneracy in the Biquaternion Algebra* and *The Spectrum*.

Throughout, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $\vec e_k^2=-e_t$, and $\tilde Q=Q_te_t+\vec Q$; the conjugation is ${}^{\natural}$; the quaternionic norm is $\langle\tilde Q\rangle_{\natural}=\tilde Q^{\natural}\tilde Q$, central; and the product is the plain product unless stated otherwise. The null cone is $\mathcal N=\{N=0\}$; the spectral-degenerate cone is $\mathcal S=\{B^2=0\}$; **regular** means non-zero: $\langle\tilde Q\rangle_{\natural}\neq0$ for the norm, $B^2\neq0$ for the spectrum.

## Definition and Characterisation

**Definition.** The sector $\Sigma_{11}$ is

$$
\Sigma_{11}=\{N\neq0,\ B^2\neq0\}.
$$

**Theorem (five descriptions).** For $\tilde Q\in\mathbb{B}$ the following are equivalent:

(i) $\tilde Q\in\Sigma_{11}$;

(ii) $\tilde Q$ is a unit and its two eigenvalues are distinct;

(iii) $\tilde Q$ is a unit and is semisimple with a non-scalar spectrum;

(iv) $\tilde Q$ admits a spectral decomposition into two non-trivial idempotents with distinct non-zero coefficients;

(v) $\tilde Q$ is invertible, non-scalar, and admits a Peirce decomposition with idempotents commuting with it.

*Proof.* (i) $\iff$ (ii): $\langle\tilde Q\rangle_{\natural}\neq0$ is the unit condition, and $B^2\neq0$ is the discriminant condition, so the eigenvalues $\lambda_\pm=Q_t\pm\beta$, with $\beta=iB$ and $B^2\neq0$, are distinct; conversely distinct eigenvalues give $B^2\neq0$ and $\langle\tilde Q\rangle_{\natural}=\lambda_+\lambda_-\neq0$ makes the element a unit.

(ii) $\iff$ (iii): in two dimensions a semisimple element with a repeated eigenvalue is a scalar, so semisimplicity with a non-scalar spectrum is the same as two distinct eigenvalues.

(ii) $\iff$ (iv): with distinct eigenvalues the spectral idempotents $e_\pm$ exist, are non-trivial, and are unique; the coefficients $\lambda_\pm$ are distinct and non-zero because $\langle\tilde Q\rangle_{\natural}=\lambda_+\lambda_-\neq0$. Conversely such a decomposition exhibits two distinct eigenvalues and a non-zero norm.

(i) $\iff$ (v): for a non-scalar element a Peirce decomposition relative to $\tilde Q$ exists exactly when $B^2\neq0$, by the existence theorem of *The Spectrum*; invertibility is exactly $\langle\tilde Q\rangle_{\natural}\neq0$. So both conditions together are exactly (i).

**Corollary (regular semisimple units).** The sector is the set of regular semisimple elements of the unit group:

$$
\Sigma_{11}=\{\tilde Q\in\mathbb{B}^\times\ :\ \lambda_+\neq\lambda_-\},
$$

with $\mathbb{B}^\times=\{N\neq0\}$ the unit group. Its complement in $\mathbb{B}^\times$ is the degenerate half $\Sigma_{10}$, so the unit group splits into a generic part and a unipotent part.

**Corollary (eigenvalue parametrisation).** Every element of the sector is written uniquely as

$$
\tilde Q=\lambda_+e_++\lambda_-e_-,\qquad
\lambda_\pm\in\mathbb{C}^\times,\quad \lambda_+\neq\lambda_-,
$$

with $e_\pm$ the spectral idempotents, $e_+^2=e_+$, $e_-^2=e_-$, $e_+e_-=0$, $e_++e_-=e_t$. Conversely every such choice gives an element of $\Sigma_{11}$. In these terms

$$
Q_t=\frac{\lambda_++\lambda_-}{2},\qquad
B^2=-\left(\frac{\lambda_+-\lambda_-}{2}\right)^2,\qquad
N=\lambda_+\lambda_-.
$$

The two invariants are therefore the two elementary symmetric functions of the spectrum: $\langle\tilde Q\rangle_{\natural}$ is the product, and $B^2$ is minus a quarter of the squared difference.

**Corollary (complement of a hypersurface).** $\Sigma_{11}$ is the complement of the hypersurface $\langle\tilde Q\rangle_{\natural}\,B^2=0$, the union of the two cones. It is Zariski-open and dense in $\mathbb{B}$.

## Geometry

**Theorem (open dense, of full measure).** $\Sigma_{11}$ is open and dense in $\mathbb{B}$, of complex dimension $4$ and real dimension $8$. Its complement $\mathcal N\cup\mathcal S$ is a complex hypersurface, of complex dimension $3$ and real dimension $6$, hence of real codimension $2$ and Lebesgue measure zero.

*Proof.* The functions $\langle\tilde Q\rangle_{\natural}$ and $B^2$ are non-zero polynomials in four complex variables, so each zero locus is a complex hypersurface, and so is their union; the complement is open and dense. The dimension of the complement is $4-1=3$ over $\mathbb{C}$, that of the sector $4$ over $\mathbb{C}$ and $8$ over $\mathbb{R}$. A complex hypersurface in $\mathbb{C}^4$ has real codimension $2$ and measure zero.

**Proposition (connected).** $\Sigma_{11}$ is connected.

*Proof.* By the eigenvalue parametrisation, $\Sigma_{11}$ is the image of the connected parameter space

$$
\{(\lambda_+,\lambda_-,e_+):\ \lambda_\pm\neq0,\ \lambda_+\neq\lambda_-,\ e_+\text{ a non-trivial idempotent}\}
$$

under the continuous map $(\lambda_+,\lambda_-,e_+)\mapsto\lambda_+e_++\lambda_-e_-$. The eigenvalue parameter space is $\mathbb{C}^2$ minus the diagonal and the two axes, three complex lines through the origin, and its complement is connected. The non-trivial idempotents are $e_+=(e_t+\tilde\Xi)/2$ with $\tilde\Xi^2=e_t$ and $\tilde\Xi\neq\pm e_t$; the quadric $\tilde\Xi^2=e_t$ is a smooth connected complex surface, and deleting the two points $\pm e_t$ leaves it connected. A continuous image of a connected space is connected.

**Proposition (not simply connected).** $\Sigma_{11}$ has non-trivial fundamental group.

*Proof.* For $\varepsilon\neq0$ consider the loop

$$
\tilde Q(t)=e_t+\varepsilon e^{2\pi it}\vec e_x,\qquad 0\le t\le1.
$$

Its invariants are

$$
\langle\tilde Q(t\rangle_{\natural})=1+\varepsilon^2e^{4\pi it},\qquad B^2(\tilde Q(t))=\varepsilon^2e^{4\pi it},
$$

both non-zero, so the loop lies in $\Sigma_{11}$. The continuous map $\tilde Q\mapsto(\langle\tilde Q\rangle_{\natural},B^2(\tilde Q))$ sends $\Sigma_{11}$ to $\mathbb{C}^\times\times\mathbb{C}^\times$ and sends this loop to one whose two components wind twice around $1$ and around $0$ respectively. That image is not null-homotopic in the torus, so the loop is not null-homotopic in $\Sigma_{11}$.

**Remark (the identity is not generic).** $e_t$ has $B^2=0$, so it lies in $\Sigma_{10}$, not in $\Sigma_{11}$. The sector is not a neighbourhood of the identity and not a subgroup; it is the part of the unit group on which the discriminant does not vanish. Likewise the scalar line $\mathbb{C}^\times e_t$ is entirely outside the sector.

**Remark (where $Q_t$ may vanish).** The sector meets the hyperplane $Q_t=0$: the pure vectors with $B^2\neq0$, such as $\vec e_x+\vec e_y$, have $\langle\tilde Q\rangle_{\natural}=B^2\neq0$ and lie in $\Sigma_{11}$. For such an element the two eigenvalues are opposite, $\lambda_-=-\lambda_+$, and its square is a non-zero scalar. So the sector is not characterised by a non-zero scalar part, only by the non-vanishing of both invariants.

## The Elements

Let $\tilde Q\in\Sigma_{11}$, with $\beta=iB$, $B$ a fixed square root of $B^2$, and eigenvalues $\lambda_\pm=Q_t\pm\beta$. The other square root replaces $\beta$ by $-\beta$ and exchanges the two eigenvalues.

**Spectrum and minimal polynomial.** The spectrum is $\{\lambda_+,\lambda_-\}$, with $\lambda_+\neq\lambda_-$ and $\lambda_+\lambda_-=N\neq0$. The characteristic and minimal polynomial is

$$
p(X)=X^2-2Q_tX+N,
$$

squarefree, with discriminant $-4B^2\neq0$. The element is semisimple, and regular semisimple: its centraliser has the minimal possible dimension among non-scalar elements.

**Centraliser.** Evaluation gives

$$
\mathbb{C}[\tilde Q]\cong\mathbb{C}[X]/(p)\cong\mathbb{C}\oplus\mathbb{C},
$$

of complex dimension $2$. Under the isomorphism $\mathbb{C}[\tilde Q]\cong\mathbb{C}\oplus\mathbb{C}$ the idempotents correspond to $(0,0)$, $(1,0)$, $(0,1)$ and $(1,1)$, so they are exactly $0$, $e_+$, $e_-$ and $e_t$.

**Spectral idempotents.** They are unique and given by the Lagrange formula

$$
e_\pm=\frac{\tilde Q-\lambda_\mp e_t}{\lambda_\pm-\lambda_\mp},
$$

with $e_\pm^2=e_\pm$, $e_+e_-=0$, $e_++e_-=e_t$, $\tilde Qe_\pm=\lambda_\pm e_\pm$. Each is a non-trivial idempotent, since $\lambda_+\neq\lambda_-$ and $\tilde Q$ is not a scalar.

**Adapted Peirce decomposition.** Relative to $(e_+,e_-)$ the Peirce form is diagonal with both diagonal entries non-zero:

$$
e_+\tilde Qe_+=\lambda_+e_+,\qquad
e_+\tilde Qe_-=0,\qquad
e_-\tilde Qe_+=0,\qquad
e_-\tilde Qe_-=\lambda_-e_-.
$$

This is the only sector in which the Peirce decomposition relative to $\tilde Q$ has two non-zero coefficients and two non-trivial idempotents. In $\Sigma_{01}$ one coefficient vanishes; on the scalar line of $\Sigma_{10}$ the two coefficients coincide and the refinement is non-unique; in $\Sigma_{10}^{\mathrm{J}}$ and in $\Sigma_{00}\setminus\{0\}$ no Peirce decomposition relative to $\tilde Q$ exists.

**The spectral decomposition.** The two-term writing
$$
\tilde Q=\lambda_+e_++\lambda_-e_-,\qquad \lambda_\pm=Q_t\pm\beta,\quad \beta=iB,
$$
is the eigenvalue decomposition of $\tilde Q$. It exists because the minimal polynomial is split and squarefree, and it is unique: the eigenvalues are distinct, so the spectral idempotents are determined by $\tilde Q$. The eigenbasis construction — the eigenbasis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ and the diagonalisation of $L_{\tilde Q}$ — is in §*The Eigenbasis, the Nilpotents, and the Peirce Corners*; the general construction is in *The Eigenbasis of a Spectrally Regular Biquaternion*, §*The Eigenbasis*.

**Powers, inverse, and the eigenvalue map.** For every polynomial $f\in\mathbb{C}[X]$,
$$
f(\tilde Q)=f(\lambda_+)e_++f(\lambda_-)e_-,\qquad
\tilde Q^{-1}=\lambda_+^{-1}e_++\lambda_-^{-1}e_-,
$$
the second because $\lambda_+\lambda_-=N\neq0$; it agrees with $\tilde Q^{\natural}/N$, since $\lambda_-\tilde\Pi_++\lambda_+\tilde\Pi_-=\tilde Q^{\natural}$. The eigenvalue map $\mathbb{B}^\times\to\mathbb{C}^\times\times\mathbb{C}^\times$, $\tilde Q\mapsto(\lambda_+,\lambda_-)$, is surjective, not injective and not a group homomorphism.

**Annihilators.** Since $\tilde Q$ is a unit,

$$
A(\tilde Q)=B(\tilde Q)=\{0\},
$$

and left and right multiplication are bijections of $\mathbb{B}\cong\mathbb{C}^4$, of complex rank $4$.

**Inverse.** $\tilde Q^{-1}=\tilde Q^{\natural}/N$, and

$$
\langle\tilde Q^{-1}\rangle_{\natural}=\frac{1}{\langle\tilde Q\rangle_{\natural}},\qquad
B^2(\tilde Q^{-1})=\frac{B^2(\tilde Q)}{\langle\tilde Q\rangle_{\natural}^2}\neq0,
$$

so the inverse lies in the sector.

## The Eigenbasis, the Nilpotents, and the Peirce Corners

**Every $\tilde Q\in\Sigma_{11}$ has $B^2\neq0$. Its own root carries a Peirce pair, the two mixed corners carry a pair of nilpotents, and the four elements form a basis in which left multiplication by $\tilde Q$ is diagonal. The basis is a normalised Peirce eigenbasis of left multiplication; the two minimal left ideals are the eigenspaces of right multiplication, not of left multiplication.** This is the Q-dependent specialisation of the Peirce decomposition of *The Peirce Decomposition of the Biquaternion Algebra*, §*The Peirce Decompositions*: the four corner lines are the same construction, read relative to the pair of $\tilde Q$'s own root. The general construction, its normalisation and the expansion of an arbitrary biquaternion are in *The Eigenbasis of a Spectrally Regular Biquaternion*.

### The Root, the Idempotents, and the Eigenvalues

Let
$$
\tilde Q=Q_te_t+\vec Q,\qquad
\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,\qquad
B^2\neq0,
$$
and fix a square root $B$ of $B^2$, with $\beta=iB$. Define
$$
\vec U=\frac{\vec Q}{B},\qquad
\vec\Xi=-i\vec U=-\frac{i\vec Q}{B},\qquad
\tilde\Pi_\pm=\frac{e_t\pm\vec\Xi}{2},\qquad
\lambda_\pm=Q_t\pm \beta.
$$
Then
$$
\vec\Xi^2=e_t,\qquad
\tilde\Pi_\pm^2=\tilde\Pi_\pm,\qquad
\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0,\qquad
\tilde\Pi_++\tilde\Pi_-=e_t,
$$
and
$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-.
$$
The pair $\tilde\Pi_\pm$ is the pair denoted $e_\pm$ in §*The Elements*; the two notations are the same spectral idempotents.

The pair $(\tilde\Pi_+,\tilde\Pi_-)$ is attached to $\tilde Q$: it is the pair of the root $\vec\Xi$, not an arbitrary pair of idempotents. The signs are fixed by
$$
\vec\Xi\tilde\Pi_\pm=\tilde\Pi_\pm\vec\Xi=\pm\tilde\Pi_\pm,\qquad
\tilde Q\tilde\Pi_\pm=\lambda_\pm\tilde\Pi_\pm.
$$
Choosing the negative square root sends $\vec\Xi$ to $-\vec\Xi$, exchanges $\tilde\Pi_+$ and $\tilde\Pi_-$, and exchanges $\lambda_+$ and $\lambda_-$; the unordered pair and the unordered spectrum are unchanged.

### The Peirce Corners and the Nilpotents

Define the four **Peirce corners**
$$
\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\tilde\Pi_t,\qquad s,t\in\{+,-\}.
$$
Each is one complex line. The two diagonal corners are the lines of the idempotents, and the two mixed corners are square-zero: an element $x\in\mathbb{B}_{st}$ with $s\neq t$ has zero scalar part, because its trace is zero, and its square is zero, because
$$
x^2\in\tilde\Pi_s\mathbb{B}\tilde\Pi_t\tilde\Pi_s\mathbb{B}\tilde\Pi_t=0
\qquad(s\neq t).
$$

**Construction of the two nilpotents.** Choose a nonzero
$$
\vec\Upsilon_+\in\mathbb{B}_{-+}=\tilde\Pi_-\mathbb{B}\tilde\Pi_+.
$$
Consider the map
$$
\mathbb{B}_{+-}\longrightarrow\mathbb{C}\tilde\Pi_-,\qquad x\longmapsto\vec\Upsilon_+x.
$$
It is linear between complex lines, and it is nonzero. Otherwise $\vec\Upsilon_+x=0$ for every $x\in\mathbb{B}_{+-}$, hence $\vec\Upsilon_+\tilde\Pi_-\mathbb{B}\tilde\Pi_-=0$, and then $\mathbb{B}\vec\Upsilon_+\mathbb{B}\tilde\Pi_-=0$. But $\vec\Upsilon_+\neq0$, so the two-sided ideal $\mathbb{B}\vec\Upsilon_+\mathbb{B}$ is the whole simple algebra $\mathbb{B}$, and $\mathbb{B}\tilde\Pi_-\neq0$, a contradiction. A nonzero linear map between complex lines is an isomorphism. Hence there is a unique
$$
\vec\Upsilon_-\in\mathbb{B}_{+-}
\qquad\text{with}\qquad
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-.
$$
The other product is then forced. It lies in $\mathbb{C}\tilde\Pi_+$, say $\vec\Upsilon_-\vec\Upsilon_+=\alpha\tilde\Pi_+$, and
$$
\vec\Upsilon_+=\tilde\Pi_-\vec\Upsilon_+=\vec\Upsilon_+(\vec\Upsilon_-\vec\Upsilon_+)=\alpha\vec\Upsilon_+\tilde\Pi_+=\alpha\vec\Upsilon_+,
$$
so $\alpha=1$. Therefore
$$
\boxed{\ \vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_+^2=\vec\Upsilon_-^2=0.\ }
$$
**The two-line normalisation.** If one starts from arbitrary nonzero $u\in\mathbb{B}_{-+}$ and $v\in\mathbb{B}_{+-}$, then $uv=c\tilde\Pi_-$ for some $c\neq0$. Choose $\alpha$ with $\alpha^2=c$ and set $\vec\Upsilon_+=u/\alpha$, $\vec\Upsilon_-=v/\alpha$; the argument above applied to $u/\alpha$ and $v/\alpha$ gives $vu=c\tilde\Pi_+$, and the boxed identities hold. This is the same construction read from two arbitrary generators instead of one, and the residual freedom is the reciprocal rescaling of the pair.

The construction from $\vec\Upsilon_+$ alone makes one choice, the nonzero element $\vec\Upsilon_+$ of the line $\mathbb{B}_{-+}$. That choice determines $\vec\Upsilon_-$ uniquely. In that construction no intermediate scalar and no square root enter. A square root appears when the pair is parametrised by two arbitrary generators, as in the two-line normalisation above, or by a transverse vector, as in the closed forms below.

The corners and their generators are collected in the table.

| Corner | Definition | Generator |
|---|---|---|
| $\mathbb{B}_{++}$ | $\tilde\Pi_+\mathbb{B}\tilde\Pi_+$ | $\tilde\Pi_+$ |
| $\mathbb{B}_{+-}$ | $\tilde\Pi_+\mathbb{B}\tilde\Pi_-$ | $\vec\Upsilon_-$ |
| $\mathbb{B}_{-+}$ | $\tilde\Pi_-\mathbb{B}\tilde\Pi_+$ | $\vec\Upsilon_+$ |
| $\mathbb{B}_{--}$ | $\tilde\Pi_-\mathbb{B}\tilde\Pi_-$ | $\tilde\Pi_-$ |

**The two signs.** The index is fixed by the left ideal, not by the corner: $\vec\Upsilon_+$ lies in $\mathbb{B}_{-+}$ and, together with $\tilde\Pi_+$, generates $S_+=\mathbb{B}\tilde\Pi_+$; $\vec\Upsilon_-$ lies in $\mathbb{B}_{+-}$ and, together with $\tilde\Pi_-$, generates $S_-=\mathbb{B}\tilde\Pi_-$. Thus
$$
S_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,\qquad
S_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-.
$$

**Uniqueness up to rescaling.** The pair is determined by the products and squares only up to
$$
\vec\Upsilon_+\longmapsto\mu\,\vec\Upsilon_+,\qquad
\vec\Upsilon_-\longmapsto\mu^{-1}\vec\Upsilon_-,\qquad
\mu\in\mathbb{C}^{\times},
$$
which preserves both products and both squares. Indeed, $\mu^{-1}\vec\Upsilon_-$ is the unique element of $\mathbb{B}_{+-}$ whose product with $\mu\vec\Upsilon_+$ is $\tilde\Pi_-$, so the construction forces $\vec\Upsilon_-'=\mu^{-1}\vec\Upsilon_-$. Conversely every pair with the same products and squares arises this way, because the mixed corners are lines. The construction therefore defines the pair up to this one rescaling, and no further choice enters.

**The corner, without a preferred axis.** For every pure biquaternion $\vec X$,
$$
\tilde\Pi_-\vec X\tilde\Pi_+=\frac12\left(\vec X_\perp+i\,\vec U\times\vec X\right)
=\frac12\left(\vec X-\frac{\vec X\cdot\vec Q}{B^2}\vec Q\right)+\frac{i}{4B}\,[\vec Q,\vec X],
$$
$$
\tilde\Pi_+\vec X\tilde\Pi_-=\frac12\left(\vec X_\perp-i\,\vec U\times\vec X\right)
=\frac12\left(\vec X-\frac{\vec X\cdot\vec Q}{B^2}\vec Q\right)-\frac{i}{4B}\,[\vec Q,\vec X],
$$
where $\vec X_\perp=\vec X-\dfrac{\vec X\cdot\vec Q}{B^2}\vec Q$. No axis is singled out. When $\vec X_\perp^2\neq0$ both projections are nonzero.

**The two nilpotents from a transverse vector.** Let $\vec X$ be a pure vector with $\vec X_\perp^2\neq0$, and put
$$
u_+=\tilde\Pi_-\vec X\tilde\Pi_+,\qquad u_-=\tilde\Pi_+\vec X\tilde\Pi_-.
$$
Then
$$
u_+u_-=\vec X_\perp^2\,\tilde\Pi_-,\qquad
u_-u_+=\vec X_\perp^2\,\tilde\Pi_+,\qquad
u_\pm^2=0,
$$
as the expansion of the two projections shows: the cross terms cancel because $\vec X_\perp\cdot(\vec U\times\vec X_\perp)=0$. Then
$$
\vec\Upsilon_\pm=\frac{u_\pm}{\sqrt{\vec X_\perp^2}}
$$
satisfy $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$, $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$, $\vec\Upsilon_\pm^2=0$. Every admissible pair arises this way, and two choices of $\vec X$ give pairs differing by the reciprocal rescaling. The scalar is
$$
\vec X_\perp^2=\vec X^2+\frac{(\vec X\cdot\vec Q)^2}{B^2}.
$$

**The transverse unit vector.** If $\vec V$ is a pure unit vector with $\vec V\cdot\vec U=0$, then $\vec V\tilde\Pi_+\in\mathbb{B}_{-+}$ and $\vec V\tilde\Pi_-\in\mathbb{B}_{+-}$, and, up to the reciprocal rescaling,
$$
\vec\Upsilon_+=i\,\vec V\tilde\Pi_+,\qquad
\vec\Upsilon_-=i\,\vec V\tilde\Pi_-.
$$
For $\vec V=\vec e_x$ and $\vec U=\vec e_z$ one has $\vec V\tilde\Pi_+=(\vec e_x+i\vec e_y)/2$ and $\vec V\tilde\Pi_-=(\vec e_x-i\vec e_y)/2$, and direct multiplication, using $\vec V^2=-e_t$, gives
$$
(\vec V\tilde\Pi_+)(\vec V\tilde\Pi_-)=-\tilde\Pi_-,
\qquad
(\vec V\tilde\Pi_-)(\vec V\tilde\Pi_+)=-\tilde\Pi_+.
$$
A general transverse unit is $\vec V=\lambda\vec e_x+\mu\vec e_y$ with $\lambda^2+\mu^2=1$; the factor $\lambda-i\mu$ cancels in the normalised pair, so the same products hold. The factor $i$ on both generators restores the plus signs. This is the transverse-vector construction with $\vec X=\vec V$ and $\sqrt{\vec V_\perp^2}=i$.

**The symmetric closed form.** The vector $\vec w=\vec e_x+\vec e_y+\vec e_z$ is the only nonzero vector fixed by every permutation of the axes. Put $\Sigma=\vec w\cdot\vec Q=Q_x+Q_y+Q_z$. Then
$$
\vec w_\perp=\vec w-\frac{\Sigma}{B^2}\vec Q,\qquad
\vec w_\perp^2=\vec w^2+\frac{\Sigma^2}{B^2}=-3+\frac{\Sigma^2}{B^2}=\frac{\Sigma^2-3B^2}{B^2}.
$$
Therefore
$$
\boxed{\ \vec\Upsilon_\pm=\frac{B\,\vec w-\dfrac{\Sigma}{B}\,\vec Q\pm\dfrac{i}{2}\,[\vec Q,\vec w]}{2\sqrt{\Sigma^2-3B^2}}\ }
$$
with $\vec w=\vec e_x+\vec e_y+\vec e_z$ and $\Sigma=Q_x+Q_y+Q_z$. In full coordinates,
$$
\vec\Upsilon_\pm=\frac{\Bigl(B-\dfrac{\Sigma Q_x}{B}\pm i(Q_y-Q_z)\Bigr)\vec e_x+\Bigl(B-\dfrac{\Sigma Q_y}{B}\pm i(Q_z-Q_x)\Bigr)\vec e_y+\Bigl(B-\dfrac{\Sigma Q_z}{B}\pm i(Q_x-Q_y)\Bigr)\vec e_z}{2\sqrt{\Sigma^2-3B^2}}.
$$
A permutation of the axes permutes the three components and leaves $B$ and $\Sigma$ unchanged, so the formula is symmetric in $x,y,z$. Expanding the brackets gives
$$
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_\pm^2=0,
$$
and the denominator is
$$
2\sqrt{\Sigma^2-3B^2}=2\sqrt{-\bigl((Q_x-Q_y)^2+(Q_y-Q_z)^2+(Q_z-Q_x)^2\bigr)}.
$$

**The exceptional cone and the chart.** The symmetric formula degenerates exactly on the cone
$$
\Sigma^2=3B^2,
\qquad\text{that is,}\qquad
(Q_x-Q_y)^2+(Q_y-Q_z)^2+(Q_z-Q_x)^2=0,
$$
which for real $\vec Q$ is the line $Q_x=Q_y=Q_z$. On that cone use the axis chart: for $\mu\in\{x,y,z\}$,
$$
\vec\Upsilon_\pm=\frac{B\,\vec e_\mu-\dfrac{Q_\mu}{B}\,\vec Q\pm\dfrac{i}{2}\,[\vec Q,\vec e_\mu]}{2\sqrt{Q_\mu^2-B^2}},
$$
which is the transverse-vector construction with $\vec X=\vec e_\mu$. The chart with axis $\mu$ is defined when $Q_\mu^2\neq B^2$, that is, when $Q_\nu^2+Q_\rho^2\neq0$ for the two other coordinates. At least one of the three is defined whenever $B\neq0$: if all three failed, then $Q_x^2+Q_y^2=Q_y^2+Q_z^2=Q_z^2+Q_x^2=0$, hence $Q_x^2=Q_y^2=Q_z^2$ and $2Q_x^2=0$, so $B=0$. The charts are the one formula read with $\mu=x,y,z$, and the ones that are defined give pairs differing by the reciprocal rescaling. The symmetric formula off the cone and the axis charts on it cover every $\vec Q$ with $B\neq0$.

**The normalisation.** The symmetric formula off the exceptional cone, the axis chart on it and one fixed branch of the square root are the normalisation of *The Eigenbasis of a Spectrally Regular Biquaternion*, §*The Transverse-Vector Construction*: they fix the scale of the pair, and with them the quadruple $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ is unique. Without this choice the pair is determined only up to the reciprocal rescaling of the theorem above.

**Why no formula is axis-free everywhere.** A closed form with no auxiliary vector would be a map $F$ with $F(S\vec Q)=S\,F(\vec Q)$ for every rotation $S$, rational in $\vec Q$ and $B$. By invariant theory the only such maps are $F(\vec Q)=f(B^2)\vec Q$: the invariant tensors are $\delta_{ij}$ and $\epsilon_{ijk}$, and $\epsilon$ cannot build a vector from a single vector. But the corner is transverse to $\vec Q$, so $F$ would vanish. Every explicit generator therefore uses an auxiliary vector: the symmetric formula uses the permutation-invariant $\vec w$, the axis charts use $\vec e_x,\vec e_y,\vec e_z$. The corner line is a spinor line, and a spinor is not a function of $\vec Q$ alone.

**The standard pair.** For the opposite root, $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$, the corner generators of *The Peirce Decomposition of the Biquaternion Algebra*, §*The Biquaternion Case*, are
$$
\vec\Upsilon_x=\frac{i\vec e_x-\vec e_y}{2}\in\mathbb{B}_{+-},\qquad
\vec\Upsilon_y=\frac{i\vec e_x+\vec e_y}{2}\in\mathbb{B}_{-+},
$$
with $\vec\Upsilon_x\vec\Upsilon_y=\tilde\Pi_+$ and $\vec\Upsilon_y\vec\Upsilon_x=\tilde\Pi_-$. These are the $\vec\Upsilon_1,\vec\Upsilon_2$ of *Conventions of the Special Elements*, §*The Nilpotent Convention*, indexed by direction. The present root is $\vec\Xi=-i\vec e_z$ when $Q_z>0$ with the choice $B=Q_z$, which is the negative of that one; the two corner labels and the two idempotent labels are therefore exchanged. In the present indexing
$$
\vec\Upsilon_+=\vec\Upsilon_x,\qquad \vec\Upsilon_-=\vec\Upsilon_y,
$$
and the products are $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$, $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$, as required.

### The Eigenbasis

The four elements
$$
\tilde\Pi_+,\qquad \vec\Upsilon_-,\qquad \vec\Upsilon_+,\qquad \tilde\Pi_-
$$
form a $\mathbb{C}$-basis of $\mathbb{B}$. It is the **eigenbasis of $L_{\tilde Q}$**. In this basis the multiplication by $\tilde Q$ is diagonal:
$$
\tilde Q\tilde\Pi_+=\lambda_+\tilde\Pi_+,\qquad
\tilde Q\vec\Upsilon_-=\lambda_+\vec\Upsilon_-,\qquad
\tilde Q\vec\Upsilon_+=\lambda_-\vec\Upsilon_+,\qquad
\tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_-.
$$
The diagonal values are
$$
\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-).
$$
The reason is the corner rule: an element of $\mathbb{B}_{st}$ has left sign $s$ and right sign $t$ under multiplication by the root $\vec\Xi$, and $\tilde Q=Q_te_t+\beta\,\vec\Xi$ acts on it on the left by $Q_t+i\,sB=\lambda_s$ and on the right by $Q_t+i\,tB=\lambda_t$. The four basis elements, their corners, and the two diagonal readings are collected in the table.

| Basis element | Corner | Left eigenvalue $L_{\tilde Q}$ | Right eigenvalue $R_{\tilde Q}$ |
|---|---|---|---|
| $\tilde\Pi_+$ | $\mathbb{B}_{++}$ | $\lambda_+$ | $\lambda_+$ |
| $\vec\Upsilon_-$ | $\mathbb{B}_{+-}$ | $\lambda_+$ | $\lambda_-$ |
| $\vec\Upsilon_+$ | $\mathbb{B}_{-+}$ | $\lambda_-$ | $\lambda_+$ |
| $\tilde\Pi_-$ | $\mathbb{B}_{--}$ | $\lambda_-$ | $\lambda_-$ |

Thus the left action is diagonal with the values $\lambda_+,\lambda_+,\lambda_-,\lambda_-$, and the right action is diagonal with the values $\lambda_+,\lambda_-,\lambda_+,\lambda_-$, in the same basis.

### The Action of the Four Basis Elements

**In the eigenbasis $\mathcal{B}=(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ the multiplication of the four basis elements is the table, and the left and right actions on the basis are read from it.**

The multiplication is the table.

| $PX$ | $\tilde\Pi_+$ | $\vec\Upsilon_-$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ |
|---|---|---|---|---|
| $\tilde\Pi_+$ | $\tilde\Pi_+$ | $\vec\Upsilon_-$ | $0$ | $0$ |
| $\vec\Upsilon_-$ | $0$ | $0$ | $\tilde\Pi_+$ | $\vec\Upsilon_-$ |
| $\vec\Upsilon_+$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ | $0$ | $0$ |
| $\tilde\Pi_-$ | $0$ | $0$ | $\vec\Upsilon_+$ | $\tilde\Pi_-$ |

**The left action.** For $\tilde Q_2\in\mathbb{B}$ write $L_{\tilde Q_2}(X)=\tilde Q_2X$. Reading the table row by row,
$$
L_{\tilde\Pi_+}(\tilde\Pi_+)=\tilde\Pi_+,\quad
L_{\tilde\Pi_+}(\vec\Upsilon_-)=\vec\Upsilon_-,\quad
L_{\tilde\Pi_+}(\vec\Upsilon_+)=0,\quad
L_{\tilde\Pi_+}(\tilde\Pi_-)=0,
$$
$$
L_{\vec\Upsilon_-}(\tilde\Pi_+)=0,\quad
L_{\vec\Upsilon_-}(\vec\Upsilon_-)=0,\quad
L_{\vec\Upsilon_-}(\vec\Upsilon_+)=\tilde\Pi_+,\quad
L_{\vec\Upsilon_-}(\tilde\Pi_-)=\vec\Upsilon_-,
$$
$$
L_{\vec\Upsilon_+}(\tilde\Pi_+)=\vec\Upsilon_+,\quad
L_{\vec\Upsilon_+}(\vec\Upsilon_-)=\tilde\Pi_-,\quad
L_{\vec\Upsilon_+}(\vec\Upsilon_+)=0,\quad
L_{\vec\Upsilon_+}(\tilde\Pi_-)=0,
$$
$$
L_{\tilde\Pi_-}(\tilde\Pi_+)=0,\quad
L_{\tilde\Pi_-}(\vec\Upsilon_-)=0,\quad
L_{\tilde\Pi_-}(\vec\Upsilon_+)=\vec\Upsilon_+,\quad
L_{\tilde\Pi_-}(\tilde\Pi_-)=\tilde\Pi_-.
$$
The four lists are the Peirce identities read as left multiplication: $\tilde\Pi_+$ keeps the two vectors of $S_+$ and kills $S_-$, $\tilde\Pi_-$ does the reverse, and the two nilpotents exchange the two spinor spaces in the two directions. In particular
$$
L_{\tilde\Pi_+}+L_{\tilde\Pi_-}=\mathrm{id},
\qquad
L_{\vec\Upsilon_+}L_{\vec\Upsilon_-}=L_{\tilde\Pi_-},
\qquad
L_{\vec\Upsilon_-}L_{\vec\Upsilon_+}=L_{\tilde\Pi_+},
\qquad
L_{\vec\Upsilon_\pm}^2=0,
$$
which are $\tilde\Pi_++\tilde\Pi_-=e_t$, $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$, $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$ and $\vec\Upsilon_\pm^2=0$.

For $\tilde Q$ itself the left action is diagonal,
$$
L_{\tilde Q}(\tilde\Pi_+)=\lambda_+\tilde\Pi_+,\quad
L_{\tilde Q}(\vec\Upsilon_-)=\lambda_+\vec\Upsilon_-,\quad
L_{\tilde Q}(\vec\Upsilon_+)=\lambda_-\vec\Upsilon_+,\quad
L_{\tilde Q}(\tilde\Pi_-)=\lambda_-\tilde\Pi_-,
$$
with the values $\lambda_+,\lambda_+,\lambda_-,\lambda_-$ on the four basis vectors in the order $\mathcal{B}$. This is the eigenbasis property of the sector: each basis vector is an eigenvector of $L_{\tilde Q}$.

**The right action.** For $R_{\tilde Q_2}(X)=X\tilde Q_2$ the same table read column by column gives
$$
R_{\tilde\Pi_+}(\tilde\Pi_+)=\tilde\Pi_+,\quad
R_{\tilde\Pi_+}(\vec\Upsilon_-)=0,\quad
R_{\tilde\Pi_+}(\vec\Upsilon_+)=\vec\Upsilon_+,\quad
R_{\tilde\Pi_+}(\tilde\Pi_-)=0,
$$
$$
R_{\vec\Upsilon_-}(\tilde\Pi_+)=\vec\Upsilon_-,\quad
R_{\vec\Upsilon_-}(\vec\Upsilon_-)=0,\quad
R_{\vec\Upsilon_-}(\vec\Upsilon_+)=\tilde\Pi_-,\quad
R_{\vec\Upsilon_-}(\tilde\Pi_-)=0,
$$
$$
R_{\vec\Upsilon_+}(\tilde\Pi_+)=0,\quad
R_{\vec\Upsilon_+}(\vec\Upsilon_-)=\tilde\Pi_+,\quad
R_{\vec\Upsilon_+}(\vec\Upsilon_+)=0,\quad
R_{\vec\Upsilon_+}(\tilde\Pi_-)=\vec\Upsilon_+,
$$
$$
R_{\tilde\Pi_-}(\tilde\Pi_+)=0,\quad
R_{\tilde\Pi_-}(\vec\Upsilon_-)=\vec\Upsilon_-,\quad
R_{\tilde\Pi_-}(\vec\Upsilon_+)=0,\quad
R_{\tilde\Pi_-}(\tilde\Pi_-)=\tilde\Pi_-,
$$
and for $\tilde Q$
$$
R_{\tilde Q}(\tilde\Pi_+)=\lambda_+\tilde\Pi_+,\quad
R_{\tilde Q}(\vec\Upsilon_-)=\lambda_-\vec\Upsilon_-,\quad
R_{\tilde Q}(\vec\Upsilon_+)=\lambda_+\vec\Upsilon_+,\quad
R_{\tilde Q}(\tilde\Pi_-)=\lambda_-\tilde\Pi_-,
$$
with the values $\lambda_+,\lambda_-,\lambda_+,\lambda_-$. The left and right actions do not coincide: $R_{\tilde Q}$ and $L_{\tilde Q}$ agree on an element exactly when the element is central, that is, on $\mathbb{C}e_t$.

**A general element.** For $\tilde Q_2=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-$ the left action on the basis is
$$
L_{\tilde Q_2}(\tilde\Pi_+)=Q_{2,11}\tilde\Pi_++Q_{2,21}\vec\Upsilon_+,\qquad
L_{\tilde Q_2}(\vec\Upsilon_-)=Q_{2,11}\vec\Upsilon_-+Q_{2,21}\tilde\Pi_-,
$$
$$
L_{\tilde Q_2}(\vec\Upsilon_+)=Q_{2,12}\tilde\Pi_++Q_{2,22}\vec\Upsilon_+,\qquad
L_{\tilde Q_2}(\tilde\Pi_-)=Q_{2,12}\vec\Upsilon_-+Q_{2,22}\tilde\Pi_-,
$$
and the right action is
$$
R_{\tilde Q_2}(\tilde\Pi_+)=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-,\qquad
R_{\tilde Q_2}(\vec\Upsilon_-)=Q_{2,21}\tilde\Pi_++Q_{2,22}\vec\Upsilon_-,
$$
$$
R_{\tilde Q_2}(\vec\Upsilon_+)=Q_{2,11}\vec\Upsilon_++Q_{2,12}\tilde\Pi_-,\qquad
R_{\tilde Q_2}(\tilde\Pi_-)=Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-.
$$
The two actions are diagonal exactly on the diagonal subalgebra $\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\tilde\Pi_-$, of which $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ is the member with the prescribed eigenvalues. This is the precise sense in which the Peirce coordinates of $\tilde Q_2=\tilde Q$ are the eigenvalues: $Q_{2,12}=Q_{2,21}=0$ is the condition that both actions be diagonal, and $\tilde Q$ is the member with $Q_{2,11}=\lambda_+$ and $Q_{2,22}=\lambda_-$.

**The four elements of the fixed basis.** The coordinates of $e_t,\vec e_x,\vec e_y,\vec e_z$ in $\mathcal{B}$ are read from the expansions. In the standard case, $Q_x=Q_y=0$ with the standard root $i\vec e_z$, that is $B=-Q_z$ and $\lambda_\pm=Q_t\mp iQ_z$, the nilpotents are
$$
\vec\Upsilon_-=\frac{i\vec e_x-\vec e_y}{2},\qquad
\vec\Upsilon_+=\frac{i\vec e_x+\vec e_y}{2},
$$
and
$$
e_t=\tilde\Pi_++\tilde\Pi_-,\qquad
\vec e_x=-i(\vec\Upsilon_-+\vec\Upsilon_+),\qquad
\vec e_y=\vec\Upsilon_+-\vec\Upsilon_-,\qquad
\vec e_z=-i\tilde\Pi_++i\tilde\Pi_-.
$$
Their coordinates are
$$
e_t=(1,0,0,1),\qquad
\vec e_x=(0,-i,-i,0),\qquad
\vec e_y=(0,-1,1,0),\qquad
\vec e_z=(-i,0,0,i),
$$
and the left action of the four on the basis is read from the table. In particular $\vec e_x,\vec e_y,\vec e_z$ satisfy $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, as the fixed basis does, so the same identities hold for their left actions.

**A general pure element.** Off the axis the coordinates of $\vec e_x,\vec e_y,\vec e_z$ depend on $\vec Q$. For any pure $\vec X$,
$$
\vec X=i\,\frac{\vec X\cdot\vec Q}{B}\,(\tilde\Pi_+-\tilde\Pi_-)+X_{12}\vec\Upsilon_-+X_{21}\vec\Upsilon_+,
\qquad
X_{12}\tilde\Pi_-=\vec\Upsilon_+\vec X\tilde\Pi_-,
\qquad
X_{21}\tilde\Pi_+=\vec\Upsilon_-\vec X\tilde\Pi_+,
$$
so its coordinates in $\mathcal{B}$ are
$$
\vec X=\Bigl(i\,\frac{\vec X\cdot\vec Q}{B},\;X_{12},\;X_{21},\;-i\,\frac{\vec X\cdot\vec Q}{B}\Bigr).
$$
The standard case is $\vec Q=Q_z\vec e_z$, $B=-Q_z$.

### The Eigenbasis of Left Multiplication

**A basis of $\mathbb{B}$ is an eigenbasis of $L_{\tilde Q}$ if each of its vectors $b$ satisfies $\tilde Qb=\mu b$ for some scalar $\mu$. The basis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ is one. It is the normalised Peirce representative: the two idempotents are the spectral idempotents and the two nilpotents are the corner generators whose scale is fixed by the normalisation. As an arbitrary eigenbasis it is not unique, because each eigenspace is two-dimensional; as this representative it is unique with the normalisation fixed.**

Write
$$
L_{\tilde Q}(\tilde Q_2)=\tilde Q\tilde Q_2,\qquad R_{\tilde Q}(\tilde Q_2)=\tilde Q_2\tilde Q.
$$
An eigenvector of $L_{\tilde Q}$ with eigenvalue $\mu$ is a nonzero element $\tilde Q_2$ with $\tilde Q\tilde Q_2=\mu\tilde Q_2$. The diagonal property of the eigenbasis reads
$$
\tilde Q\tilde\Pi_+=\lambda_+\tilde\Pi_+,\qquad
\tilde Q\vec\Upsilon_-=\lambda_+\vec\Upsilon_-,\qquad
\tilde Q\vec\Upsilon_+=\lambda_-\vec\Upsilon_+,\qquad
\tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_-,
$$
so the basis is an eigenbasis; the left action in it is diagonal with the values $\lambda_+,\lambda_+,\lambda_-,\lambda_-$.

**The two eigenspaces.** The eigenspaces are two-dimensional:
$$
\ker(L_{\tilde Q}-\lambda_+)=\tilde\Pi_+\mathbb{B}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_-,
\qquad
\ker(L_{\tilde Q}-\lambda_-)=\tilde\Pi_-\mathbb{B}=\mathbb{C}\vec\Upsilon_+\oplus\mathbb{C}\tilde\Pi_-.
$$
These are the two minimal **right** ideals. The basis $(\tilde\Pi_+,\vec\Upsilon_-)$ is a basis of the first, $(\vec\Upsilon_+,\tilde\Pi_-)$ a basis of the second.

**Uniqueness.** An arbitrary eigenbasis of $L_{\tilde Q}$ is any pair of bases of these two eigenspaces, so it is not unique. The Peirce basis is the representative singled out by the spectral data: it orders each eigenspace as $(\tilde\Pi_+,\vec\Upsilon_-)$ and $(\vec\Upsilon_+,\tilde\Pi_-)$, the diagonal idempotent first, and the pair $(\vec\Upsilon_+,\vec\Upsilon_-)$ is determined up to the reciprocal rescaling before the normalisation, and the normalisation fixes the scale. This is the precise sense in which $\mathcal{B}(\tilde Q)$ is the eigenbasis of $\tilde Q$: it is the unique normalised Peirce basis, not the unique basis of eigenvectors.

**The left ideals are eigenspaces of right multiplication.** The two minimal left ideals
$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,
\qquad
S_-=\mathbb{B}\tilde\Pi_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-
$$
are not eigenspaces of $L_{\tilde Q}$: each contains one eigenvector for $\lambda_+$ and one for $\lambda_-$. They are the eigenspaces of $R_{\tilde Q}$,
$$
\ker(R_{\tilde Q}-\lambda_+)=S_+,\qquad
\ker(R_{\tilde Q}-\lambda_-)=S_-,
$$
and the right action in the same basis is diagonal with the values $\lambda_+,\lambda_-,\lambda_+,\lambda_-$.
The reason is the side of the multiplication: $L_{\tilde Q}$ multiplies on the left and preserves each right ideal, $R_{\tilde Q}$ multiplies on the right and preserves each left ideal.

The two readings are compared in the table.

| Operator | Eigenvalue | Eigenspace | Dimension over $\mathbb{C}$ | Basis |
|---|---|---|---|---|
| $L_{\tilde Q}$ | $\lambda_+$ | $\tilde\Pi_+\mathbb{B}$ | $2$ | $(\tilde\Pi_+,\vec\Upsilon_-)$ |
| $L_{\tilde Q}$ | $\lambda_-$ | $\tilde\Pi_-\mathbb{B}$ | $2$ | $(\vec\Upsilon_+,\tilde\Pi_-)$ |
| $R_{\tilde Q}$ | $\lambda_+$ | $\mathbb{B}\tilde\Pi_+=S_+$ | $2$ | $(\tilde\Pi_+,\vec\Upsilon_+)$ |
| $R_{\tilde Q}$ | $\lambda_-$ | $\mathbb{B}\tilde\Pi_-=S_-$ | $2$ | $(\vec\Upsilon_-,\tilde\Pi_-)$ |

**Restriction to one left ideal.** On $S_+$ the operator $L_{\tilde Q}$ has the two distinct eigenvalues $\lambda_+,\lambda_-$, with eigenbasis $(\tilde\Pi_+,\vec\Upsilon_+)$; on $S_-$ it has the same two eigenvalues, with eigenbasis $(\vec\Upsilon_-,\tilde\Pi_-)$. On each, the eigenvalues are distinct, so the eigenbasis is unique up to two independent scales.

**The eigenprojection and the projector.** The element $\tilde\Pi_+$ is the eigenprojection of the eigenvalue decomposition. The operator $L_{\tilde\Pi_+}$ is the spectral projector onto the $\lambda_+$-eigenspace of $L_{\tilde Q}$: it sends $\tilde Q_2$ to $\tilde\Pi_+\tilde Q_2$, the first Peirce component, and its image is the two-dimensional right ideal $\tilde\Pi_+\mathbb{B}$. The two objects must not be confused: $L_{\tilde\Pi_+}$ is an operator on the four-dimensional algebra, while the spectral projector of the multiplication map is defined on the algebra itself.

## Spinors and the Peirce Index

**A spinor space of $\mathbb{B}$ is a minimal nonzero left ideal. The two spinor spaces are $S_+=\mathbb{B}\tilde\Pi_+$ and $S_-=\mathbb{B}\tilde\Pi_-$, each a complex plane, and the algebra is their direct sum.** This is the specialisation of §*Spinors and the Peirce Index* of *The Eigenbasis of a Spectrally Regular Biquaternion*.

### The Two Spinor Spaces

The two spaces are
$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,
\qquad
S_-=\mathbb{B}\tilde\Pi_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-,
$$
each of complex dimension two, and
$$
\mathbb{B}=S_+\oplus S_-.
$$
A **spinor of the first Peirce copy** is an element of $S_+$; a **spinor of the second Peirce copy** is an element of $S_-$.

**The module structure.** Left multiplication makes $S_+$ and $S_-$ left $\mathbb{B}$-modules, and each is a complex plane: a spinor has two complex coordinates. The two are isomorphic as left modules: right multiplication by $\vec\Upsilon_-$ maps $S_+$ onto $S_-$, with inverse right multiplication by $\vec\Upsilon_+$, because
$$
\tilde\Pi_+\vec\Upsilon_-=\vec\Upsilon_-,\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,
\qquad
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,
\qquad
\tilde\Pi_-\vec\Upsilon_+=\vec\Upsilon_+.
$$
They are nevertheless distinct subspaces of $\mathbb{B}$, and the direct sum is the whole algebra.

### The Left Action and the Definition of the Peirce Index

In the eigenbasis $(\tilde\Pi_+,\vec\Upsilon_+)$ of $S_+$, a spinor of the first Peirce copy is
$$
\xi_+=Q_{2,11}\tilde\Pi_++Q_{2,21}\vec\Upsilon_+,\qquad Q_{2,11},Q_{2,21}\in\mathbb{C},
$$
with the coordinate pair $(Q_{2,11},Q_{2,21})$, the first column of the matrix model of §*Matrices and the Column Correspondence*. Under left multiplication by $\tilde Q$,
$$
\tilde Q\xi_+=\lambda_+Q_{2,11}\tilde\Pi_++\lambda_-Q_{2,21}\vec\Upsilon_+,
$$
so the coordinate pair is sent to
$$
(Q_{2,11},Q_{2,21})\longmapsto(\lambda_+Q_{2,11},\;\lambda_-Q_{2,21}).
$$
A spinor of the second Peirce copy is an element of $S_-$,
$$
\xi_-=Q_{2,12}\vec\Upsilon_-+Q_{2,22}\tilde\Pi_-,\qquad Q_{2,12},Q_{2,22}\in\mathbb{C}.
$$
The order of the coefficients follows the eigenbasis $(\vec\Upsilon_-,\tilde\Pi_-)$ of $S_-$, in which the eigenvalues are $(\lambda_+,\lambda_-)$, so the coordinate pair is $(Q_{2,12},Q_{2,22})$, the second column of the matrix model of §*Matrices and the Column Correspondence*, and
$$
\tilde Q\xi_-=\lambda_+Q_{2,12}\vec\Upsilon_-+\lambda_-Q_{2,22}\tilde\Pi_-
\longmapsto
(\lambda_+Q_{2,12},\;\lambda_-Q_{2,22}).
$$
**Left versus right multiplication.** The diagonal action displayed above is the action of $L_{\tilde Q}$ on each spinor space, and it carries both eigenvalues. The space $S_+$ is not an eigenspace of $L_{\tilde Q}$; it is the $\lambda_+$-eigenspace of the right multiplication $R_{\tilde Q}$, and $S_-$ is the $\lambda_-$-eigenspace. The distinction is the side on which $\tilde Q$ multiplies: $R_{\tilde Q}$ is scalar on each $S_\pm$, while $L_{\tilde Q}$ carries the two eigenvalues on each. This is the content of §*The Eigenbasis of Left Multiplication*.

The basis $(\vec\Upsilon_-,\tilde\Pi_-)$ is part of the definition: writing the two vectors in the other order would exchange the two diagonal values.

The two spinor spaces and their coordinates are collected in the table.

| Spinor space | Eigenbasis | Spinor | Coordinates |
|---|---|---|---|
| $S_+=\mathbb{B}\tilde\Pi_+$ | $(\tilde\Pi_+,\vec\Upsilon_+)$ | $Q_{2,11}\tilde\Pi_++Q_{2,21}\vec\Upsilon_+$ | $(Q_{2,11},Q_{2,21})$, column $1$ |
| $S_-=\mathbb{B}\tilde\Pi_-$ | $(\vec\Upsilon_-,\tilde\Pi_-)$ | $Q_{2,12}\vec\Upsilon_-+Q_{2,22}\tilde\Pi_-$ | $(Q_{2,12},Q_{2,22})$, column $2$ |

**A general element is a pair of spinors.** Every $\tilde Q_2\in\mathbb{B}$ splits as
$$
\tilde Q_2=\tilde Q_2\tilde\Pi_++\tilde Q_2\tilde\Pi_-,
$$
and the two summands are a spinor of the first Peirce copy and a spinor of the second Peirce copy. In the eigenbasis coordinates they are
$$
\tilde Q_2\longmapsto(Q_{2,11},Q_{2,12},Q_{2,21},Q_{2,22}),
\qquad
\tilde Q_2\tilde\Pi_+\longmapsto(Q_{2,11},Q_{2,21}),
\qquad
\tilde Q_2\tilde\Pi_-\longmapsto(Q_{2,12},Q_{2,22}).
$$
A general element is therefore not a spinor: it has one spinor component of each Peirce copy.

**Complex dimensions.** Each spinor has two complex components, hence four real parameters. The two spinor spaces have complex dimension two and real dimension four each, and their direct sum has the complex dimension four and the real dimension eight of $\mathbb{B}$. The label "first" versus "second" is fixed by the convention $\tilde\Pi_+=(e_t+\vec\Xi)/2$; replacing the square root by its negative, or exchanging the two labels, exchanges the two Peirce copies.

### Matrices and the Column Correspondence

Fix the assignment
$$
\tilde\Pi_+\mapsto E_{11},\qquad
\vec\Upsilon_-\mapsto E_{12},\qquad
\vec\Upsilon_+\mapsto E_{21},\qquad
\tilde\Pi_-\mapsto E_{22},
$$
where $E_{ij}$ is the matrix unit with $1$ in row $i$ and column $j$. Then every $\tilde Q_2\in\mathbb{B}$ has the unique expansion
$$
\tilde Q_2=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-,
\qquad Q_{2,ij}\in\mathbb{C},
$$
and is represented by
$$
\mathsf M_2^{Q}(\tilde Q_2)=\begin{pmatrix}Q_{2,11}&Q_{2,12}\\Q_{2,21}&Q_{2,22}\end{pmatrix}.
$$
The element $\tilde Q_2=\tilde Q$ has $Q_{2,11}=\lambda_+$, $Q_{2,22}=\lambda_-$ and $Q_{2,12}=Q_{2,21}=0$, so
$$
\mathsf M_2^{Q}(\tilde Q)=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}.
$$

The two columns are the two spinor spaces:
$$
S_+=\mathbb{B}\tilde\Pi_+\longleftrightarrow\operatorname{span}\{E_{11},E_{21}\}=\text{column }1,
\qquad
S_-=\mathbb{B}\tilde\Pi_-\longleftrightarrow\operatorname{span}\{E_{12},E_{22}\}=\text{column }2.
$$
The first column of $\mathsf M_2^{Q}(\tilde Q_2)$ is the coordinate vector of $\tilde Q_2\tilde\Pi_+$, the second is the coordinate vector of $\tilde Q_2\tilde\Pi_-$.

A spinor of the first Peirce copy
$$
\xi_+=\alpha\tilde\Pi_++\beta\vec\Upsilon_+
\longleftrightarrow
\begin{pmatrix}\alpha\\\beta\end{pmatrix}
$$
is represented by the matrix
$$
\begin{pmatrix}\alpha&0\\\beta&0\end{pmatrix},
$$
whose first column is $\xi_+$ and whose second column is zero. A spinor of the second Peirce copy
$$
\xi_-=\gamma\vec\Upsilon_-+\delta\tilde\Pi_-
\longleftrightarrow
\begin{pmatrix}\gamma\\\delta\end{pmatrix}
$$
is represented by the matrix
$$
\begin{pmatrix}0&\gamma\\0&\delta\end{pmatrix},
$$
whose first column is zero and whose second column is $\xi_-$. The order $(\vec\Upsilon_-,\tilde\Pi_-)$ is the eigenbasis of $S_-$ used above; it is the order in which the diagonal values are $(\lambda_+,\lambda_-)$.

Multiplication by $\tilde Q$ acts on the first column by $\mathsf M_2^{Q}(\tilde Q)$,
$$
\tilde Q\xi_+\longleftrightarrow
\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}
\begin{pmatrix}\alpha\\\beta\end{pmatrix}
=
\begin{pmatrix}\lambda_+\alpha\\\lambda_-\beta\end{pmatrix},
$$
and on the second column by the same matrix,
$$
\tilde Q\xi_-\longleftrightarrow
\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}
\begin{pmatrix}\gamma\\\delta\end{pmatrix}
=
\begin{pmatrix}\lambda_+\gamma\\\lambda_-\delta\end{pmatrix}.
$$
This is the precise statement that the two spinor spaces are the two columns and that multiplication by $\tilde Q$ acts on both by the same diagonal matrix. A general element of $\mathbb{B}$ is not a spinor: its matrix has two nonzero columns, one in each spinor space.

## What Depends on $\tilde Q$ and What Does Not

The eigenbasis data depend on $\tilde Q$ through its root. The comparison is collected in the table.

| Object | Depends on $\tilde Q$? |
|---|---|
| Root $\vec\Xi$ and idempotents $\tilde\Pi_\pm$ | yes |
| Corner lines $\mathbb{B}_{+-},\mathbb{B}_{-+}$ as subspaces | yes |
| Left ideals $S_+=\mathbb{B}\tilde\Pi_+$ and $S_-=\mathbb{B}\tilde\Pi_-$ | yes |
| Pair $(\vec\Upsilon_+,\vec\Upsilon_-)$ | yes, through the root; the residual scale is removed by the normalisation |
| Diagonal values $(\lambda_+,\lambda_-)$ of $L_{\tilde Q}$ | yes |
| Peirce coordinates of a general element $\tilde Q_2$ | yes |

The eigenbasis is not the standard Peirce basis attached to the fixed root $i\vec e_z$. The two coincide, up to the reciprocal rescaling, exactly when $\vec Q$ is parallel to $\vec e_z$, that is, when $Q_x=Q_y=0$. In that case $\vec\Xi=\pm i\vec e_z$, the pair is the standard pair up to the exchange of its two members, and the nilpotents are $\vec\Upsilon_x,\vec\Upsilon_y$, in one order or the other, up to the reciprocal rescaling.

## The Eigenbasis Data

Given $\tilde Q$ with $B^2\neq0$, the following data are attached to $\tilde Q$:
$$
\vec\Xi=-\frac{i\vec Q}{B},\qquad
\tilde\Pi_\pm=\frac{e_t\pm\vec\Xi}{2},\qquad
\lambda_\pm=Q_t\pm \beta,
$$
$$
\vec\Upsilon_+\in\mathbb{B}_{-+},\qquad
\vec\Upsilon_-\in\mathbb{B}_{+-},\qquad
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_\pm^2=0,
$$
with the symmetric closed form
$$
\vec\Upsilon_\pm=\frac{B\,\vec w-\dfrac{\Sigma}{B}\,\vec Q\pm\dfrac{i}{2}\,[\vec Q,\vec w]}{2\sqrt{\Sigma^2-3B^2}},
\qquad
\vec w=\vec e_x+\vec e_y+\vec e_z,\quad \Sigma=Q_x+Q_y+Q_z,
$$
valid off the cone $\Sigma^2=3B^2$; on that cone the axis charts
$$
\vec\Upsilon_\pm=\frac{B\,\vec e_\mu-\dfrac{Q_\mu}{B}\,\vec Q\pm\dfrac{i}{2}\,[\vec Q,\vec e_\mu]}{2\sqrt{Q_\mu^2-B^2}},
\qquad \mu=x,y,z,
$$
cover the pair, at least one of the three being defined, and the defined readings differ by the reciprocal rescaling.
$$
\mathbb{B}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\vec\Upsilon_+\oplus\mathbb{C}\tilde\Pi_-,
$$
$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,\qquad
S_-=\mathbb{B}\tilde\Pi_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-,
$$
and every $\tilde Q_2\in\mathbb{B}$ has the unique expansion
$$
\tilde Q_2=Q_{2,11}\tilde\Pi_++Q_{2,12}\vec\Upsilon_-+Q_{2,21}\vec\Upsilon_++Q_{2,22}\tilde\Pi_-,
\qquad Q_{2,ij}\in\mathbb{C},
$$
with $\tilde Q_2=\tilde Q$ having $Q_{2,11}=\lambda_+$, $Q_{2,22}=\lambda_-$ and $Q_{2,12}=Q_{2,21}=0$.

**Diagonal property.**
$$
\tilde Q\tilde\Pi_+=\lambda_+\tilde\Pi_+,\qquad
\tilde Q\vec\Upsilon_-=\lambda_+\vec\Upsilon_-,\qquad
\tilde Q\vec\Upsilon_+=\lambda_-\vec\Upsilon_+,\qquad
\tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_-.
$$
The eigenbasis of $L_{\tilde Q}$ has eigenvalues
$$
(\lambda_+,\lambda_+,\lambda_-,\lambda_-).
$$
The $\lambda_+$-eigenspace of $L_{\tilde Q}$ is the right ideal $\tilde\Pi_+\mathbb{B}$, with basis $(\tilde\Pi_+,\vec\Upsilon_-)$; the $\lambda_-$-eigenspace is $\tilde\Pi_-\mathbb{B}$, with basis $(\vec\Upsilon_+,\tilde\Pi_-)$. The two left ideals $S_+,S_-$ are the eigenspaces of $R_{\tilde Q}$, with eigenvalues $\lambda_+,\lambda_-$ respectively. On each left ideal the restriction of $L_{\tilde Q}$ has the distinct eigenvalues $(\lambda_+,\lambda_-)$, so the eigenbasis of that restriction is unique up to two independent scales.

**Spinors.**
A spinor of the first Peirce copy is an element of $S_+$,
$$
\xi_+=Q_{2,11}\tilde\Pi_++Q_{2,21}\vec\Upsilon_+,
\qquad (Q_{2,11},Q_{2,21})\in\mathbb{C}^2,
$$
and under left multiplication
$$
\tilde Q\xi_+=\lambda_+Q_{2,11}\tilde\Pi_++\lambda_-Q_{2,21}\vec\Upsilon_+,
\qquad\text{that is,}\qquad
(Q_{2,11},Q_{2,21})\longmapsto(\lambda_+Q_{2,11},\;\lambda_-Q_{2,21}).
$$
A spinor of the second Peirce copy is an element of $S_-$,
$$
\xi_-=Q_{2,12}\vec\Upsilon_-+Q_{2,22}\tilde\Pi_-,
\qquad (Q_{2,12},Q_{2,22})\in\mathbb{C}^2,
$$
and under left multiplication
$$
\tilde Q\xi_-=\lambda_+Q_{2,12}\vec\Upsilon_-+\lambda_-Q_{2,22}\tilde\Pi_-,
\qquad\text{that is,}\qquad
(Q_{2,12},Q_{2,22})\longmapsto(\lambda_+Q_{2,12},\;\lambda_-Q_{2,22}).
$$
The two spinor spaces are the two Peirce carriers, which here are the two minimal left ideals; under left multiplication each is a complex plane carrying the two eigenvalues $\lambda_+,\lambda_-$.

**Matrices.**
With
$$
\tilde\Pi_+\mapsto E_{11},\qquad
\vec\Upsilon_-\mapsto E_{12},\qquad
\vec\Upsilon_+\mapsto E_{21},\qquad
\tilde\Pi_-\mapsto E_{22},
$$
a general element has the matrix
$$
\mathsf M_2^{Q}(\tilde Q_2)=\begin{pmatrix}Q_{2,11}&Q_{2,12}\\Q_{2,21}&Q_{2,22}\end{pmatrix},
\qquad
\mathsf M_2^{Q}(\tilde Q)=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}.
$$
The first column is $S_+$, the second is $S_-$, and multiplication by $\tilde Q$ acts on both by $\operatorname{diag}(\lambda_+,\lambda_-)$.

## Multiplication and Inversion

**Products stay in the unit group.** The norm is multiplicative, so for $\tilde P,\tilde Q\in\Sigma_{11}$,

$$
\langle\tilde P\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural}\neq0,
$$

and the product lies in $\mathbb{B}^\times=\Sigma_{10}\sqcup\Sigma_{11}$. Both outcomes occur.

**Theorem (both outcomes).**

$$
\Sigma_{11}\cdot\Sigma_{11}\subseteq\Sigma_{10}\cup\Sigma_{11},
$$

and the product of two elements of the sector can lie in $\Sigma_{11}$ and can lie in $\Sigma_{10}$.

*Witnesses.* For the first, $\tilde Q=e_t+\vec e_x$ has $\langle\tilde Q\rangle_{\natural}=2$ and $B^2=1$, and

$$
\tilde Q^2=e_t+2\vec e_x+\vec e_x^2=2\vec e_x,
$$

with $\langle\tilde Q\rangle_{\natural}=4$ and $B^2=4$: it stays in the sector. For the second, $\tilde P=e_t+2\vec e_x$ and $\tilde Q=e_t-2\vec e_x$ both have $\langle\tilde Q\rangle_{\natural}=5$ and $B^2=4$, and

$$
\tilde P\tilde Q=e_t-4\vec e_x^2=5e_t,
$$

with $B^2=0$ and $\langle\tilde Q\rangle_{\natural}=25$: the product lies on the scalar line, in $\Sigma_{10}^{\mathrm{s}}$.

**Squares.** The square of an element of the sector has eigenvalues $\lambda_+^2,\lambda_-^2$ and

$$
B^2(\tilde Q^2)=4Q_t^2B^2(\tilde Q).
$$

Hence

$$
\tilde Q^2\in\Sigma_{11}\ \text{if }Q_t\neq0,\qquad
\tilde Q^2=-B^2(\tilde Q)\,e_t\in\Sigma_{10}^{\mathrm{s}}\ \text{if }Q_t=0.
$$

The second case is exactly $\lambda_-=-\lambda_+$; the pure vector $\vec e_x+\vec e_y$ is the standard witness,

$$
(\vec e_x+\vec e_y)^2=-2e_t.
$$

So squaring can leave the sector, and it leaves it precisely through the vertex of the spectral cone.

**Inversion and closure.** The sector is inverse-closed, because $\langle\tilde Q^{-1}\rangle_{\natural}\neq0$ and $B^2(\tilde Q^{-1})\neq0$; it is not product-closed, by the theorem. It is therefore a **symmetric subset** of the unit group, not a subgroup. In fact it contains no subgroup at all, since every subgroup contains the identity and $e_t\notin\Sigma_{11}$.

**Caveat on the parametrisation.** Although $\lambda_+e_++\lambda_-e_-$ is unique, products do not add eigenvalues: the eigenvalues of $\tilde P\tilde Q$ are not determined by those of $\tilde P$ and $\tilde Q$ separately. Only their product is, through the norm.

## Relation to the Two Cones

**The sector is the complement of both cones.** As point sets,

$$
\Sigma_{11}=\mathbb{B}\setminus(\mathcal N\cup\mathcal S),\qquad
\mathbb{B}=\Sigma_{11}\sqcup\Sigma_{10}\sqcup\Sigma_{01}\sqcup\Sigma_{00}.
$$

It is the only cell off both cones, and its closure is all of $\mathbb{B}$.

**The two cones are tangent exactly on the common stratum.** The defining functions satisfy the identity

$$
N-B^2=Q_t^2,
$$

so their gradients,

$$
\nabla N=2(Q_t,\vec Q),\qquad \nabla B^2=2(0,\vec Q),
$$

coincide whenever $Q_t=0$. At a common point of the two cones one has $Q_t=0$ and $B^2=0$, which is $\Sigma_{00}$; there the gradients are both $2(0,\vec Q)$, equal and non-zero off the origin. So the cones are tangent along $\Sigma_{00}\setminus\{0\}$ and both singular at the origin. On $\Sigma_{11}$ there is nothing to be tangent to: the sector is disjoint from both cones.

**The cell where the answers agree.** Every element of the sector is a unit with distinct eigenvalues: both questions — is it invertible, and are its eigenvalues separated — receive the positive answer. This is the fourth corner of the $2\times2$ table and the reason the independence of the two problems is not vacuous: the doubly regular case exists, and it exists on a dense open set.

**Independence, restated.** $\Sigma_{01}$ and $\Sigma_{10}$ show that neither cone contains the other. $\Sigma_{11}$ shows that the two conditions are simultaneously satisfiable, and $\Sigma_{00}$ shows that they are simultaneously violable. The four cells together are the complete truth table of the pair of predicates $(N\neq0,\ B^2\neq0)$.

## Comparison with the Other Three Sectors

| sector | conditions | elements | spectrum | Peirce decomposition | product |
|---|---|---|---|---|---|
| **doubly regular** $\Sigma_{11}$ | $\langle\tilde Q\rangle_{\natural}\neq0$, $B^2\neq0$ | $\lambda_+e_++\lambda_-e_-$ with $\lambda_\pm$ distinct and non-zero | $\{\lambda_+,\lambda_-\}$ | exists, unique; both terms non-zero | stays in $\mathbb{B}^\times$; lands in $\Sigma_{11}$ or $\Sigma_{10}$ |
| **norm-degenerate, spectrally regular** $\Sigma_{01}$ | $\langle\tilde Q\rangle_{\natural}=0$, $B^2\neq0$ | $c\tilde\Pi$, $\tilde\Pi$ a non-trivial idempotent | $\{c,0\}$ | exists, unique; one term vanishes | stays on $\mathcal N$; all three outcomes |
| **norm-regular, spectrally degenerate** $\Sigma_{10}$ | $\langle\tilde Q\rangle_{\natural}\neq0$, $B^2=0$ | $Q_tu$, $u$ unipotent | $\{Q_t\}$, repeated | fails on $\Sigma_{10}^{\mathrm{J}}$; one-term and non-unique on $\Sigma_{10}^{\mathrm{s}}$ | stays in $\mathbb{B}^\times$; lands in $\Sigma_{10}$ or $\Sigma_{11}$ |
| **doubly degenerate** $\Sigma_{00}$ | $\langle\tilde Q\rangle_{\natural}=0$, $B^2=0$ | non-zero nilpotents of index two, plus the origin | $\{0\}$ | fails off the origin | $0$ or $\Sigma_{01}$ |

The four cells are exhaustive and disjoint. $\Sigma_{11}$ is the unique cell in which both predicates hold, $\Sigma_{00}$ the unique cell in which both fail, and the two mixed cells are the remaining two rows of the truth table.

**Position among the four sectors.** Sector $11$ is the **distinct sector**: two distinct non-zero eigenvalues, a unique two-term spectral decomposition, and no point of either cone. The finer split inside the other sectors is by the minimal polynomial, not by the two predicates; it is recorded in *Relations between the N Norm and Spectral Regularity and Degeneracy*, §*The Chain of Invariants*. On this sector the two classifications coincide, because the sector is homogeneous: every element has two distinct non-zero eigenvalues and a unique Peirce decomposition relative to $\tilde Q$.

## Consequences

**Eigenbasis.** It exists. The genuine two-term spectral decomposition is

$$
\tilde Q=\lambda_+e_++\lambda_-e_-,\qquad
e_\pm=\frac{\tilde Q-\lambda_\mp e_t}{\lambda_\pm-\lambda_\mp}.
$$

It is unique. The Peirce eigenbasis $(e_+,\vec\Upsilon_-,\vec\Upsilon_+,e_-)$ is unique with the normalisation fixed. Both eigenvalues are non-zero and distinct, and both idempotents are non-trivial. This is the only sector in which all of these hold at once.

**The flow.** The element supplies the pure root $\vec U=\vec Q/B$ of $-1$, and $e^{\theta\tilde Q}=e^{\theta Q_t}W(-\theta,B/2\pi)$, with $W$ the Fourier kernel of *Biquaternion Continuous Harmonic Analysis*, §*The Fourier Kernel*. The Hermitian norm of the flow, $\langle\tilde X\rangle_*=\operatorname{Sc}(\tilde X\tilde X^*)$, is

$$
\langle e^{\theta\tilde Q}\rangle_*
=\lvert e^{\theta Q_t}\rvert^2
\left(\lvert\cos(B\theta)\rvert^2+\lvert\sin(B\theta)\rvert^2\,\lVert\vec U\rVert_E^2\right),
\qquad
\lVert\vec U\rVert_E^2\ge1,
$$

with equality exactly when $\vec U$ is real, that is, when the element is normal: $\tilde Q\tilde Q^*=\tilde Q^*\tilde Q$, with $\tilde X^*=\overline{\tilde X^\natural}$ (*The Biquaternion Eigenvalue Decomposition*, §*The Hermitian Case*). The eigenbasis is orthogonal for the Hermitian form exactly in that case. The flow is $*$-unitary for the Hermitian form exactly when $Q_t\in i\mathbb{R}$ and $\vec Q\in\mathbb{R}^3$, and self-adjoint for the Hermitian form exactly when $Q_t\in\mathbb{R}$ and $\vec Q\in i\mathbb{R}^3$; these are the material and Hermitian sub-sectors, and normality implies neither. The generic element of $\Sigma_{11}$ has complex eigenvalues and a growing norm.

**Polar decomposition.** It exists and is finite: the modulus $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}=\sqrt{\lambda_+\lambda_-}\neq0$, so the modulus–unit polar decomposition of *The Polar Decomposition of a N-Regular Biquaternion* applies. The sector is the only one in which the polar word and the spectral decomposition are simultaneously available: in $\Sigma_{01}$ the polar word fails while the spectral decomposition survives, and in $\Sigma_{10}$ the spectral decomposition fails while the polar word survives.

**One-sided operators.** $L_{\tilde Q}$ and $R_{\tilde Q}$ are bijections of complex rank $4$ with zero kernel, and both annihilators vanish. Together with the eigenbasis, this is the full non-degenerate package.

**The generic case.** Every statement proved for a generic element of $\mathbb{B}$ — invertible, semisimple, with distinct eigenvalues, unique eigenprojectors and a finite polar word — holds on $\Sigma_{11}$ and fails somewhere on its complement. The sector has full measure, and its complement is the arrangement of the two cones.

## The Generators, the Eigenvalues, and the Element

**The root and the two idempotents.**

$$
\boxed{\ \vec\Xi=-\frac{i}{B}\vec Q=-\frac{iQ_x}{B}\vec e_x-\frac{iQ_y}{B}\vec e_y-\frac{iQ_z}{B}\vec e_z,\qquad \vec\Xi^2=e_t\ }
$$

$$
\boxed{\ \tilde\Pi_+=\frac12\left(e_t-\frac{i}{B}\vec Q\right)=\frac12 e_t-\frac{iQ_x}{2B}\vec e_x-\frac{iQ_y}{2B}\vec e_y-\frac{iQ_z}{2B}\vec e_z\ }
$$

$$
\boxed{\ \tilde\Pi_-=\frac12\left(e_t+\frac{i}{B}\vec Q\right)=\frac12 e_t+\frac{iQ_x}{2B}\vec e_x+\frac{iQ_y}{2B}\vec e_y+\frac{iQ_z}{2B}\vec e_z\ }
$$

**The two nilpotents.** Put $\vec w=\vec e_x+\vec e_y+\vec e_z$ and $\Sigma=Q_x+Q_y+Q_z$. Away from the exceptional cone $\Sigma^2=3B^2$, they are

$$
\boxed{\ \vec\Upsilon_+=\frac{B\,\vec w-\dfrac{\Sigma}{B}\,\vec Q+\dfrac{i}{2}\,[\vec Q,\vec w]}{2\sqrt{\Sigma^2-3B^2}}\ }
$$

$$
\boxed{\ \vec\Upsilon_-=\frac{B\,\vec w-\dfrac{\Sigma}{B}\,\vec Q-\dfrac{i}{2}\,[\vec Q,\vec w]}{2\sqrt{\Sigma^2-3B^2}}\ }
$$

with the normalisation $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$ and $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$ for one fixed square root; on the exceptional cone the axis charts replace the symmetric formula.

**The two eigenvalues.**

$$
\boxed{\ \lambda_+=Q_t+iB\ }
$$

$$
\boxed{\ \lambda_-=Q_t-iB\ }
$$

with $\lambda_++\lambda_-=2Q_t$ and $\lambda_+\lambda_-=\langle\tilde Q\rangle_{\natural}$.

**The element.** In the eigenbasis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$,

$$
\boxed{\ \tilde Q=\lambda_+\tilde\Pi_++0\cdot\vec\Upsilon_-+0\cdot\vec\Upsilon_++\lambda_-\tilde\Pi_-\ }
$$

$$
\boxed{\ \tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-
=\frac{\lambda_++\lambda_-}{2}e_t+\frac{\lambda_+-\lambda_-}{2}\vec\Xi
=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z\ }
$$

with $\vec\Xi=-i\vec Q/B$. The eigenvalues weight the operator, not the element: in this basis $L_{\tilde Q}$ has the diagonal values $\lambda_+,\lambda_+,\lambda_-,\lambda_-$, and $R_{\tilde Q}$ the values $\lambda_+,\lambda_-,\lambda_+,\lambda_-$. The sum weighted by them, $\lambda_+\tilde\Pi_++\lambda_+\vec\Upsilon_-+\lambda_-\vec\Upsilon_++\lambda_-\tilde\Pi_-$, is not $\tilde Q$.

## Summary

| question | answer |
|---|---|
| definition | $\Sigma_{11}=\{N\neq0,\ B^2\neq0\}$ |
| descriptions | $\mathbb{B}\setminus(\mathcal N\cup\mathcal S)$; a unit with distinct eigenvalues; $\lambda_+e_++\lambda_-e_-$ with $\lambda_\pm$ distinct and non-zero; invertible with a non-trivial Peirce decomposition relative to $\tilde Q$ |
| geometry | open dense, of full measure; complex dimension $4$ and real dimension $8$; connected; complement the hypersurface $NB^2=0$ |
| elements | regular semisimple units; minimal polynomial $X^2-2Q_tX+N$, squarefree; centraliser $\mathbb{C}\oplus\mathbb{C}$ |
| Peirce decomposition | exists, unique, both coefficients non-zero |
| eigenbasis | normalised Peirce basis; unique with the normalisation fixed |
| annihilators | both zero; left and right multiplication bijective |
| inversion | closed: $\tilde Q^{-1}\in\Sigma_{11}$ |
| multiplication | $\Sigma_{11}\cdot\Sigma_{11}\subseteq\Sigma_{10}\cup\Sigma_{11}$, with both outcomes; not product-closed |
| squares | in $\Sigma_{11}$ when $Q_t\neq0$, on the scalar line when $Q_t=0$ |
| relation to the cones | off both cones; the cones are tangent along $\Sigma_{00}\setminus\{0\}$ |
| place in the arrangement | the distinct sector: the one cell where both answers are positive |

The sector is the generic sector. It is the set of units with distinct non-zero eigenvalues, the complement of the union of the two cones, and the only cell of the arrangement in which both questions — is the element invertible, and can its eigenvalues be told apart — receive the positive answer. It is what the algebra looks like when nothing degenerates. Its complement is the arrangement, and the three other sectors are the three ways the doubly regular case can fail: by losing invertibility, by losing spectral separation, or by losing both.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Sigma_{ij}$ | the sector with $i=1$ iff $\langle\tilde Q\rangle_{\natural}\neq0$, $j=1$ iff $B^2\neq0$ |
| $\Sigma_{11}$ | the norm-regular, spectrally regular sector, this article |
| $\mathcal N=\{N=0\}$ | the null cone of the quaternionic norm |
| $\mathcal S=\{B^2=0\}$ | the spectral-degenerate cone |
| $\mathbb{B}^\times=\{N\neq0\}$ | the unit group |
| $\lambda_\pm=Q_t\pm\beta$, $\beta=iB$ | the two eigenvalues |
| $e_\pm=\tilde\Pi_\pm$ | the spectral idempotents, unique; the same pair in both notations |
| $\Rho=\sqrt{N}$ | the modulus |
| $L_{\tilde Q}$, $R_{\tilde Q}$ | left and right multiplication, both bijective on the sector |

## Further Reading

- [The Eigenbasis of a Spectrally Regular Biquaternion](the-eigenbasis-of-a-spectrally-regular-biquaternion.html), for the construction in full generality, the normalisation, the expansion of an arbitrary biquaternion and the spinor reading.
- [The N-Degenerate, Spectrally Degenerate Sector](the-n-degenerate-spectrally-degenerate-sector.html), for $\Sigma_{00}$, the nilpotents and the origin.
- [The N-Degenerate, Spectrally Regular Sector](the-n-degenerate-spectrally-regular-sector.html), for $\Sigma_{01}$, the scaled idempotents.
- [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html), for $\Sigma_{10}$, the unipotents and the scalar line.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the null cone, its strata and the unit group.
- [The Spectrum](the-spectrum.html), for the discriminant, the spectral criterion and the spectral-degenerate cone.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html), for the four sectors and the comparison of the two cones.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the Peirce corners and the minimal ideals.
- [The Polar Decomposition of a N-Regular Biquaternion](the-polar-decomposition-of-an-n-regular-biquaternion.html), for the modulus $\Rho=\sqrt N$ and the unit factor.
- [Relations between the Biquaternion Exponential and the Fourier Kernel](relations-between-the-biquaternion-exponential-and-the-fourier-kernel.html), for the exponential as a Fourier kernel, the root supplied by the element and the Hermitian norm of the flow.
