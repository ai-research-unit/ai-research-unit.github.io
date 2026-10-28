# __Roots of Unity and the Lagrange Idempotents__

## Introduction

A single matrix carries the whole frame of $M_6(\mathbb{C})$: a root of unity $H$ with $H^6=I$ and six distinct eigenvalues. Its six eigenspaces are six lines, and the six Lagrange projectors onto them are idempotent, orthogonal and complete. The root is read as the sum $H=\sum_k\zeta_kP_k$ of its idempotents with the sixth roots of unity as coefficients; the coefficients grade the algebra by $\mathbb{Z}/6$; and the cube $H^3$ is the chirality involution. **No second object is primitive.** The idempotents are functions of $H$ alone, and the root is the only input.

The article fixes the root, the Lagrange formula, the grading and the root set, in that order. It assumes the algebra $M_6(\mathbb{C})$ — the basis $E_{ij}$, the product rule $E_{ij}E_{kl}=\delta_{jk}E_{il}$, the trace and the determinant — which is *The Matrix Algebra $M_6(\mathbb{C})$*. It uses no form, no norm and no topology. The Peirce decomposition that the six lines induce is *The Peirce Decomposition*; the frame and its gauge are *The Frame, the Simple Nilpotents and the Gauge*; the two chiralities are *The Two Chiralities*; the spectral theory of an element with repeated eigenvalues, where the Lagrange formula degenerates, is *Spectral Theory and the Spectral Projectors*.

The construction is root-first. The biquaternion articles build the frame from two anticommuting roots of $+1$; here one root of order six supplies all six idempotents, and the order-two case is a specialisation, not a second ingredient. That contrast is stated in §*The Order-Two Case*.

## The Sixth Roots of Unity

### The Roots

**Definition.** Let

$$
\zeta=e^{2\pi i/6}=\tfrac12+\tfrac{\sqrt3}{2}i ,
$$

a primitive sixth root of unity, and put $\zeta_k=\zeta^{k-1}$ for $k=1,\dots,6$. The six roots are

$$
\zeta_1=1,\qquad
\zeta_2=\zeta=\tfrac12+\tfrac{\sqrt3}{2}i,\qquad
\zeta_3=\zeta^2=-\tfrac12+\tfrac{\sqrt3}{2}i,\qquad
\zeta_4=-1,\qquad
\zeta_5=-\zeta,\qquad
\zeta_6=\bar\zeta .
$$

They are the elements of the cyclic group $\mu_6=\{z\in\mathbb{C}^\times:z^6=1\}\cong\mathbb{Z}/6$.

**Proposition.** The roots have the following orders and elementary symmetric functions.

| Root | $\zeta_1$ | $\zeta_2$ | $\zeta_3$ | $\zeta_4$ | $\zeta_5$ | $\zeta_6$ |
|---|---|---|---|---|---|---|
| Value | $1$ | $\tfrac12+\tfrac{\sqrt3}{2}i$ | $-\tfrac12+\tfrac{\sqrt3}{2}i$ | $-1$ | $-\tfrac12-\tfrac{\sqrt3}{2}i$ | $\tfrac12-\tfrac{\sqrt3}{2}i$ |
| Order | $1$ | $6$ | $3$ | $2$ | $3$ | $6$ |
| Conjugate | $\zeta_1$ | $\zeta_6$ | $\zeta_5$ | $\zeta_4$ | $\zeta_3$ | $\zeta_2$ |

The primitive roots are $\zeta_2$ and $\zeta_6$; the real roots are $\zeta_1=1$ and $\zeta_4=-1$; and

$$
\sum_{k=1}^{6}\zeta_k=0,\qquad \prod_{k=1}^{6}\zeta_k=-1 .
$$

**Proof.** The order of $\zeta_k=\zeta^{k-1}$ is $6/\gcd(6,k-1)$, which gives the row of orders. Complex conjugation sends $\zeta$ to $\zeta^{-1}=\zeta^5$, hence $\zeta_k=\zeta^{k-1}$ to $\zeta^{6-(k-1)}=\zeta_{8-k}$, which is the row of conjugates. The sum vanishes because the six roots are the roots of $x^6-1$, whose coefficient of $x^5$ is zero. The product is the constant term up to the sign $(-1)^6$: $x^6-1=\prod_k(x-\zeta_k)$ gives $-1=\prod_k(-\zeta_k)=\prod_k\zeta_k$, since $6$ is even.

### The Cyclotomic Factorisation

**Proposition.** Over $\mathbb{Q}$,

$$
x^6-1=(x-1)(x+1)(x^2+x+1)(x^2-x+1),
$$

the four factors being the cyclotomic polynomials $\Phi_1,\Phi_2,\Phi_3,\Phi_6$. The minimal polynomial of $\zeta$ over $\mathbb{Q}$ is $\Phi_6(x)=x^2-x+1$, of degree two.

**Proof.** The identity $x^6-1=(x^3-1)(x^3+1)$ and the factorisations $x^3-1=(x-1)(x^2+x+1)$, $x^3+1=(x+1)(x^2-x+1)$ give the product. The roots of $\Phi_6$ are the primitive sixth roots $\zeta,\zeta^5$, whose sum is $1$ and whose product is $1$; the polynomial $x^2-x+1$ has exactly those roots.

The factorisation matters for the arithmetic of the root, not for the algebra over $\mathbb{C}$: over $\mathbb{C}$ the polynomial splits into six linear factors, and the idempotents below are the six factors evaluated at $H$.

### The Discriminant

**Proposition.** The discriminant of $x^6-1$ is

$$
\operatorname{disc}(x^6-1)=\prod_{j<l}(\zeta_l-\zeta_j)^2=6^6=46656 .
$$

**Proof.** For $f(x)=x^n-a$ the discriminant is $(-1)^{(n-1)(n-2)/2}n^na^{n-1}$; at $n=6$, $a=1$ the sign is $(-1)^{10}=+1$ and the value is $6^6$. The product formula is the definition of the discriminant of a monic polynomial with simple roots.

The discriminant is nonzero, which is the statement that the six roots are distinct. This is the arithmetic shadow of the hypothesis that $H$ has a simple spectrum.

## The Root

### Definition

**Definition.** A **root** of $M_6(\mathbb{C})$ is an element $H\in M_6(\mathbb{C})$ such that

$$
H^6=I_6
$$

and the characteristic polynomial of $H$ has six distinct roots.

The word *root* is used in the sense of the corpus: an element whose power is a central value, here the unit, and the qualification *simple spectrum* is part of the definition of the root of this article.

**Proposition.** Let $H$ be a root. Then:

- $H$ is diagonalisable over $\mathbb{C}$;
- its eigenvalues are the six sixth roots of unity, each with multiplicity one;
- its characteristic and minimal polynomials are both $x^6-1$;
- $\operatorname{tr}H=0$ and $\det H=-1$.

**Proof.** The polynomial $x^6-1$ has the six distinct roots $\zeta_k$ and annihilates $H$. A matrix annihilated by a polynomial with distinct roots is diagonalisable, and its eigenvalues are among those roots. Six distinct eigenvalues in dimension six exhaust the spectrum, so each root occurs once, the characteristic polynomial is $\prod_k(x-\zeta_k)=x^6-1$, and the minimal polynomial, which has the same roots and divides $x^6-1$, is also $x^6-1$. The trace is the sum of the eigenvalues, which vanishes; the determinant is their product, which is $-1$.

**Corollary.** Every root is semisimple, hence is a semisimple element of $GL_6(\mathbb{C})$, and $H$ generates a cyclic subgroup of order six.

**Proof.** A diagonalisable matrix with eigenvalues of order dividing six satisfies $H^6=I$ and has $H^r\neq I$ for $0<r<6$, because $\zeta^r\neq1$. So $\langle H\rangle\cong\mathbb{Z}/6$.

### The Eigenlines

**Definition.** For a root $H$ and $k\in\{1,\dots,6\}$ put

$$
V_k=\ker(H-\zeta_kI_6).
$$

**Proposition.** The $V_k$ are six lines and

$$
\mathbb{C}^6=V_1\oplus V_2\oplus V_3\oplus V_4\oplus V_5\oplus V_6 .
$$

**Proof.** Each $V_k$ is the eigenspace of the eigenvalue $\zeta_k$, of dimension one because the spectrum is simple. Distinct eigenspaces of a diagonalisable matrix are independent, and their dimensions sum to six.

The decomposition is canonical: it is determined by $H$, and it is the finest decomposition of $\mathbb{C}^6$ on which $H$ acts by scalars. **The root is the decomposition.** Everything below is a rewriting of this sentence.

## The Lagrange Projectors

### The Formula

**Definition.** For a root $H$ and $k\in\{1,\dots,6\}$ the **Lagrange projector** $P_k$ is

$$
P_k=\prod_{l\neq k}\frac{H-\zeta_lI_6}{\zeta_k-\zeta_l}.
$$

The denominator is a nonzero complex number, by the distinctness of the roots, so the product is a well-defined polynomial in $H$ of degree five.

**Theorem.** For every root $H$ the six Lagrange projectors satisfy

$$
P_k^2=P_k,\qquad P_kP_l=\delta_{kl}P_k,\qquad \sum_{k=1}^{6}P_k=I_6,\qquad H=\sum_{k=1}^{6}\zeta_kP_k .
$$

Moreover $\operatorname{im}P_k=V_k$, $\ker P_k=\bigoplus_{l\neq k}V_l$, $\operatorname{rank}P_k=1$ and $\operatorname{tr}P_k=1$.

**Proof.** Let $L_k(x)=\prod_{l\neq k}(x-\zeta_l)/(\zeta_k-\zeta_l)$, the Lagrange interpolation polynomial of the six nodes $\zeta_1,\dots,\zeta_6$. It satisfies $L_k(\zeta_j)=\delta_{kj}$. On the eigenline $V_j$ the matrix $H$ acts as $\zeta_jI$, so $L_k(H)$ acts as $L_k(\zeta_j)I=\delta_{kj}I$. Therefore $L_k(H)$ is the identity on $V_k$ and zero on every other $V_l$; this is the projection onto $V_k$ along the sum of the other lines. The four displayed identities follow at once, and so do the statements about image, kernel and rank. The trace of a projection is its rank, so $\operatorname{tr}P_k=1$.

**Corollary (the idempotents determine the root).** $H=\sum_k\zeta_kP_k$, and the $P_k$ are polynomials in $H$. The map $H\mapsto(P_1,\dots,P_6)$ is injective, and its image is the set of complete orthogonal families of six rank-one idempotents.

**Proof.** The formula for $H$ is the spectral theorem read at the six eigenvalues: on $V_j$ both sides equal $\zeta_jI$. If two roots give the same family, the formula returns the same $H$. Conversely, a complete orthogonal family of six rank-one idempotents decomposes $\mathbb{C}^6$ into six lines, and $H=\sum\zeta_kP_k$ has the required spectrum and sixth power.

### The Fourier Form

**Theorem.** For every root $H$ and every $k$,

$$
P_k=\frac16\sum_{r=0}^{5}\zeta_k^{-r}H^r
=\frac16\left(I_6+\zeta_k^{-1}H+\zeta_k^{-2}H^2+\cdots+\zeta_k^{-5}H^5\right).
$$

**Proof.** On $V_j$ the right-hand side acts as $\frac16\sum_r\zeta_k^{-r}\zeta_j^rI=\frac16\sum_r(\zeta_j/\zeta_k)^rI$. The ratio $\zeta_j/\zeta_k$ is a sixth root of unity, equal to $1$ exactly when $j=k$; the geometric sum is $6$ in that case and $0$ otherwise. So the right-hand side is the projection onto $V_k$ along the other lines, which is $P_k$.

**Corollary (the inverse relations).** For every $r$,

$$
H^r=\sum_{k=1}^{6}\zeta_k^rP_k .
$$

**Proof.** Both sides act as $\zeta_j^rI$ on $V_j$.

The Fourier form exhibits the projectors as the **discrete Fourier transform of the powers of $H$**. It also gives the trace without a spectral argument:

$$
\operatorname{tr}P_k=\frac16\sum_{r=0}^{5}\zeta_k^{-r}\operatorname{tr}(H^r)=\frac16\operatorname{tr}(I_6)=1,
$$

because $\operatorname{tr}(H^r)=\sum_j\zeta_j^r=0$ for $1\le r\le5$, the sum of the $r$-th powers of the roots of $x^6-1$ being zero unless $6$ divides $r$.

### The Explicit Matrices

**Example (diagonal root).** Let

$$
H=\operatorname{diag}(\zeta_1,\zeta_2,\zeta_3,\zeta_4,\zeta_5,\zeta_6).
$$

Then $V_k=\mathbb{C}e_k$ and

$$
P_k=E_{kk},\qquad k=1,\dots,6 .
$$

The Lagrange formula returns the coordinate idempotents, and the Fourier form returns $\frac16\sum_r\zeta_k^{-r}\operatorname{diag}(\zeta_1^r,\dots,\zeta_6^r)=E_{kk}$.

**Example (the cyclic shift).** Let $\rho$ be the permutation matrix of the cycle $1\mapsto2\mapsto3\mapsto4\mapsto5\mapsto6\mapsto1$, acting on the standard column $e_j$ by $\rho e_j=e_{j-1}$ with indices modulo six. Then $\rho^6=I_6$, and the eigenvalues of $\rho$ are the six sixth roots, each once: the vector

$$
v_k=\sum_{j=1}^{6}\zeta_k^{j-1}e_j
$$

satisfies $\rho v_k=\zeta_kv_k$. So $\rho$ is a root, and the Fourier form gives

$$
P_k=\frac16\sum_{r=0}^{5}\zeta_k^{-r}\rho^r,
\qquad
(P_k)_{ij}=\frac16\zeta_k^{i-j},
$$

the second identity because $(\rho^r)_{ij}=\delta_{i,j-r}$. The matrix $P_2$, the projector of the eigenvalue $\zeta_2=\zeta$, is therefore

$$
P_2=\frac16
\begin{pmatrix}
1&\zeta^{-1}&\zeta^{-2}&\zeta^{-3}&\zeta^{-4}&\zeta^{-5}\\
\zeta&1&\zeta^{-1}&\zeta^{-2}&\zeta^{-3}&\zeta^{-4}\\
\zeta^2&\zeta&1&\zeta^{-1}&\zeta^{-2}&\zeta^{-3}\\
\zeta^3&\zeta^2&\zeta&1&\zeta^{-1}&\zeta^{-2}\\
\zeta^4&\zeta^3&\zeta^2&\zeta&1&\zeta^{-1}\\
\zeta^5&\zeta^4&\zeta^3&\zeta^2&\zeta&1
\end{pmatrix}.
$$

Each row is the previous row multiplied by $\zeta$; the matrix is circulant, its columns sum to $0$ because $k\neq1$, and $P_2^2=P_2$ is the identity $\frac1{36}\sum_{r,s}\zeta^{-r-s}\rho^{r+s}=\frac16\sum_t\zeta^{-t}\rho^t=P_2$. The projector $P_1$ of the eigenvalue $1$ is the all-ones matrix $\frac16J$.

**Remark.** The two examples are conjugate: $\rho$ is the regular representation of $\mathbb{Z}/6$ and $H$ is its decomposition into characters. Every root is conjugate to the diagonal one, by §*The Root Set*, so the two examples exhaust the isomorphism types of the pair $(H,\{P_k\})$.

## The $\mathbb{Z}/6$ Grading

### The Peirce Lines

The projectors cut the algebra into the thirty-six lines

$$
A_{kl}=P_kM_6(\mathbb{C})P_l=\{P_kAP_l:A\in M_6(\mathbb{C})\}=\mathbb{C}E_{kl},
$$

the last equality in the frame of the diagonal root, where $P_k=E_{kk}$. The product rule is the matrix-unit rule.

**Proposition.** $A_{kl}A_{mn}\subseteq\delta_{lm}A_{kn}$.

**Proof.** An element of $A_{kl}$ is $P_kAP_l$ and an element of $A_{mn}$ is $P_mBP_n$. The product is $P_kA(P_lP_m)BP_n=\delta_{lm}P_k(AB)P_n\in\delta_{lm}A_{kn}$.

**Corollary.** $M_6(\mathbb{C})=\bigoplus_{k,l}A_{kl}$, a direct sum of thirty-six lines.

**Proof.** The $P_k$ are complete and orthogonal, so $A=\sum_{k,l}P_kAP_l$ for every $A$, and the sum is direct because the $P_kAP_l$ are the entries of $A$ in the decomposition $\mathbb{C}^6=\bigoplus V_k$.

### The Grading

**Definition.** For $r\in\mathbb{Z}/6\mathbb{Z}$ put

$$
A_r=\bigoplus_{k-l\equiv r}A_{kl}.
$$

**Theorem.** The subspaces $A_r$ satisfy

$$
M_6(\mathbb{C})=\bigoplus_{r\in\mathbb{Z}/6\mathbb{Z}}A_r,
\qquad
A_rA_s\subseteq A_{r+s},
\qquad
\dim_{\mathbb{C}}A_r=6\ \text{for every }r .
$$

**Proof.** The first statement is the direct sum over the thirty-six pairs regrouped by $k-l$. For the second, $A_{kl}\subseteq A_r$ and $A_{mn}\subseteq A_s$ have $k-l\equiv r$ and $m-n\equiv s$; their product is either zero or $A_{kn}$, and $k-n=(k-l)+(l-n)\equiv r+s$ when $l=m$. For the dimension, fix $r$; for each of the six values of $k$ there is exactly one $l$ with $k-l\equiv r$, namely $l=k-r$, so $A_r$ is the sum of six lines.

**Proposition (the grading operators).** $H\in A_0$, and $H$ acts by the scalar $\zeta_k$ on $V_k$. The grading is read from the two commuting families of multiplications $L_{P_k}$ and $R_{P_k}$: on $A_{kl}$ the left multiplications have joint weight $k$ and the right multiplications have joint weight $l$, so

$$
A_r=\bigoplus_{k-l\equiv r}A_{kl}
=\{A\in M_6(\mathbb{C}):L(A)-R(A)\equiv rA \pmod 6\},
$$

where $L=\sum_k k\,L_{P_k}$ and $R=\sum_l l\,R_{P_l}$.

**Proof.** $H=\sum_j\zeta_jP_j$ is a linear combination of the $P_j$, hence lies in $A_0=\bigoplus_jA_{jj}$, and it acts by $\zeta_k$ on the line $V_k$. For $A\in A_{kl}$ one has $P_mA=\delta_{mk}A$ and $AP_m=\delta_{ml}A$, so $L(A)=kA$ and $R(A)=lA$; the difference is $(k-l)A$, whose class modulo six is $r$.

**Remark.** The grading is not the eigenspace decomposition of $\operatorname{ad}_H$. On $A_{kl}$ the commutator is $\operatorname{ad}_H(A)=(\zeta_k-\zeta_l)A$, and the differences $\zeta_k-\zeta_l$ are not sixth roots of unity; they depend on the pair, not on the class of $k-l$. The grading **is** the eigenspace decomposition of the automorphism $\operatorname{Ad}_H(A)=HAH^{-1}$: on $A_{kl}$ it acts by $\zeta_k/\zeta_l=\zeta^{k-l}$. The grading is by the difference of the Peirce labels, which is the **diagonal distance** of a matrix entry. It is a grading of the algebra, and $H$ is one of its degree-zero elements.

### The Two Coarser Gradings

The group $\mathbb{Z}/6$ has exactly four subgroups, $0$, $2\mathbb{Z}/6\cong\mathbb{Z}/3$, $3\mathbb{Z}/6\cong\mathbb{Z}/2$ and $\mathbb{Z}/6$, so the grading has exactly two proper coarsenings.

**The $\mathbb{Z}/2$ quotient.** Put

$$
A_{\text{even}}=A_0\oplus A_2\oplus A_4,\qquad
A_{\text{odd}}=A_1\oplus A_3\oplus A_5 .
$$

Both have dimension $18$, and $A_{\text{even}}$ is a subalgebra while $A_{\text{odd}}$ is a bimodule over it. In the frame, $A_{\text{even}}$ consists of the entries with $k-l$ even, that is $k$ and $l$ of the same parity: the matrices that preserve the decomposition

$$
\mathbb{C}^6=V_1\oplus V_3\oplus V_5\oplus V_2\oplus V_4\oplus V_6
$$

into the **even** and **odd** halves. The odd part consists of the entries that exchange the two halves. This is the $3+3$ split of *The Two Chiralities*.

**The $\mathbb{Z}/3$ quotient.** Put

$$
B_0=A_0\oplus A_3,\qquad B_1=A_1\oplus A_4,\qquad B_2=A_2\oplus A_5 .
$$

Each has dimension $12$, and $B_rB_s\subseteq B_{r+s}$ with indices modulo three. $B_0$ is the diagonal subalgebra $\mathbb{C}^6$; $B_1$ and $B_2$ are the entries two and four steps above the diagonal, together with their wraparound.

**Proposition.** The two quotients are the only proper coarsenings of the $\mathbb{Z}/6$ grading, and they are independent: neither is a coarsening of the other.

**Proof.** A coarsening of a $\mathbb{Z}/6$ grading is a grading by a quotient of $\mathbb{Z}/6$; the quotients are $\mathbb{Z}/2$ and $\mathbb{Z}/3$. The $\mathbb{Z}/2$ classes of $0$ and $3$ differ, while the $\mathbb{Z}/3$ classes of $0$ and $2$ differ, so neither grading refines the other.

### The Chirality Involution

**Definition.** The **chirality involution** of the root is

$$
\Gamma=H^3 .
$$

**Proposition.** $\Gamma^2=I_6$, $\Gamma\neq\pm I_6$, $\operatorname{tr}\Gamma=0$, and

$$
\Gamma=\sum_{k=1}^{6}(-1)^{k-1}P_k
=P_1-P_2+P_3-P_4+P_5-P_6 .
$$

The eigenvalues of $\Gamma$ are $+1$ with multiplicity three, on $V_1\oplus V_3\oplus V_5$, and $-1$ with multiplicity three, on $V_2\oplus V_4\oplus V_6$.

**Proof.** $(\zeta_k)^3=(-1)^{k-1}$; the spectral formula for a function of $H$ gives $\Gamma=\sum_k\zeta_k^3P_k$. The trace is the sum of three plus ones and three minus ones.

**Theorem (the $\mathbb{Z}/2$ grading is the chirality).** Conjugation by $\Gamma$ acts as $+1$ on $A_{\text{even}}$ and as $-1$ on $A_{\text{odd}}$, and $A_{\text{even}}$ is the fixed subalgebra of the involution $\operatorname{Ad}_\Gamma$.

**Proof.** $\Gamma=\sum_k(-1)^{k-1}P_k$ is a linear combination of the Peirce idempotents, hence $\Gamma P_k=P_k\Gamma=(-1)^{k-1}P_k$. For $A\in A_{kl}$, $\Gamma A\Gamma=(-1)^{k+l-2}A=(-1)^{k+l}A$, which is $+1$ exactly when $k$ and $l$ have the same parity, that is on $A_{\text{even}}$.

**Corollary (the coarse idempotents).** The two idempotents of the involution are

$$
\Pi_+=\frac{I_6+\Gamma}{2}=P_1+P_3+P_5,
\qquad
\Pi_-=\frac{I_6-\Gamma}{2}=P_2+P_4+P_6 .
$$

They are orthogonal, complete, of ranks $3$ and $3$, and each is a sum of three **primitive** Lagrange idempotents. They are therefore not primitive: the involution $\Gamma$ is a coarsening of the root, not a replacement for it.

This is the precise sense in which the order-two case is contained in the order-six case. The involution $\Gamma$ has a repeated eigenvalue, its projectors are sums of Lagrange projectors, and the primitive decomposition is still the six-root one.

## The Root Set

### The Conjugacy Class

The group $PGL_6(\mathbb{C})=GL_6(\mathbb{C})/\mathbb{C}^\times$ acts on $M_6(\mathbb{C})$ by conjugation, and the property of being a root is invariant under the action.

**Theorem.** The root set is a single orbit of $PGL_6(\mathbb{C})$, namely

$$
\{H\in M_6(\mathbb{C}):H^6=I_6,\ \text{six distinct eigenvalues}\}
=PGL_6(\mathbb{C})/T,
$$

where $T$ is the image in $PGL_6$ of the diagonal torus in the eigenbasis. Its complex dimension is

$$
\dim PGL_6-\dim T=35-5=30 .
$$

**Proof.** Every root is diagonalisable with the eigenvalues $\zeta_1,\dots,\zeta_6$, each once, so it is conjugate to the diagonal root $D=\operatorname{diag}(\zeta_1,\dots,\zeta_6)$. The roots are therefore one orbit. The stabiliser of $D$ in $GL_6$ is the group of invertible matrices commuting with $D$; since the eigenvalues are distinct, that is the diagonal torus $\mathbb{C}^{\times6}$, of dimension six, and its image in $PGL_6$ is the torus $T$ of dimension five. The orbit–stabiliser theorem and $\dim PGL_6=36-1=35$ give the dimension.

**Corollary (all roots are conjugate).** Any two roots are conjugate by an element of $PGL_6(\mathbb{C})$, and the conjugation carries the Lagrange family of one to the Lagrange family of the other.

**Proof.** Conjugation carries $H$ to $gHg^{-1}$ and the polynomial $P_k(H)$ to $gP_k(H)g^{-1}=P_k(gHg^{-1})$.

### The Flag and the Labelling

Forget the splitting of $\mathbb{C}^6$ into lines and keep the flag. A root determines the ordered flag

$$
0\subset V_1\subset V_1\oplus V_2\subset\cdots\subset V_1\oplus\cdots\oplus V_6=\mathbb{C}^6 .
$$

**Proposition.** The map from roots to full flags is surjective, and its fibre over a flag is the set of splittings of the flag, an affine space of dimension $15$.

**Proof.** Given a full flag, choosing a line $V_k$ in each successive quotient splits the flag; the choices are independent, of dimensions $5,4,3,2,1,0$, whose sum is $15$. The root is recovered from the splitting and the assignment of $\zeta_k$ to $V_k$.

**Proposition (the $6!$ of the labelling).** A root is an ordered decomposition into six lines, the $k$-th line carrying the eigenvalue $\zeta_k$. The symmetric group $S_6$, of order $6!=720$, acts freely by permuting the positions and hence the roots; the quotient is the space of unordered decompositions. Over that quotient the root set is a cover of degree $6!$.

**Proof.** Write the root as $(L_1,\dots,L_6)$ with $H|_{L_k}=\zeta_kI$. Permuting the positions gives $(L_{\sigma(1)},\dots,L_{\sigma(6)})$, the root $\sum_k\zeta_kP_{L_{\sigma(k)}}$, which differs from $H$ for $\sigma\neq\mathrm{id}$ because the six lines are distinct. The action is free. The fibre over the unordered set $\{L_1,\dots,L_6\}$ is the set of bijections from the six positions to the six lines, of cardinality $6!$.

**Remark.** The two numbers $30$ and $15$ are not in conflict. The root set has dimension $30$; the flag variety has dimension $15$; the fibre of the forgetful map is the $15$-dimensional space of splittings. The $6!$ is a discrete relabelling, not a continuous parameter: the root set is a $6!$-fold cover of the space of unordered decompositions. The map to the flag variety is defined on the root, where the eigenvalues order the lines; it does not descend to the unordered space.

### The Root and the Gauge

The orbit count is the first half of the count of the frame. The frame of $M_6(\mathbb{C})$ is an ordered basis up to an overall scalar; the root fixes the six lines, and the gauge fixes one scale in each line. The root contributes $30$ parameters, the gauge $5$, and

$$
30+5=35=\dim PGL_6 .
$$

The gauge is the subject of *The Frame, the Simple Nilpotents and the Gauge*. The two counts meet because the frame is $PGL_6$ itself: a root is a point of $PGL_6/T$ and a gauge is a point of $T$.

## The Order-Two Case

**The root of $+1$ is the order-two case of the same construction.** Let $E\in M_2(\mathbb{C})$ satisfy $E^2=I_2$ with distinct eigenvalues $+1,-1$. The two Lagrange projectors are

$$
P_+=\frac{I_2+E}{2},\qquad P_-=\frac{I_2-E}{2},
$$

idempotent, orthogonal, complete, and $E=P_+-P_-$. This is the frame of the biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$, whose Peirce decomposition has four one-dimensional corners. **No second root is needed.** The six-root construction of this article reduces to it at $n=2$: two roots of unity, two projectors, one grading by $\mathbb{Z}/2$.

For $n=6$ the same reduction is available for the involution $\Gamma=H^3$: its two projectors are $\Pi_\pm=(I\pm\Gamma)/2$, of ranks three. They are the coarse idempotents of §*The Chirality Involution*, not primitive idempotents, and the primitive ones remain the six $P_k$. The order-two case is thus a **quotient** of the order-six case, obtained by grouping the six lines into the even and the odd three.

**Remark (why one root suffices).** In the biquaternion articles a frame is built from a root of $+1$ together with a second root anticommuting with it, because $M_2$ has only two eigenvalues and the two mixed units need a relative scale. In $M_6$ the root has six eigenvalues; the six lines are already distinct and the mixed units between them are indexed by pairs. The relative scales are the gauge, not a second root. **The root is the only primitive object; the gauge is a choice of frame inside it.**

## Summary

A root of $M_6(\mathbb{C})$ is a matrix $H$ with $H^6=I_6$ and six distinct eigenvalues. Its six eigenspaces are six lines, and the Lagrange projectors

$$
P_k=\prod_{l\neq k}\frac{H-\zeta_lI_6}{\zeta_k-\zeta_l}
=\frac16\sum_{r=0}^{5}\zeta_k^{-r}H^r
$$

are primitive idempotents, orthogonal and complete, with $H=\sum_k\zeta_kP_k$.

$$
\boxed{\ \text{One root of order six gives the six primitive idempotents; no second object is primitive.}\ }
$$

The projectors grade the algebra by $\mathbb{Z}/6$, with six graded pieces $A_r$ of dimension six each, and the two quotients $\mathbb{Z}/2$ and $\mathbb{Z}/3$ are the only coarser gradings. The cube $\Gamma=H^3$ is the chirality involution: it has eigenvalues $+1$ and $-1$, each of multiplicity three, and its projectors are the sums $P_1+P_3+P_5$ and $P_2+P_4+P_6$.

The root set is one conjugacy class of $PGL_6$, of complex dimension $30=35-5$; the stabiliser is the five-dimensional torus, which is the gauge. The $6!$ relabellings of the six lines are discrete, and the flag variety is the $15$-dimensional image of the forgetful map.

| Object | Data |
|---|---|
| Root | $H^6=I_6$, six distinct eigenvalues |
| Idempotents | $P_k$, $k=1,\dots,6$, primitive, rank one |
| Spectral formula | $H=\sum_k\zeta_kP_k$ |
| Grading | $M_6=\bigoplus_{r\in\mathbb{Z}/6}A_r$, $\dim A_r=6$ |
| Chirality | $\Gamma=H^3$, $3+3$ split |
| Root set | $PGL_6/T$, complex dimension $30$ |
| Gauge | $T\cong(\mathbb{C}^\times)^5$, dimension $5$ |
| Total frame | $30+5=35=\dim PGL_6$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\zeta=e^{2\pi i/6}$ | the primitive sixth root |
| $\zeta_k=\zeta^{k-1}$ | the six sixth roots, $k=1,\dots,6$ |
| $H$ | the root, $H^6=I_6$ with simple spectrum |
| $V_k=\ker(H-\zeta_kI_6)$ | the six eigenlines |
| $P_k$ | the Lagrange projector onto $V_k$ |
| $A_{kl}=P_kM_6P_l$ | the thirty-six Peirce lines |
| $A_r=\bigoplus_{k-l\equiv r}A_{kl}$ | the $\mathbb{Z}/6$ graded pieces, $\dim A_r=6$ |
| $\Gamma=H^3$ | the chirality involution |
| $\Pi_\pm=(I_6\pm\Gamma)/2$ | the coarse idempotents of ranks $3,3$ |
| $PGL_6/T$ | the root set, complex dimension $30$ |

## Further Reading

- [The Matrix Algebra $M_6(\mathbb{C})$](the-matrix-algebra-m6c.html), for the product, the trace, the determinant and the group $PGL_6$.
- [The Peirce Decomposition](the-peirce-decomposition-of-m6c.html), for the decomposition of $M_6$ by the six projectors and the coarse split by one of them.
- [The Frame, the Simple Nilpotents and the Gauge](the-frame-the-simple-nilpotents-and-the-gauge-of-m6c.html), for the nilpotents $E_{12},\dots,E_{56}$ and the five-parameter gauge.
- [The Two Chiralities](the-two-chiralities-of-m6c.html), for the $3+3$ split and the mass block.
- [Primitive Idempotents and Minimal Left Ideals](primitive-idempotents-and-minimal-left-ideals.html), for the general theory of the idempotents and the modules they generate.
- [Idempotents and Involutions of an Algebra](idempotents-and-involutions-of-an-algebra.html), for the correspondence between idempotents and involutions in the general case.
- [Complementary Idempotents and the Peirce Decomposition](complementary-idempotents-and-the-peirce-decomposition.html), for the Peirce decomposition relative to a complete orthogonal family.
- [Flag Manifolds](flag-manifolds.html), for the full flag variety and its dimension.
- [Grassmannians and Stiefel Manifolds](grassmannians-and-stiefel-manifolds.html), for the partial flags and the Grassmannians used in the coarse splits.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the representation of $\mathbb{Z}/6$ and the discrete Fourier decomposition of a cyclic group.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the spectral theorem, the Lagrange interpolation formula and the trace of a projection.
