# __Exercise: The CHSH Inequality and Tsirelson's Bound__

## Introduction

This article is one of a series of **worked exercises** that illustrate quantum physics in two parallel presentations: the standard Hilbert-space formulation, and the biquaternion formulation developed in the companion articles. The goal is not to derive new physics, but to give a concrete, computationally explicit demonstration of the correspondence between the two formalisms.

Each exercise in the series is solved twice: first in the standard way, then in the biquaternion way. The results agree, as they must: the two formulations are the same mathematics in different notation.

The earlier exercises treated a single qubit, an entangled pair in the singlet state, the reduced state of one subsystem, and — in *Exercise: The Correlation Function of the Bell States* — the full spin correlation function of all four Bell states. This exercise uses that last result and goes one step further. It treats the **CHSH inequality** of Clauser, Horne, Shimony, and Holt (1969), which is the two-settings-per-party form of Bell's theorem and the inequality actually tested in the loophole-free experiments, and it derives the two numbers that give the inequality its content:

- the **classical bound** $|S| \le 2$, valid for every local hidden-variable model;
- the **quantum bound** $|S| \le 2\sqrt{2}$, Tsirelson's bound.

The exercise is built directly on the parent articles. The two-qubit arena — the tensor-product algebra $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$, its trace, and the partial traces — is fixed by *Entangled Subsystems in the Biquaternion Framework*. The four Bell idempotents $P_\epsilon$ and their classification by the sign pattern $\epsilon_1\epsilon_2\epsilon_3=+1$ are fixed by *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$*. The correlation function

$$
E(\vec u_1, \vec u_2) = \mathrm{Tr}\!\left(P_\epsilon\circ\bigl((i\vec u_1)\otimes(i\vec u_2)\bigr)\right) = -\sum_{j\in\{x,y,z\}}\epsilon_j\,a_j b_j
$$

is the result of *Exercise: The Correlation Function of the Bell States*, and it is the input to every quantum computation below. No Bell projector is re-derived; the exercise applies the parent results.

Two honest statements belong in the introduction, and they are revisited at the end.

First, **the framework reproduces both bounds; it does not explain why nature stops at $2\sqrt{2}$.** The derivation below is the standard operator-norm argument, translated into the algebra. It shows that the quantum bound follows from the tensor-product structure and the $\pm1$ spectrum of the observables. It does not supply a principle, beyond that algebra, from which the value $2\sqrt{2}$ could be anticipated. The no-signaling maximum is $4$, and the framework — like ordinary quantum physics — offers no reason why the physical world realizes $2\sqrt{2}$ rather than $4$ other than the fact that it is quantum-mechanical.

Second, the sharp bound is obtained **after** the identification $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$, by the spectral norm of that matrix algebra. The framework's own positive-definite quadratic form, the Euclidean form $\mathrm{Sc}(x x^{*})$ of the companion articles, is (up to the trace normalisation) the Frobenius norm of the matrix image, and it yields only the trivial bound $4$. This is a genuine gap in the framework's internal resources, and it is labelled as such in the biquaternion solution: the framework does not contain, by itself, the norm that gives Tsirelson's bound. What it contains is the algebra whose matrix representation carries that norm.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$. The quaternion units are $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $e_k^2 = -e_t$ and the cyclic products $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$; $i$ is the scalar imaginary, $i^2=-1$. On a single factor the trace is twice the scalar part, $\mathrm{Tr}_\mathbb{B}(\tilde{H}) = 2\,\mathrm{Sc}(\tilde{H})$, and on the tensor product $\mathrm{Tr}(x\otimes y) = \mathrm{Tr}_\mathbb{B}(x)\cdot\mathrm{Tr}_\mathbb{B}(y)$, with $\mathrm{Tr}_\mathbb{B}(e_t)=2$ and $\mathrm{Tr}_\mathbb{B}(e_k)=0$. The isomorphism is the one fixed by *Quantum Physics in Biquaternionic Form*,

$$
e_t\mapsto I_2,\qquad \vec e_x\mapsto -i\sigma_1,\qquad \vec e_y\mapsto -i\sigma_2,\qquad \vec e_z\mapsto -i\sigma_3,
$$

where $\sigma_1,\sigma_2,\sigma_3$ are the Pauli matrices; the image of $ie_k$ is $\sigma_k$. The three Pauli matrices are also written $\boldsymbol{\sigma}=(\sigma_1,\sigma_2,\sigma_3)$.

## The Exercise

Two spin-$\tfrac{1}{2}$ particles are prepared in one of the four **Bell states**, and the two particles are measured by two separated parties, Alice and Bob.

Alice chooses one of two unit directions $\vec u_1$ or $\vec u_1'$; Bob chooses one of two unit directions $\vec u_2$ or $\vec u_2'$. Each measurement has two outcomes, labelled $\pm1$. Write

$$
E(\vec u_1, \vec u_2) = \bigl\langle \bigl(\vec u_1\cdot\boldsymbol{\sigma}_1\bigr)\bigl(\vec u_2\cdot\boldsymbol{\sigma}_2\bigr)\bigr\rangle
$$

for the **correlation** of the two outcomes, where $\boldsymbol{\sigma}_1=\boldsymbol{\sigma}\otimes I$ and $\boldsymbol{\sigma}_2=I\otimes\boldsymbol{\sigma}$. The **CHSH combination** is

$$
S = E(\vec u_1, \vec u_2) - E(\vec u_1, \vec u_2') + E(\vec u_1', \vec u_2) + E(\vec u_1', \vec u_2').
$$

The exercise has four parts.

1. **The classical bound.** Show that every local hidden-variable model satisfies $|S|\le 2$.
2. **The quantum correlators.** Using the Bell idempotents and the correlation function of the parent articles, express $E(\vec u_1,\vec u_2)$ for each of the four Bell states and hence $S$ in terms of the measurement directions and the sign pattern $\epsilon$.
3. **The optimal configuration.** For the singlet, maximize $|S|$ over the four measurement directions and show that the maximum is $2\sqrt{2}$. Show that all four Bell states attain the same maximum.
4. **Tsirelson's bound.** Show that no quantum state — entangled, mixed, or otherwise — can exceed $|S|=2\sqrt{2}$.

The exercise is solved first in the standard formulation and then in the biquaternion formulation, in parallel steps.

## Solution in the Standard Formulation

### Step 1: The CHSH observables

For a unit vector $\vec u_1=(a_1,a_2,a_3)$, write $A(\vec u_1)=\vec u_1\cdot\boldsymbol{\sigma}=\sum_j a_j\sigma_j$ for the single-qubit observable, so that

$$
A(\vec u_1)\otimes I = \vec u_1\cdot\boldsymbol{\sigma}_1,\qquad I\otimes A(\vec u_2) = \vec u_2\cdot\boldsymbol{\sigma}_2 .
$$

Each $A(\vec u_1)$ is Hermitian with eigenvalues $\pm1$ and square $A(\vec u_1)^2=I$. Write

$$
A=A(\vec u_1),\quad A'=A(\vec u_1'),\quad B=B(\vec u_2),\quad B'=B(\vec u_2')
$$

for short. The correlation is the expectation of the tensor-product observable $A\otimes B$, and the CHSH combination is the expectation of the **Bell operator**

$$
S = A\otimes B - A\otimes B' + A'\otimes B + A'\otimes B',
$$

so that $S=\langle S\rangle$. Every property of $S$ below is a property of the single Hermitian operator $S$.

Equivalently, one may expand in the Pauli-string basis. With the correlation matrix

$$
T_{jk} = \langle \sigma_j\otimes\sigma_k\rangle = \mathrm{Tr}\!\left(\rho\,\sigma_j\otimes\sigma_k\right),
$$

the correlation function is the bilinear form $E(\vec u_1,\vec u_2)=\vec u_1^T T\,\vec u_2$, and the CHSH combination is a quadratic expression in the four directions.

### Step 2: The classical bound

A **local hidden-variable model** assigns to each measurement a pre-existing outcome that depends on the measurement direction and on a shared variable $\lambda$ distributed with density $p(\lambda)$:

$$
A_\lambda(\vec u_1),\; A_\lambda(\vec u_1'),\; B_\lambda(\vec u_2),\; B_\lambda(\vec u_2') \in \{\pm1\},
\qquad
E(\vec u_1,\vec u_2) = \int d\lambda\,p(\lambda)\,A_\lambda(\vec u_1)B_\lambda(\vec u_2).
$$

The outcomes for Alice depend only on $\vec u_1$ and $\lambda$; those for Bob only on $\vec u_2$ and $\lambda$. Substituting into $S$ and grouping by party,

$$
S = \int d\lambda\,p(\lambda)\Bigl[\,A_\lambda(\vec u_1)\bigl(B_\lambda(\vec u_2)-B_\lambda(\vec u_2')\bigr)
+ A_\lambda(\vec u_1')\bigl(B_\lambda(\vec u_2)+B_\lambda(\vec u_2')\bigr)\Bigr].
$$

Fix $\lambda$. The two signs $B_\lambda(\vec u_2)$ and $B_\lambda(\vec u_2')$ are each $\pm1$, so exactly one of the two combinations $B_\lambda(\vec u_2)-B_\lambda(\vec u_2')$ and $B_\lambda(\vec u_2)+B_\lambda(\vec u_2')$ vanishes and the other is $\pm2$. Hence the bracket is $\pm2$ in absolute value for every $\lambda$, and

$$
|S| \;\le\; \int d\lambda\,p(\lambda)\cdot 2 \;=\; 2 .
$$

This is the classical (CHSH) bound. It is tight: the deterministic model $A_\lambda=A_\lambda'=+1$, $B_\lambda=+1$, $B_\lambda'=-1$ gives $S=2$.

### Step 3: The quantum correlators of the Bell states

The parent exercise computed the correlation function of each Bell state. Its result is

$$
E(\vec u_1, \vec u_2) = -\sum_{j\in\{x,y,z\}}\epsilon_j\,a_j b_j = \vec u_1^T T\,\vec u_2,
\qquad
T = -\mathrm{diag}(\epsilon_1,\epsilon_2,\epsilon_3),
$$

for the Bell state with sign pattern $\epsilon=(\epsilon_1,\epsilon_2,\epsilon_3)$, $\epsilon_1\epsilon_2\epsilon_3=+1$. The four patterns and their correlation matrices are:

| Bell state | $\epsilon=(\epsilon_1,\epsilon_2,\epsilon_3)$ | $T=-\mathrm{diag}(\epsilon)$ | $E(\vec u_1,\vec u_2)$ |
|---|---|---|---|
| $\lvert\Psi^-\rangle$ | $(+1,+1,+1)$ | $\mathrm{diag}(-1,-1,-1)$ | $-\vec u_1\cdot\vec u_2$ |
| $\lvert\Phi^+\rangle$ | $(-1,+1,-1)$ | $\mathrm{diag}(+1,-1,+1)$ | $a_1b_1-a_2b_2+a_3b_3$ |
| $\lvert\Phi^-\rangle$ | $(+1,-1,-1)$ | $\mathrm{diag}(-1,+1,+1)$ | $-a_1b_1+a_2b_2+a_3b_3$ |
| $\lvert\Psi^+\rangle$ | $(-1,-1,+1)$ | $\mathrm{diag}(+1,+1,-1)$ | $a_1b_1+a_2b_2-a_3b_3$ |

Only the singlet has $T=-I$ and hence the rotationally invariant correlation $E=-\vec u_1\cdot\vec u_2$. The other three have a correlation matrix with one diagonal entry of the opposite sign; their correlations depend on the directions.

Substituting into the CHSH combination, for a state with sign pattern $\epsilon$,

$$
S_\epsilon = -\sum_{j\in\{x,y,z\}}\epsilon_j\bigl(a_jb_j - a_jb'_j + a'_jb_j + a'_jb'_j\bigr).
$$

For the singlet, $\epsilon_j=+1$ for all $j$, so

$$
S_{\Psi^-} = -\vec u_1\cdot\vec u_2 + \vec u_1\cdot\vec u_2' - \vec u_1'\cdot\vec u_2 - \vec u_1'\cdot\vec u_2'
= -\vec u_1\cdot(\vec u_2-\vec u_2') - \vec u_1'\cdot(\vec u_2+\vec u_2').
$$

### Step 4: The optimal configuration and the value $2\sqrt{2}$

Consider first the singlet. With $\vec u_2$ and $\vec u_2'$ held fixed, the two terms in $S_{\Psi^-}$ involve $\vec u_1$ and $\vec u_1'$ separately, so each can be maximized independently over the unit sphere:

$$
\max_{|\vec u_1|=1}\bigl[-\vec u_1\cdot(\vec u_2-\vec u_2')\bigr] = |\vec u_2-\vec u_2'|,
\qquad
\max_{|\vec u_1'|=1}\bigl[-\vec u_1'\cdot(\vec u_2+\vec u_2')\bigr] = |\vec u_2+\vec u_2'| .
$$

Therefore

$$
\max_{|\vec u_1|=|\vec u_1'|=1} S_{\Psi^-} = |\vec u_2-\vec u_2'| + |\vec u_2+\vec u_2'|
= \sqrt{2-2c} + \sqrt{2+2c} = \sqrt{2}\left(\sqrt{1-c}+\sqrt{1+c}\right),
$$

with $c=\vec u_2\cdot\vec u_2'$. The function is maximized at $c=0$, i.e. at $\vec u_2\perp\vec u_2'$, where it takes the value $2\sqrt{2}$. The directions

$$
\vec u_1=\vec u_x,\quad \vec u_1'=\vec u_z,\quad
\vec u_2=\frac{\vec u_x+\vec u_z}{\sqrt{2}},\quad \vec u_2'=\frac{-\vec u_x+\vec u_z}{\sqrt{2}}
$$

realize this configuration, and direct substitution gives $S_{\Psi^-}=-2\sqrt{2}$; reversing the signs of $\vec u_1$ and $\vec u_1'$ gives $+2\sqrt{2}$.

Now consider the other three Bell states. They are related to the singlet by **local unitary operations**: the parent article *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$* shows that conjugating $P_{\Phi^+}$ by the unit real quaternions $e_t,\vec e_x,\vec e_y,\vec e_z$ on the first factor permutes the four Bell idempotents. In Hilbert-space terms the four Bell states lie in a single local-unitary orbit. The CHSH maximum is invariant under local unitaries, because a local unitary simply maps the set of measurement directions onto itself; the maximum for each Bell state is therefore also $2\sqrt{2}$.

The explicit optimal configuration for a non-singlet Bell state is worth recording. Its correlation matrix $T=-\mathrm{diag}(\epsilon)$ has diagonal entries $T_{jj}=-\epsilon_j$, two of which are equal because $\epsilon_1\epsilon_2\epsilon_3=+1$ guarantees at least two equal signs. Choose the plane spanned by the two axes $j,k$ with $\epsilon_j=\epsilon_k$, put $\vec u_1,\vec u_1'$ along those two axes, and put $\vec u_2,\vec u_2'$ at $\pm45^\circ$ within that plane,

$$
\vec u_1=\vec u_j,\quad \vec u_1'=\vec u_k,\quad
\vec u_2=\frac{\vec u_j+\vec u_k}{\sqrt{2}},\quad \vec u_2'=\frac{-\vec u_j+\vec u_k}{\sqrt{2}} .
$$

Then $S_\epsilon = \sqrt{2}\,(T_{jj}+T_{kk}) = -\sqrt{2}\,(\epsilon_j+\epsilon_k) = \mp 2\sqrt{2}$, so $|S_\epsilon|=2\sqrt{2}$. For example, $\lvert\Phi^+\rangle$ with $\epsilon=(-1,+1,-1)$ uses the plane of $\vec u_x$ and $\vec u_z$ and gives $S=+2\sqrt{2}$; $\lvert\Phi^-\rangle$ with $\epsilon=(+1,-1,-1)$ uses $\vec u_y,\vec u_z$; $\lvert\Psi^+\rangle$ with $\epsilon=(-1,-1,+1)$ uses $\vec u_x,\vec u_y$. Thus **all four Bell states attain Tsirelson's bound**.

### Step 5: Tsirelson's bound

It remains to show that no state and no directions can do better than $2\sqrt{2}$. The proof is a single operator identity.

Start from the grouped form of the Bell operator,

$$
S = A\otimes(B-B') + A'\otimes(B+B'),
$$

and square it:

$$
S^2 = A^2\otimes(B-B')^2 + A'^2\otimes(B+B')^2
+ AA'\otimes(B-B')(B+B') + A'A\otimes(B+B')(B-B').
$$

Now $A^2=A'^2=I$, and the anticommutators give

$$
(B-B')^2 = 2I-\{B,B'\},\qquad (B+B')^2 = 2I+\{B,B'\},
$$

so the first two terms sum to $4\,I\otimes I$. In the cross terms,

$$
(B-B')(B+B') = [B,B'],\qquad (B+B')(B-B') = -[B,B'],
$$

so the cross terms collapse to $[A,A']\otimes[B,B']$. Hence the exact identity

$$
S^2 = 4\,I\otimes I + [A,A']\otimes[B,B'] .
$$

The commutators can be evaluated in closed form. For two directions $\vec u_1,\vec u_1'$ and $u=\vec u_1\times\vec u_1'$,

$$
AA' = (\vec u_1\cdot\boldsymbol{\sigma})(\vec u_1'\cdot\boldsymbol{\sigma})
= (\vec u_1\cdot\vec u_1')\,I + i\,(u\cdot\boldsymbol{\sigma}),
$$

so $[A,A']=2i\,(u\cdot\boldsymbol{\sigma})$; similarly $[B,B']=2i\,(v\cdot\boldsymbol{\sigma})$ with $v=\vec u_2\times\vec u_2'$. Therefore

$$
S^2 = 4\,I\otimes I - 4\,(u\cdot\boldsymbol{\sigma})\otimes(v\cdot\boldsymbol{\sigma}).
$$

The eigenvalues of $(u\cdot\boldsymbol{\sigma})$ are $\pm|u|$, so the eigenvalues of the tensor product are $\pm|u||v|$, and those of $S^2$ are $4\bigl(1\mp|u||v|\bigr)$. Since $|u|=|\sin\theta_{aa'}|\le1$ and $|v|=|\sin\theta_{bb'}|\le1$, the largest eigenvalue of $S^2$ is at most $8$, and every eigenvalue of $S$ is bounded in absolute value by $2\sqrt{2}$:

$$
\|S\| \le 2\sqrt{2}.
$$

For any state $\rho$, the expectation $\langle S\rangle=\mathrm{Tr}(\rho S)$ is a convex combination of the eigenvalues of $S$, so $|S|=|\langle S\rangle|\le 2\sqrt{2}$. This is Tsirelson's bound (Cirel'son, 1980). It is saturated, as Step 4 showed, by every Bell state at $\vec u_1\perp\vec u_1'$, $\vec u_2\perp\vec u_2'$ with the optimal relative orientation.

## Solution in the Biquaternion Formulation

### Step 1: The CHSH element

In the biquaternion framework the two-qubit observables live in $\mathbb{M}_+\otimes\mathbb{M}_+\subset\mathbb{B}\otimes\mathbb{B}$. The single-qubit observable along $\vec u_1$ is the Hermitian element $i\vec u_1=i\sum_j a_j e_j$, whose image under the isomorphism is $\vec u_1\cdot\boldsymbol{\sigma}$. The correlation observable of the parent exercise is

$$
\tilde{H}_{ab} = (i\vec u_1)\otimes(i\vec u_2),
$$

and the correlation is the tensor-product trace pairing $E(\vec u_1,\vec u_2)=\mathrm{Tr}(P_\epsilon\circ\tilde{H}_{ab})$.

Assembling the four settings, the **CHSH element** is

$$
\tilde{\mathcal{S}}
= (i\vec u_1)\otimes(i\vec u_2) - (i\vec u_1)\otimes(i\vec u_2')
+ (i\vec u_1')\otimes(i\vec u_2) + (i\vec u_1')\otimes(i\vec u_2'),
$$

a single Hermitian element of $\mathbb{M}_+\otimes\mathbb{M}_+$. Because the isomorphism $e_k\mapsto-i\sigma_k$ carries $i\vec u_1$ to $\vec u_1\cdot\boldsymbol{\sigma}$ and respects the tensor product, it carries $\tilde{\mathcal{S}}$ to the Bell operator $S$ of the standard formulation. The CHSH combination is therefore the Born pairing of the state with one element of the algebra,

$$
S = \mathrm{Tr}\bigl(P_\epsilon\circ\tilde{\mathcal{S}}\bigr),
$$

and every statement about $S$ is a statement about $\tilde{\mathcal{S}}$.

### Step 2: The expectation on a Bell idempotent

By linearity of the trace pairing, the expectation of $\tilde{\mathcal{S}}$ on $P_\epsilon$ is the CHSH combination of the four single-setting correlations. The parent result $E(\vec u_1,\vec u_2)=-\sum_j\epsilon_j a_jb_j$ gives immediately

$$
S_\epsilon = -\sum_{j\in\{x,y,z\}}\epsilon_j\bigl(a_jb_j - a_jb'_j + a'_jb_j + a'_jb'_j\bigr),
$$

which is exactly the standard expression of Step 3. For the singlet, $\epsilon_j=+1$, and

$$
S_{\Psi^-} = -\vec u_1\cdot\vec u_2 + \vec u_1\cdot\vec u_2' - \vec u_1'\cdot\vec u_2 - \vec u_1'\cdot\vec u_2'
= -\vec u_1\cdot(\vec u_2-\vec u_2') - \vec u_1'\cdot(\vec u_2+\vec u_2').
$$

The optimization of Step 4 is then carried out in the algebra exactly as before, since it uses only the real vectors $\vec u_1,\vec u_1',\vec u_2,\vec u_2'$ and the bilinear form. The result is the same: $|S_\epsilon|=2\sqrt{2}$ for every Bell state.

It is worth recording the same content in the language of **joint probabilities**, because that is the form in which the CHSH combination enters the operational discussion of the companion article *The Quantum–Classical Divide in the Biquaternion Framework*. With the single-qubit idempotents $\tilde\Pi(\pm\vec u_1)=\tfrac12(e_t\pm i\vec u_1)$, the joint probability of outcomes $\pm,\pm$ is the Born pairing applied twice:

$$
p_\epsilon(\pm,\pm\mid\vec u_1,\vec u_2)
= \mathrm{Tr}\Bigl(P_\epsilon\circ\bigl(\tilde\Pi(\pm\vec u_1)\otimes \tilde\Pi(\pm\vec u_2)\bigr)\Bigr).
$$

Expanding the product of projectors gives $p(+,+)=p(-,-)=\tfrac14\bigl(1+E(\vec u_1,\vec u_2)\bigr)$ and $p(+,-)=p(-,+)=\tfrac14\bigl(1-E(\vec u_1,\vec u_2)\bigr)$ — the cross terms vanish because the single-particle expectations $\langle\sigma_j\otimes I\rangle$ and $\langle I\otimes\sigma_k\rangle$ are zero in every Bell state — and the CHSH combination is the corresponding combination of joint probabilities,

$$
S = \bigl[p(++)+p(--)-p(+-)-p(-+)\bigr]_{\vec u_1,\vec u_2}
-\bigl[p(++)+p(--)-p(+-)-p(-+)\bigr]_{\vec u_1,\vec u_2'}
+\cdots .
$$

### Step 3: The square of the CHSH element

The counterpart of the standard identity $S^2=4I+[A,A']\otimes[B,B']$ is a clean computation in $\mathbb{B}\otimes\mathbb{B}$. Collecting terms,

$$
\tilde{\mathcal{S}}
= -\vec u_1\otimes(\vec u_2-\vec u_2') - \vec u_1'\otimes(\vec u_2+\vec u_2').
$$

Write $\tilde{Q}=\vec u_1\otimes(\vec u_2-\vec u_2')$ and $\tilde{R}=\vec u_1'\otimes(\vec u_2+\vec u_2')$, so that $\tilde{\mathcal{S}}=-(\tilde{Q}+\tilde{R})$ and

$$
\tilde{\mathcal{S}}^2 = \tilde{Q}^2 + \tilde{R}^2 + XY + YX .
$$

Each term is evaluated with the quaternion multiplication rules. First, $\vec u_1^2=-e_t$ and $(\vec u_2-\vec u_2')^2=-|\vec u_2-\vec u_2'|^2e_t=-2(1-c)e_t$ with $c=\vec u_2\cdot\vec u_2'$, so

$$
\tilde{Q}^2 = \vec u_1^2\otimes(\vec u_2-\vec u_2')^2 = (-e_t)\otimes\bigl(-2(1-c)e_t\bigr) = 2(1-c)\,e_t\otimes e_t .
$$

Similarly, $(\vec u_2+\vec u_2')^2=-2(1+c)e_t$, so

$$
\tilde{R}^2 = 2(1+c)\,e_t\otimes e_t,
\qquad
\tilde{Q}^2+\tilde{R}^2 = 4\,e_t\otimes e_t .
$$

For the cross terms, the anti-commutativity of distinct quaternion units gives

$$
(\vec u_2-\vec u_2')(\vec u_2+\vec u_2') = [\vec u_2,\vec u_2'] = 2\,(\vec u_2\times\vec u_2'),
\qquad
(\vec u_2+\vec u_2')(\vec u_2-\vec u_2') = -[\vec u_2,\vec u_2'],
$$

and therefore

$$
XY+YX = [\vec u_1,\vec u_1']\otimes 2(\vec u_2\times\vec u_2') = 4\,(\vec u_1\times\vec u_1')\otimes(\vec u_2\times\vec u_2').
$$

Collecting the pieces,

$$
\boxed{\;\tilde{\mathcal{S}}^2
= 4\Bigl(e_t\otimes e_t + (\vec u_1\times\vec u_1')\otimes(\vec u_2\times\vec u_2')\Bigr).\;}
$$

This is the biquaternion form of the Bell-operator identity. The square of the CHSH element is the identity of the algebra plus a single tensor product of two cross products.

### Step 4: The bound, and a gap in the framework's own norms

Under the isomorphism, a pure quaternion $u=\sum_j u_j e_j$ maps to $-i\,(u\cdot\boldsymbol{\sigma})$, so

$$
(\vec u_1\times\vec u_1')\otimes(\vec u_2\times\vec u_2')
\;\longmapsto\;
-(u\cdot\boldsymbol{\sigma})\otimes(v\cdot\boldsymbol{\sigma}),
\qquad
u=\vec u_1\times\vec u_1',\;\; v=\vec u_2\times\vec u_2' .
$$

The image of $\tilde{\mathcal{S}}^2$ is therefore $4\bigl[I\otimes I-(u\cdot\boldsymbol{\sigma})\otimes(v\cdot\boldsymbol{\sigma})\bigr]$, with eigenvalues $4(1\mp|u||v|)$; the eigenvalues of the image of $\tilde{\mathcal{S}}$ are $\pm2\sqrt{1\mp|u||v|}$, and the largest of these is $2\sqrt{1+|u||v|}\le2\sqrt{2}$ because $|u||v|=|\sin\theta_{aa'}||\sin\theta_{bb'}|\le1$. Hence $|\mathrm{Tr}(P_\epsilon\circ\tilde{\mathcal{S}})|\le2\sqrt{2}$ for every Bell state, and — the operator-norm argument being state-independent — for every state of the two-qubit algebra, pure or mixed. Tsirelson's bound is recovered.

It is at this point that the gap flagged in the introduction becomes concrete. The bound above is a statement about **eigenvalues of the matrix image**, i.e. about the spectral norm of $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$. The framework's own positive-definite norm — the Euclidean form $\mathrm{Sc}(x x^{*})$ of the companion articles, which corresponds to the Frobenius norm of the matrix image — is not strong enough to give it. Indeed, taking the trace of the boxed identity,

$$
\mathrm{Tr}\bigl(\tilde{\mathcal{S}}^2\bigr) = 4\,\mathrm{Tr}(e_t\otimes e_t) + 4\,\mathrm{Tr}\bigl((\vec u_1\times\vec u_1')\otimes(\vec u_2\times\vec u_2')\bigr) = 16 + 0 = 16,
$$

because the cross-product factor is traceless in each tensor factor. The Frobenius norm of $\tilde{\mathcal{S}}$ is accordingly $4$ for every configuration, and the Cauchy–Schwarz bound on the Born pairing with a state of unit Frobenius norm is $|S|\le4$ — the trivial no-signaling bound, not $2\sqrt{2}$. The Euclidean form does not distinguish the singlet's alignment of the four settings from a generic one. The sharp bound requires the spectral norm, and that norm is carried by the matrix representation, not by the algebra's own quadratic form. We leave this as a labelled gap rather than presenting the algebra as if it contained the bound on its own.

## The Three Bounds

The CHSH combination is confined by three different values, and the gap between the first two is the content of Bell's theorem.

| Bound | Value of $|S|$ | Assumption |
|---|---|---|
| Classical (CHSH) | $2$ | pre-existing local outcomes, shared $\lambda$ |
| Quantum (Tsirelson) | $2\sqrt{2}$ | states in $\mathbb{M}_+\otimes\mathbb{M}_+$, observables with spectrum $\{\pm1\}$ |
| No-signaling (algebraic) | $4$ | each $E\in[-1,1]$, marginals well defined |

The classical value is attained by deterministic local models (Step 2). The quantum value is attained by every Bell state (Step 4), and cannot be exceeded by any quantum state (Step 5). The no-signaling value $4$ is attained by the Popescu–Rohrlich box, the hypothetical device whose correlators, in the sign convention used here, are

$$
E(\vec u_1,\vec u_2)=+1,\quad E(\vec u_1,\vec u_2')=-1,\quad E(\vec u_1',\vec u_2)=+1,\quad E(\vec u_1',\vec u_2')=+1,
$$

so that $S=1-(-1)+1+1=4$; its single-party outcomes are unbiased, so it cannot transmit a signal. Quantum physics permits $2\sqrt{2}$ and forbids $4$; the framework reproduces the quantum value and, like standard quantum physics, does not explain why the world realizes $2\sqrt{2}$ rather than the algebraic maximum.

## What the Biquaternion Solution Illustrates

**1. The CHSH combination is one element of the algebra.** In the standard formulation the Bell operator is a sum of four tensor products of Pauli observables. In the framework it is the single Hermitian element $\tilde{\mathcal{S}}\in\mathbb{M}_+\otimes\mathbb{M}_+$, and the CHSH quantity is its Born pairing with the state. The inequality is a statement about the spectrum of one algebraic element.

**2. Its square is the identity plus one cross term.** The identity $\tilde{\mathcal{S}}^2=4\bigl(e_t\otimes e_t+(\vec u_1\times\vec u_1')\otimes(\vec u_2\times\vec u_2')\bigr)$ is the biquaternion content of Tsirelson's bound. The cross products are the only place the two parties' settings meet, and it is their bounded length, $|\vec u_1\times\vec u_1'|\le1$ and $|\vec u_2\times\vec u_2'|\le1$, that caps the violation.

**3. The four Bell states are a single local-unitary orbit, and they all saturate the bound.** The orbit statement is a result of the Bell-basis parent article; the invariance of the CHSH maximum under local unitaries transfers the singlet's value $2\sqrt{2}$ to its three companions. The explicit non-singlet configurations of Step 4 use the measurement plane spanned by the two equal-sign entries of $\epsilon$.

**4. The Born rule applied twice gives the joint statistics.** The joint probabilities $p(\pm,\pm\mid\vec u_1,\vec u_2)$ are trace pairings with products of two idempotents, and the correlator is their signed sum. This is the pattern the companion article on the quantum–classical divide cites.

**5. The framework reproduces, and does not explain, the bound.** The derivation is the standard operator-norm argument in a different notation. The framework supplies a clean home for the statement — the square of one element of $\mathbb{M}_+\otimes\mathbb{M}_+$ — but not a new reason for the value. Where the framework's own norm is used, it yields only the trivial bound $4$; the sharp value comes from the spectral norm of the matrix representation.

## Further Problems

**Problem 1 (Werner states and the threshold for violation).** Consider the two-qubit Werner state

$$
\tilde{Ϛ}_p = p\,P_{\mathrm{singlet}} + (1-p)\,\tfrac14\,e_t\otimes e_t,
\qquad 0\le p\le1 .
$$

Compute its correlation matrix and show that the maximal CHSH value is $2\sqrt{2}\,p$. Deduce that the state violates the CHSH inequality exactly when $p>1/\sqrt{2}$. Verify also that the maximally mixed state ($p=0$) has $T=0$ and gives $S=0$, well within the classical bound.

**Problem 2 (The algebraic maximum and the Popescu–Rohrlich box).** Write down the four correlators of the Popescu–Rohrlich box and verify that they give $|S|=4$ while all four single-party marginals are unbiased. Explain, using the eigenvalue computation of Step 5, why no choice of $\pm1$ observables on $\mathbb{C}^2\otimes\mathbb{C}^2$ can realize those four correlators: what constraint on $|u|$ and $|v|$ does the derivation impose?

**Problem 3 (Product states do not violate).** For the product state $\tilde\Pi(\vec u_4)\otimes \tilde\Pi(\vec u_3)$ of two qubits, compute $E(\vec u_1,\vec u_2)$ and show that $|S|\le2$ for all directions, with the classical value $2$ attainable. Where in the biquaternion computation does the factorization of the state enter?

**Problem 4 (Verification of the square identity on the optimal configuration).** Evaluate $\tilde{\mathcal{S}}^2$ of Step 3 at $\vec u_1\perp\vec u_1'$, $\vec u_2\perp\vec u_2'$, and verify directly that its image has eigenvalue $8$ — so that $\tilde{\mathcal{S}}$ has eigenvalue $2\sqrt{2}$ — and that the singlet idempotent is a corresponding eigen-idempotent. This is the algebraic form of the statement that the bound is saturated.

**Problem 5 (The correlation matrix and the stabilisers).** Using $T_{jj}=-\epsilon_j$ and the stabiliser operators $S_j=-e_j\otimes e_j$ of the Bell-basis parent article, express the CHSH combination for a Bell state in terms of the stabiliser eigenvalues. Confirm that the optimal directions for each state are those that weight the two equal-sign eigenvalues equally.

**Problem 6 (Open: a framework-internal reason for $2\sqrt{2}$).** The derivation above obtains the bound from the spectral norm of the matrix image of $\tilde{\mathcal{S}}$. Is there a principle internal to the biquaternion algebra — a condition on elements of $\mathbb{M}_+\otimes\mathbb{M}_+$ stated without passing to $M_4(\mathbb{C})$ — from which $2\sqrt{2}$, and not $4$, follows? The framework's own quadratic form does not do it (Step 4). This is left open; it is the framework's version of the standard question of why nature does not permit the no-signaling maximum.

## Summary

The CHSH inequality is the two-settings-per-party form of Bell's theorem, and this exercise derived its classical bound, its quantum bound, and the quantum correlators that produce it.

In the **standard formulation**, the CHSH combination is the expectation of the Bell operator $S=A\otimes B-A\otimes B'+A'\otimes B+A'\otimes B'$. Every local hidden-variable model gives $|S|\le2$, because for each value of the shared variable one of the combinations $B-B'$, $B+B'$ vanishes. The Bell-state correlators $E(\vec u_1,\vec u_2)=-\sum_j\epsilon_j a_jb_j$ give $S_{\Psi^-}=-\vec u_1\cdot(\vec u_2-\vec u_2')-\vec u_1'\cdot(\vec u_2+\vec u_2')$ for the singlet, whose maximum over directions is $|\vec u_2-\vec u_2'|+|\vec u_2+\vec u_2'|=\sqrt2(\sqrt{1-c}+\sqrt{1+c})\le2\sqrt2$. The exact operator identity $S^2=4I+[A,A']\otimes[B,B']$, evaluated with $[A,A']=2i(u\cdot\boldsymbol{\sigma})$, $[B,B']=2i(v\cdot\boldsymbol{\sigma})$, gives eigenvalues bounded by $2\sqrt2$ for every state. This is Tsirelson's bound, and it is saturated by all four Bell states at $\vec u_1\perp\vec u_1'$, $\vec u_2\perp\vec u_2'$.

In the **biquaternion formulation**, the CHSH combination is the Born pairing of the state with the single Hermitian element

$$
\tilde{\mathcal{S}}
= (i\vec u_1)\otimes(i\vec u_2) - (i\vec u_1)\otimes(i\vec u_2')
+ (i\vec u_1')\otimes(i\vec u_2) + (i\vec u_1')\otimes(i\vec u_2'),
$$

and the parent correlation function gives the same $S_\epsilon$ as the standard formulation. The Bell-operator identity becomes the algebra identity

$$
\tilde{\mathcal{S}}^2 = 4\Bigl(e_t\otimes e_t + (\vec u_1\times\vec u_1')\otimes(\vec u_2\times\vec u_2')\Bigr),
$$

whose image has eigenvalues $4(1\mp|u||v|)$; the bound $|u||v|\le1$ gives Tsirelson's value $2\sqrt2$. The CHSH quantity is thus a statement about the square of one element of $\mathbb{M}_+\otimes\mathbb{M}_+$, and the four Bell states, being a single local-unitary orbit, all attain the bound.

Two limitations are recorded rather than smoothed over. First, the framework reproduces Tsirelson's bound without explaining why the physical value is $2\sqrt2$ and not the no-signaling maximum $4$. Second, the sharp bound is obtained by the spectral norm of the matrix representation $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$; the framework's own Euclidean form gives only $|S|\le4$, as $\mathrm{Tr}(\tilde{\mathcal{S}}^2)=16$ shows. The framework contains the algebra whose representation carries Tsirelson's bound; it does not contain that bound as a property of its quadratic form alone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$ | Two-qubit tensor-product algebra |
| $\mathbb{M}_+$ | Hermitian subspace (states, observables) |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $e_k^2=-e_t$, cyclic products |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathrm{Tr}_\mathbb{B}(\tilde H)=2\,\mathrm{Sc}(\tilde H)$ | Trace on a single factor |
| $\mathrm{Tr}(x\otimes y)=\mathrm{Tr}_\mathbb{B}(x)\mathrm{Tr}_\mathbb{B}(y)$ | Trace on the tensor product |
| $e_t\mapsto I_2,\ e_k\mapsto-i\sigma_k$ | Isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$; image of $ie_k$ is $\sigma_k$ |
| $\vec u_1,\vec u_1',\vec u_2,\vec u_2'$ | Alice's and Bob's measurement directions |
| $A=\vec u_1\cdot\boldsymbol{\sigma},\ A'=\vec u_1'\cdot\boldsymbol{\sigma},\ B=\vec u_2\cdot\boldsymbol{\sigma},\ B'=\vec u_2'\cdot\boldsymbol{\sigma}$ | Single-qubit observables, spectrum $\{\pm1\}$ |
| $P_\epsilon=\tfrac14(e_t\otimes e_t+\sum_j\epsilon_j\,e_j\otimes e_j)$ | Bell idempotent, $\epsilon_1\epsilon_2\epsilon_3=+1$ |
| $E(\vec u_1,\vec u_2)=\mathrm{Tr}(P_\epsilon\circ((i\vec u_1)\otimes(i\vec u_2)))=-\sum_j\epsilon_j a_jb_j$ | Correlation function |
| $T_{jk}=\langle\sigma_j\otimes\sigma_k\rangle=-\epsilon_j\delta_{jk}$ | Correlation matrix of a Bell state |
| $S=E(\vec u_1,\vec u_2)-E(\vec u_1,\vec u_2')+E(\vec u_1',\vec u_2)+E(\vec u_1',\vec u_2')$ | CHSH combination |
| $S=A\otimes B-A\otimes B'+A'\otimes B+A'\otimes B'$ | Bell operator |
| $S^2=4I+[A,A']\otimes[B,B']=4I-4(u\cdot\boldsymbol{\sigma})\otimes(v\cdot\boldsymbol{\sigma})$ | Operator identity behind the bound |
| $\tilde{\mathcal{S}}$ | CHSH element of $\mathbb{M}_+\otimes\mathbb{M}_+$ |
| $\tilde{\mathcal{S}}^2=4(e_t\otimes e_t+(\vec u_1\times\vec u_1')\otimes(\vec u_2\times\vec u_2'))$ | Biquaternion square identity |
| $u=\vec u_1\times\vec u_1',\ v=\vec u_2\times\vec u_2'$ | Cross products controlling the bound |
| $\lvert S\rvert\le2$ | Classical (CHSH) bound |
| $\lvert S\rvert\le2\sqrt{2}$ | Tsirelson's bound |
| $\lvert S\rvert\le4$ | No-signaling (algebraic) bound |

## Further Reading

- J. S. Bell, "On the Einstein–Podolsky–Rosen paradox," *Physics* **1** (1964) 195–200, for Bell's theorem.
- J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, "Proposed experiment to test local hidden-variable theories," *Physical Review Letters* **23** (1969) 880–884, for the CHSH inequality.
- B. S. Cirel'son (Tsirelson), "Quantum generalizations of Bell's inequality," *Letters in Mathematical Physics* **4** (1980) 93–100, for the bound $2\sqrt{2}$.
- A. Peres, *Quantum Theory: Concepts and Methods* (Kluwer, 1995), for the operator-norm derivation of the quantum bound.
- S. Popescu and D. Rohrlich, "Quantum nonlocality as an axiom," *Foundations of Physics* **24** (1994) 379–385, for the no-signaling maximum $4$.
- Michael A. Nielsen and Isaac L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2000), for the CHSH inequality and Tsirelson's bound in the standard formalism.
- The companion articles of this series: *Introduction to the Biquaternion Universe*, *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, *Entangled Subsystems in the Biquaternion Framework*, *The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$*, *Exercise: The Correlation Function of the Bell States*, and *The Quantum–Classical Divide in the Biquaternion Framework*.
