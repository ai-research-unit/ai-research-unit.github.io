# __The Dirac Algebra and Biquaternions — A Dictionary__

## Introduction

This article is a dictionary. It translates between two notations for the same algebra: the **Dirac gamma-matrix algebra** of relativistic quantum mechanics, and the **biquaternion algebra** $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ of the companion articles. Its purpose is reference: given a gamma-matrix expression, to find the biquaternion that corresponds to it, and given a biquaternion relation, to find its gamma-matrix form.

The two notations describe the same mathematical object in different coordinates. The gamma matrices generate the real Clifford algebra the corpus calls $\mathrm{Cl}_{1,3}$; the biquaternions form its **even subalgebra**,

$$
\mathbb{B} \;\cong\; \mathrm{Cl}_{1,3}^{+}(\mathbb{R}),
$$

and the dictionary is the explicit isomorphism. Because a Clifford algebra is non-commutative in exactly the way the quaternions are — the product of two generators is antisymmetric — the correspondence is not a loose analogy but a change of notation, and the whole difficulty of the dictionary lies in its **signs**. This article fixes one convention, states it once, and holds it; and every entry in its tables is verified by explicit multiplication in a concrete $4\times 4$ representation.

The relation between the two algebras is not an equality of the full algebras. The Clifford algebra $\mathrm{Cl}_{1,3}$ has real dimension $16$, while the biquaternion algebra has real dimension $8$; $\mathbb{B}$ is the even part of $\mathrm{Cl}_{1,3}$, spanned by the identity, the six bivectors $\gamma^\mu\gamma^\nu$, and the pseudoscalar. The odd part — the vectors $\gamma^\mu$ and the trivectors — is not contained in $\mathbb{B}$. It is reached from the even part by multiplication by a fixed odd element, and the article gives that correspondence too, in the form of the odd generators written as $2\times 2$ matrices over $\mathbb{B}$.

The notation is inherited unchanged from the read list: the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_1e_2 = e_3$, the scalar imaginary $i$, the complex subspace $\mathbb{C}_{\mathbb{B}}$, the real-quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the two four-dimensional real subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$, the biquaternionic gradient $\tilde{\nabla}$, and the trace formula $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$. Nothing here renames or rederives them.

The article is organized as follows. The conventions — signature, metric, and the explicit representation of the gamma matrices — are fixed first, together with the distinction between the two real Clifford algebras of opposite metric sign. The isomorphism is then stated and verified. The dictionary of basis elements, of products, and of the four real subspaces follows. Separate sections treat the odd part, the chirality operator and its projectors, the norm form and conjugation, and the operator correspondence. Every table is accompanied by the check that establishes it.

## Conventions: Signature, Metric, and the Two Real Clifford Algebras

### The biquaternion side

The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$. Its $\mathbb{C}$-basis is $e_0 = 1, e_1, e_2, e_3$, with

$$
e_1^2 = e_2^2 = e_3^2 = -e_0, \qquad e_1e_2 = e_3, \qquad e_2e_3 = e_1, \qquad e_3e_1 = e_2,
$$

and $e_je_k = -e_ke_j$ for $j \neq k$. The scalar imaginary $i$ satisfies $i^2 = -1$ and commutes with every $e_\mu$. The conjugations are the ones defined in *Biquaternion Algebra*: quaternion conjugation $\bar{\cdot}$ ($e_0 \mapsto e_0$, $e_k \mapsto -e_k$), complex conjugation ${}^*$ ($i \mapsto -i$), Hermitian conjugation $\dagger = \bar{\cdot}^{\,*}$, and the anti-Hermitian conjugation $\flat = -\dagger$. Multiplication is the complex-linear extension of the quaternion product, with the scalar–vector form

$$
\tilde{Q}\circ\tilde{R} = Q_0R_0 - (\mathbf{Q},\mathbf{R}) + Q_0\mathbf{R} + R_0\mathbf{Q} + [\mathbf{Q},\mathbf{R}].
$$

### The gamma side

The gamma matrices are four $4\times 4$ complex matrices $\gamma^0, \gamma^1, \gamma^2, \gamma^3$ satisfying

$$
\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2g^{\mu\nu}I_4, \qquad g = \mathrm{diag}(+1,-1,-1,-1).
$$

The index $0$ is the timelike direction of the $ict$ gradient; with the mostly-minus generators it is the three spacelike indices $k = 1,2,3$ that carry the negative Clifford square. Thus

$$
(\gamma^0)^2 = +I_4, \qquad (\gamma^k)^2 = -I_4, \qquad k = 1,2,3.
$$

This is the standard **mostly-minus** convention, and it is the one the corpus uses throughout: the generators are the usual ones, the name is correct in the standard counting, and the square of a Clifford vector agrees with the biquaternion norm of the biquaternion the vector represents instead of differing by a sign. The $\mathbb{M}_-$ interval is a *separate* object — it belongs to the $ict$ gradient and not to the generators — and reads $ds^2 = -c^2\,dt^2 + d\mathbf{x}^2$, i.e.

$$
N(d\tilde{X}) = d\tilde{X}\circ\overline{d\tilde{X}} = (ic\,dt)^2 + d\mathbf{x}^2 = -c^2\,dt^2 + d\mathbf{x}^2 ,
$$

with the minus arising from $i^2 = -1$ and not from the generators' metric. The $ict$ metric is $\eta = \mathrm{diag}(-1,+1,+1,+1) = -g$, and it is the level-2 object of the companion *Conventions in the Biquaternion Universe*; $g$ is the level-3 metric of the generators.

The four generators, with the metric above, span a real Clifford algebra of dimension $16$, denoted $\mathrm{Cl}_{1,3}(\mathbb{R})$. In the standard mathematical convention $\mathrm{Cl}_{p,q}$ carries $p$ generators squaring to $+1$ and $q$ squaring to $-1$, so the label $(1,3)$ records one generator squaring to $+1$ and three to $-1$; the name is the standard one, $\mathrm{Cl}_{1,3} \cong M_2(\mathbb{H})$, and no relabelling warning is needed.

**A convention note, checked against the parent article.** The parent *The Dirac Equation in Biquaternionic Form* declares the Clifford metric as $g^{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$, so $(\gamma^0)^2 = +I_4$ and $(\gamma^k)^2 = -I_4$; its **explicit** matrices, the Dirac representation $\gamma^0 = \mathrm{diag}(I_2,-I_2)$, $\gamma^k = \bigl(\begin{smallmatrix}0 & \sigma^k\\ -\sigma^k & 0\end{smallmatrix}\bigr)$ and the block construction $\gamma^0 = \bigl(\begin{smallmatrix}0 & e_0\\ e_0 & 0\end{smallmatrix}\bigr)$, $\gamma^k = \bigl(\begin{smallmatrix}0 & ie_k\\ -ie_k & 0\end{smallmatrix}\bigr)$, satisfy exactly that anticommutation, and the explicit matrices used in this article, displayed below, are identical to the parent's block construction. The $ict$ metric $\eta = \mathrm{diag}(-1,+1,+1,+1) = -g$ belongs to the gradient and not to the generators; the even subalgebra is the same for either sign of $g$ (verified below), so no dictionary entry depends on which sign is chosen.

### The two real Clifford algebras and their matrix algebras

The two signs of the metric are not equivalent as real algebras, and this is a structural fact the dictionary records even though only one of them is now in use. The algebra of the mostly-minus generators — one generator squaring to $+1$ and three to $-1$, which is this article's $\mathrm{Cl}_{1,3}$ and the convention of the corpus — is isomorphic to the quaternion matrix algebra

$$
\mathrm{Cl}_{1,3} \;\cong\; M_2(\mathbb{H}) \;=\; \mathbb{H}\otimes_\mathbb{R} M_2(\mathbb{R}),
$$

while the opposite-sign algebra $\mathrm{Cl}_{3,1}$ — three generators squaring to $+1$ and one to $-1$ — is isomorphic to the real matrix algebra

$$
\mathrm{Cl}_{3,1} \;\cong\; M_4(\mathbb{R}).
$$

The two are distinct over $\mathbb{R}$ but become isomorphic after complexification, since $M_2(\mathbb{H})\otimes_\mathbb{R}\mathbb{C} \cong M_4(\mathbb{R})\otimes_\mathbb{R}\mathbb{C} \cong M_4(\mathbb{C})$. Both statements were confirmed here by exhibiting explicit representations: a quaternionic $2\times 2$ representation of the metric $\mathrm{diag}(+1,-1,-1,-1)$, whose $16$ basis products lie in $M_2(\mathbb{H})$ and have real span of dimension $16$, therefore filling $M_2(\mathbb{H})$; and a real $4\times 4$ representation of the metric $\mathrm{diag}(-1,+1,+1,+1)$, whose $16$ basis products have real span of dimension $16$ and therefore fill $M_4(\mathbb{R})$.

The even subalgebras are the same in both signatures, and this is why one dictionary serves either sign:

$$
\mathrm{Cl}_{1,3}^{+} \;\cong\; \mathrm{Cl}_{3,1}^{+} \;\cong\; M_2(\mathbb{C}) \;\cong\; \mathbb{H}\otimes_\mathbb{R}\mathbb{C} \;=\; \mathbb{B}.
$$

Passing from one sign to the other by $\gamma^\mu \mapsto i\gamma^\mu$ multiplies every even generator (a product of two or four generators) by $i^2 = -1$ or $i^4 = +1$; the real span of the even basis is unchanged, as checked explicitly. So the biquaternion algebra is the even part of **either** real Clifford algebra, and the dictionary of even elements — the tables above — is the same in either sign. What changes between the signs is the interpretation of the odd part: which of the two real forms the generators generate, and the reality properties of $\gamma_5$ and of the spinor representation. The biquaternion side of the dictionary is unaffected.

### The explicit representation used for verification

Every check below is carried out in the following $4\times 4$ representation, displayed as a $2\times 2$ matrix whose entries lie in $\mathbb{B} \cong M_2(\mathbb{C})$:

$$
\gamma^0 = \begin{pmatrix} 0 & e_0 \\ e_0 & 0 \end{pmatrix}, \qquad
\gamma^k = \begin{pmatrix} 0 & i\,e_k \\ -i\,e_k & 0 \end{pmatrix}, \qquad k = 1,2,3 .
$$

Writing the quaternion units as $e_k = -i\sigma_k$, so that $ie_k = \sigma_k$, this is the block form

$$
\gamma^0 = \begin{pmatrix} 0 & I_2 \\ I_2 & 0 \end{pmatrix}, \qquad
\gamma^k = \begin{pmatrix} 0 & \sigma_k \\ -\sigma_k & 0 \end{pmatrix},
$$

which is the usual **mostly-minus** block representation, the one used in the parent article, whose block construction is $\gamma^0 = \bigl(\begin{smallmatrix}0 & e_0\\ e_0 & 0\end{smallmatrix}\bigr)$, $\gamma^k = \bigl(\begin{smallmatrix}0 & ie_k\\ -ie_k & 0\end{smallmatrix}\bigr)$, identical to the form used here.

Direct multiplication in this representation gives $(\gamma^0)^2 = +I_4$, $(\gamma^k)^2 = -I_4$, and $\gamma^\mu\gamma^\nu = -\gamma^\nu\gamma^\mu$ for $\mu \neq \nu$, that is, $\{\gamma^\mu,\gamma^\nu\} = 2g^{\mu\nu}I_4$ with $g = \mathrm{diag}(+1,-1,-1,-1)$. The pseudoscalar is

$$
\omega = \gamma^0\gamma^1\gamma^2\gamma^3 = \mathrm{diag}(i,i,-i,-i),
$$

with $\omega^2 = -I_4$, and it commutes with every even element and anticommutes with every generator:

$$
\omega\gamma^\mu = -\gamma^\mu\omega, \qquad \omega\Phi(\tilde{Q}) = \Phi(\tilde{Q})\omega \quad (\tilde{Q} \in \mathbb{B}).
$$

## The Isomorphism: $\mathbb{B}$ is the Even Subalgebra

### The map

The biquaternion algebra is identified with the even subalgebra of $\mathrm{Cl}_{1,3}$ — the algebra of the metric $g = \mathrm{diag}(+1,-1,-1,-1)$ — by the $\mathbb{R}$-linear map $\Phi$ defined on the quaternion basis by

$$
\Phi(e_0) = I_4, \qquad
\Phi(e_1) = \gamma^2\gamma^3, \qquad
\Phi(e_2) = \gamma^3\gamma^1, \qquad
\Phi(e_3) = \gamma^1\gamma^2,
$$

and on the scalar imaginary by

$$
\Phi(i) = -\omega = -\gamma^0\gamma^1\gamma^2\gamma^3 .
$$

The sign of $\Phi(i)$ is the one free choice in the correspondence — the scalar imaginary corresponds to the pseudoscalar up to a sign — and it is fixed here so that the three imaginary quaternion units come out as the three timelike bivectors with **positive** signs, $\Phi(ie_k) = \gamma^0\gamma^k$. This is the clean form the mostly-minus convention allows: the three spacelike bivectors take the positive orientation and the three timelike bivectors take the positive sign, with the single minus absorbed into $\Phi(i)$.

Since $\Phi$ is $\mathbb{R}$-linear and $i$ commutes with the $e_\mu$, this determines $\Phi$ on all of $\mathbb{B}$: writing $\tilde{Q} = \sum_\mu (q_\mu + i q'_\mu)e_\mu$ with $q_\mu, q'_\mu \in \mathbb{R}$,

$$
\Phi(\tilde{Q}) = \sum_{\mu=0}^{3} q_\mu\,\Phi(e_\mu) + \sum_{\mu=0}^{3} q'_\mu\,\Phi(i)\Phi(e_\mu) = \sum_{\mu=0}^{3} q_\mu\,\Phi(e_\mu) - \sum_{\mu=0}^{3} q'_\mu\,\omega\,\Phi(e_\mu).
$$

### Why it is an isomorphism

Three things must be checked, and all three are verified by explicit multiplication in the representation fixed above.

*The images satisfy the quaternion relations.* The three spacelike bivectors square to $-I_4$ and anticommute among themselves, and they multiply cyclically:

$$
(\gamma^2\gamma^3)^2 = (\gamma^3\gamma^1)^2 = (\gamma^1\gamma^2)^2 = -I_4, \qquad
(\gamma^2\gamma^3)(\gamma^3\gamma^1) = \gamma^1\gamma^2 .
$$

The last identity reproduces $e_1e_2 = e_3$ exactly, since $\Phi(e_3) = \gamma^1\gamma^2$. Moreover $\omega^2 = -I_4$ and $\omega$ commutes with each spacelike bivector, so $\Phi(i) = -\omega$ behaves as central $i$:

$$
\Phi(i)^2 = -I_4, \qquad \Phi(i)\Phi(e_k) = \Phi(e_k)\Phi(i).
$$

*The map is multiplicative.* Computing all $8\times 8$ products of the real basis $\{e_0,e_1,e_2,e_3, ie_0, ie_1, ie_2, ie_3\}$ confirms

$$
\Phi(\tilde{P}\tilde{Q}) = \Phi(\tilde{P})\,\Phi(\tilde{Q})
$$

for every basis pair. The check is exhaustive on the basis, hence holds on all of $\mathbb{B}$.

*The map is injective, and its image is exactly the even part.* The eight matrices $\Phi(e_0),\dots,\Phi(ie_3)$ are linearly independent over $\mathbb{R}$ — the real span of the eight images has dimension $8$ — and each is a product of an even number of generators, hence lies in the even subalgebra $\mathrm{Cl}_{1,3}^+$. The even subalgebra also has real dimension $8$, so the image is all of it and $\Phi$ is a bijection.

This establishes

$$
\mathbb{B} \;\cong\; \mathrm{Cl}_{1,3}^{+}(\mathbb{R}), \qquad \dim_\mathbb{R}\mathbb{B} = 8 = \tfrac{1}{2}\dim_\mathbb{R}\mathrm{Cl}_{1,3} .
$$

The isomorphism is not unique: any assignment that preserves the relations differs from this one by an automorphism of $\mathbb{B}$, and the different choices are related by rotations of the spatial frame. The choice above is the corpus's, and it fixes the sign pattern derived below.

## The Dictionary of Basis Elements

### Biquaternions in gamma-matrix form

The first table is the dictionary in the direction biquaternion $\to$ Clifford. It is the image of the real basis of $\mathbb{B}$ under $\Phi$. All eight entries were computed by multiplying the representation matrices fixed above; the two nontrivial ones are the pseudoscalar column and the imaginary-quaternion rows.

| Biquaternion | Clifford element | Value in the representation |
|---|---|---|
| $e_0$ | $I_4$ | identity |
| $e_1$ | $\gamma^2\gamma^3$ | spacelike bivector |
| $e_2$ | $\gamma^3\gamma^1$ | spacelike bivector |
| $e_3$ | $\gamma^1\gamma^2$ | spacelike bivector |
| $i$ | $-\omega = -\gamma^0\gamma^1\gamma^2\gamma^3$ | $\mathrm{diag}(-i,-i,i,i)$ |
| $i\,e_1$ | $-\omega\,(\gamma^2\gamma^3) = +\gamma^0\gamma^1$ | timelike bivector |
| $i\,e_2$ | $-\omega\,(\gamma^3\gamma^1) = +\gamma^0\gamma^2$ | timelike bivector |
| $i\,e_3$ | $-\omega\,(\gamma^1\gamma^2) = +\gamma^0\gamma^3$ | timelike bivector |

The three quaternion units become the three **spacelike** bivectors, the scalar imaginary becomes **minus the pseudoscalar**, and the three imaginary quaternion units become the three **timelike** bivectors — all with positive signs. With the mostly-minus generators no mixed sign pattern arises: the single minus sits on $\Phi(i)$, which is the freedom the correspondence already carries. The map on the quaternion units reproduces $e_1e_2 = e_3$ exactly, since $(\gamma^2\gamma^3)(\gamma^3\gamma^1) = \gamma^1\gamma^2$.

### Clifford bivectors in biquaternion form

Inverting the table gives the direction Clifford $\to$ biquaternion. This is the form in which the dictionary is most often consulted, because the Lorentz generators and the gamma-matrix bilinears are bivectors.

| Clifford element | Biquaternion |
|---|---|
| $\gamma^2\gamma^3$ | $+e_1$ |
| $\gamma^3\gamma^1$ | $+e_2$ |
| $\gamma^1\gamma^2$ | $+e_3$ |
| $\gamma^3\gamma^2$ | $-e_1$ |
| $\gamma^1\gamma^3$ | $-e_2$ |
| $\gamma^2\gamma^1$ | $-e_3$ |
| $\gamma^0\gamma^1$ | $+i\,e_1$ |
| $\gamma^0\gamma^2$ | $+i\,e_2$ |
| $\gamma^0\gamma^3$ | $+i\,e_3$ |
| $\omega = \gamma^0\gamma^1\gamma^2\gamma^3$ | $-i$ |
| $I_4$ | $e_0$ |

### The sign pattern

The six bivectors split into the three spacelike ones, $\gamma^1\gamma^2, \gamma^1\gamma^3, \gamma^2\gamma^3$, which correspond to the quaternion units $e_k$, and the three timelike ones, $\gamma^0\gamma^1, \gamma^0\gamma^2, \gamma^0\gamma^3$, which correspond to $i e_k$. With the mostly-minus generators **both groups carry positive signs**:

$$
\Phi(e_1) = \gamma^2\gamma^3, \quad \Phi(e_2) = \gamma^3\gamma^1, \quad \Phi(e_3) = \gamma^1\gamma^2, \qquad
\Phi(ie_1) = \gamma^0\gamma^1, \quad \Phi(ie_2) = \gamma^0\gamma^2, \quad \Phi(ie_3) = \gamma^0\gamma^3 .
$$

The only sign in the dictionary is the minus on $\Phi(i) = -\omega$, and it is the single sign the correspondence leaves free. The reason the mixed pattern of the opposite-generator convention does not arise is visible in the products:

$$
(\gamma^2\gamma^3)(\gamma^3\gamma^1) = +\gamma^1\gamma^2, \qquad
(\gamma^3\gamma^1)(\gamma^1\gamma^2) = +\gamma^2\gamma^3, \qquad
(\gamma^1\gamma^2)(\gamma^2\gamma^3) = +\gamma^3\gamma^1,
$$

so the three spacelike products close with positive signs and reproduce $e_1e_2 = e_3$, $e_2e_3 = e_1$, $e_3e_1 = e_2$ exactly. Under the opposite sign of the generators the middle signs become negative, one of the three spacelike bivectors must be reversed, and the timelike signs come out mixed as $(-,-,+)$. That is the pattern the corpus previously recorded, and it is retired here together with the generator convention that produced it.

## Products and Non-Commutativity

The reason the dictionary is worth writing down is that both algebras are non-commutative in the same way, so that the map $\Phi$ carries products to products. This section records the product correspondence and the checks that establish it.

### The quaternion table in gamma-matrix form

Under $\Phi$, the quaternion multiplication rules become identities among bivectors. The three cyclic products are

$$
(\gamma^2\gamma^3)(\gamma^3\gamma^1) = \gamma^1\gamma^2, \qquad
(\gamma^3\gamma^1)(\gamma^1\gamma^2) = \gamma^2\gamma^3, \qquad
(\gamma^1\gamma^2)(\gamma^2\gamma^3) = \gamma^3\gamma^1,
$$

matching $e_1e_2 = e_3$, $e_2e_3 = e_1$, $e_3e_1 = e_2$. Reversing either factor reverses the sign, matching $e_2e_1 = -e_3$ and the rest. The general rule is the usual one: the product of two distinct quaternion units is the third with the sign of the permutation $(1,2,3)$, and the product of a unit with itself is $-e_0$.

### Explicit checks on independent pairs

The claim is not verified on the case that suggested it. The following four products use four different pairs of dictionary entries, including both spacelike and timelike bivectors, and each is confirmed by direct multiplication of the representation matrices:

1. **Two spacelike bivectors.** $(\gamma^2\gamma^3)(\gamma^3\gamma^1) = \gamma^1\gamma^2$; the biquaternion side is $e_1e_2 = e_3$, and $\Phi(e_3) = \gamma^1\gamma^2$.
2. **Two timelike bivectors.** $(\gamma^0\gamma^1)(\gamma^0\gamma^2) = -(\gamma^0)^2\gamma^1\gamma^2 = -\gamma^1\gamma^2 = -e_3$; the biquaternion side is $(ie_1)(ie_2) = i^2e_1e_2 = -e_3$, and $\Phi(-e_3) = -\gamma^1\gamma^2$.
3. **One of each.** $(\gamma^0\gamma^3)(\gamma^0\gamma^1) = -(\gamma^0)^2\gamma^3\gamma^1 = -\gamma^3\gamma^1 = -e_2$; the biquaternion side is $(ie_3)(ie_1) = i^2e_3e_1 = -e_2$.
4. **Mixed, non-cyclic.** $(\gamma^1\gamma^2)(\gamma^3\gamma^1) = -\gamma^2\gamma^3 = -e_1$; the biquaternion side is $(e_3)(e_2) = e_3e_2 = -e_1$.

The exhaustive check — all $36$ products of the six bivectors, which together with the identity and the pseudoscalar generate the even algebra — agrees on every pair. That, and not the four samples, is what establishes multiplicativity on the even part.

### Lorentz generators

The commutator of two generators is $\gamma^\mu\gamma^\nu - \gamma^\nu\gamma^\mu = 2\gamma^\mu\gamma^\nu$ for $\mu \neq \nu$, so the Lorentz generators

$$
\sigma^{\mu\nu} = \tfrac{1}{4}[\gamma^\mu,\gamma^\nu] = \tfrac{1}{2}\gamma^\mu\gamma^\nu
$$

are one half of the corresponding bivectors. Reading them off the bivector table above gives the dictionary of the Lorentz algebra:

| Generator | Biquaternion | Generator | Biquaternion |
|---|---|---|---|
| $\sigma^{23}$ | $\tfrac{1}{2}e_1$ | $\sigma^{01}$ | $+\tfrac{1}{2}i\,e_1$ |
| $\sigma^{31}$ | $\tfrac{1}{2}e_2$ | $\sigma^{02}$ | $+\tfrac{1}{2}i\,e_2$ |
| $\sigma^{12}$ | $+\tfrac{1}{2}e_3$ | $\sigma^{03}$ | $+\tfrac{1}{2}i\,e_3$ |

The spacelike generators $\sigma^{jk}$ are the half-quaternion-units and the boost generators $\sigma^{0k}$ are the half-imaginary-quaternion-units, both with positive signs. The commutator $[\sigma^{\mu\nu},\sigma^{\rho\sigma}]$ on the left corresponds to the biquaternion commutator on the right, since $\Phi$ is multiplicative.

### Multiplication by the pseudoscalar

The pseudoscalar is minus the image of $i$ and is central in the even algebra, so multiplication by $\omega$ on a Clifford even element corresponds exactly to multiplication by $-i$ on the biquaternion:

$$
\omega\,\Phi(\tilde{Q}) = \Phi(-i\,\tilde{Q}), \qquad \tilde{Q} \in \mathbb{B}.
$$

This is checked on the whole real basis. On the spacelike bivectors it reads $\omega(\gamma^2\gamma^3) = -\gamma^0\gamma^1$, $\omega(\gamma^3\gamma^1) = -\gamma^0\gamma^2$, $\omega(\gamma^1\gamma^2) = -\gamma^0\gamma^3$: multiplication by the pseudoscalar exchanges the spacelike and timelike bivector subspaces, which is the algebraic content of the Hodge duality of the bivectors in four dimensions. Since the dictionary maps the spacelike group to the quaternion units and the timelike group to the imaginary quaternion units, the operation is simply "multiply by $-i$" — equivalently "multiply by $i$ and reverse orientation".

## Vectors and the Odd Part

The biquaternion algebra is the **even** subalgebra, so the generators $\gamma^\mu$ themselves are not biquaternions. They are, however, obtained from the even part by multiplication by a single fixed odd element, and this gives the dictionary of the odd part.

### The generators as matrices over $\mathbb{B}$

In the representation fixed above the odd generators are $2\times 2$ matrices with entries in $\mathbb{B}$:

$$
\gamma^0 = \begin{pmatrix} 0 & e_0 \\ e_0 & 0 \end{pmatrix}, \qquad
\gamma^k = \begin{pmatrix} 0 & i\,e_k \\ -i\,e_k & 0 \end{pmatrix}, \qquad k = 1,2,3 .
$$

The corresponding **trivectors** $\gamma^\mu\gamma^\nu\gamma^\rho$ ($\mu < \nu < \rho$) are the other odd elements (of degree three); there are four of them.

### The odd part is $\gamma^0$ times the even part

Every odd element is $\gamma^0$ times an even element. On the four-vectors this is explicit:

$$
x_0\gamma^0 + x_1\gamma^1 + x_2\gamma^2 + x_3\gamma^3
= \gamma^0\,\Phi\!\left(x_0\,e_0 + i x_1\,e_1 + i x_2\,e_2 + i x_3\,e_3\right),
$$

an identity verified by multiplying the representation matrices. The biquaternion in parentheses lies in the **Hermitian subspace** $\mathbb{M}_+$, whose basis is $\{e_0, ie_1, ie_2, ie_3\}$, and with the mostly-minus generators its coefficients are all positive: the mixed $(-,-,+)$ pattern of the opposite convention, which came from the same source as the mixed timelike-bivector signs, does not appear here. The four trivectors are likewise

$$
\gamma^\mu\gamma^\nu\gamma^\rho = \gamma^0\,\Phi(w), \qquad w \in \mathbb{M}_-,
$$

as checked on the four trivector basis elements. So the odd part of $\mathrm{Cl}_{1,3}$ decomposes as

$$
\mathrm{Cl}_{1,3}^{\mathrm{odd}} = \gamma^0\,\Phi(\mathbb{M}_+) \;\oplus\; \gamma^0\,\Phi(\mathbb{M}_-),
$$

with the vector subspace corresponding to the Hermitian subspace and the trivector subspace to the anti-Hermitian subspace. Multiplying every entry of the biquaternion table above by $\gamma^0$ therefore produces the odd dictionary; the frame $\gamma^0$ is the one arbitrary choice in it, and it is fixed once and for all by the representation.

### The metric of a vector

The square of a vector is a scalar, and its scalar part is the metric form. From $\gamma^\mu\gamma^\nu = g^{\mu\nu}I_4 + \gamma^\mu\gamma^\nu\big|_{\text{bivector}}$,

$$
(x_0\gamma^0 + \cdots + x_3\gamma^3)^2 = \bigl(+x_0^2 - x_1^2 - x_2^2 - x_3^2\bigr)I_4,
$$

verified symbolically in the representation. This is the Clifford form of the metric $g(x,x)$. The biquaternion $w$ in the frame identity has norm form $N(w) = x_0^2 - x_1^2 - x_2^2 - x_3^2$, the signature of $\mathbb{M}_+$; it **agrees** with the Clifford form term by term, so there is no relative sign between the square of an odd vector and the norm of the biquaternion that represents it. That agreement is what the mostly-minus convention buys: with the opposite sign of the generators the two forms differ by an overall minus, and the odd part of the dictionary has to record that sign separately.

## The Four Real Subspaces

The four natural real subspaces of $\mathbb{B}$ are the fixed-point sets of the conjugations, and each has a simple image under the dictionary. The identifications below were checked by confirming that each generating basis vector of the subspace lies in the stated Clifford span, and conversely.

| Subspace | Real basis | Clifford image |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ (complex scalars) | $e_0,\; ie_0$ | $I_4,\; -\omega$ |
| $\mathbb{H}_{\mathbb{B}}$ (real quaternions) | $e_0,\; e_1,\; e_2,\; e_3$ | $I_4,\; \gamma^2\gamma^3,\; \gamma^3\gamma^1,\; \gamma^1\gamma^2$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $ie_0,\; ie_1,\; ie_2,\; ie_3$ | $-\omega,\; \gamma^0\gamma^1,\; \gamma^0\gamma^2,\; \gamma^0\gamma^3$ |
| $\mathbb{M}_+$ (Hermitian) | $e_0,\; ie_1,\; ie_2,\; ie_3$ | $I_4,\; \gamma^0\gamma^1,\; \gamma^0\gamma^2,\; \gamma^0\gamma^3$ |
| $\mathbb{M}_-$ (anti-Hermitian) | $ie_0,\; e_1,\; e_2,\; e_3$ | $-\omega,\; \gamma^2\gamma^3,\; \gamma^3\gamma^1,\; \gamma^1\gamma^2$ |

The pattern is clean: the real-quaternion subspace is the identity together with the **spacelike** bivectors, its multiple by $i$ is minus the pseudoscalar together with the **timelike** bivectors, and the two Hermitian sectors are obtained by taking the scalar part from one of these and the vector part from the other. The informational subspace $\mathbb{M}_+$ is the identity plus the timelike bivectors; the material subspace $\mathbb{M}_-$ is the pseudoscalar plus the spacelike bivectors. The single minus in the table is the sign of $\Phi(i)$, and it appears exactly wherever $i$ itself appears; it is not a separate sign pattern. Multiplication by the pseudoscalar — that is, by $i$ — exchanges the two sectors, which is the Clifford form of the identity $i\mathbb{M}_+ = \mathbb{M}_-$.

Two consequences follow immediately and are worth recording. First, the timelike bivectors, which are the Lorentz boosts, carry the purely imaginary vector part of $\mathbb{M}_+$: the boost generators live in the informational sector, as stated in *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*. Second, the two sectors carry the mirror norm forms: on the basis $\{ie_0, e_1, e_2, e_3\}$ of $\mathbb{M}_-$ the form $N$ is negative in the first direction and positive in the other three, while on the basis $\{e_0, ie_1, ie_2, ie_3\}$ of $\mathbb{M}_+$ it is positive in the first direction and negative in the other three. Since quaternion conjugation fixes $i$, one has $N(i\tilde{Q}) = -N(\tilde{Q})$, so the interchange $i\mathbb{M}_+ = \mathbb{M}_-$ reverses the sign of the norm form. The two sectors are thus mirror images, and the Clifford images reflect this: the identity becomes the pseudoscalar, which has the opposite square.

## Gamma-Five and the Chirality Projectors

### The chirality operator

The chirality operator of the Dirac algebra is

$$
\gamma_5 = i_{\mathrm{Cl}}\,\omega = i_{\mathrm{Cl}}\,\gamma^0\gamma^1\gamma^2\gamma^3, \qquad \gamma_5 = \mathrm{diag}(-1,-1,1,1),
$$

where $i_{\mathrm{Cl}}$ is the scalar imaginary of the **complexified** Clifford algebra, not the biquaternion imaginary. The two are different objects: the biquaternion imaginary $i$ has image $-\omega$ under $\Phi$, so in the dictionary

$$
\gamma_5 \;=\; -i_{\mathrm{Cl}}\,\Phi(i) \;=\; \Phi_{\mathbb{C}}\!\left(-i_{\mathrm{Cl}}\, i\right),
$$

where $\Phi_{\mathbb{C}}$ is the $\mathbb{C}$-linear extension of $\Phi$ to $\mathbb{C}\otimes_\mathbb{R}\mathbb{B}$. In words: **the chirality operator is the product of the two commuting square roots of $-1$**, the external complex unit $i_{\mathrm{Cl}}$ of the complexified Clifford algebra and the biquaternion imaginary $i$ (whose Clifford image is minus the pseudoscalar). This is the precise sense in which $\gamma_5$ is *not* an element of $\mathbb{B}$: it needs both square roots, and their product is a new central element of the complexified algebra.

The defining properties are verified directly:

$$
\gamma_5^2 = I_4, \qquad \gamma_5\gamma^\mu = -\gamma^\mu\gamma_5, \qquad \gamma_5\,\Phi(\tilde{Q}) = \Phi(\tilde{Q})\,\gamma_5 \quad (\tilde{Q} \in \mathbb{B}).
$$

$\gamma_5$ anticommutes with every generator and commutes with every even element, hence with the whole biquaternion image.

### The projectors

Because $\gamma_5^2 = I_4$, the chirality projectors are

$$
P_{\pm} = \tfrac{1}{2}\bigl(I_4 \pm \gamma_5\bigr) \;=\; \Phi_{\mathbb{C}}\!\left(\tfrac{1}{2}\bigl(e_0 \mp i_{\mathrm{Cl}}\, i\bigr)\right),
$$

each of rank $2$ in the $4\times 4$ representation. Direct multiplication gives

$$
P_+^2 = P_+, \qquad P_-^2 = P_-, \qquad P_+P_- = 0, \qquad P_+ + P_- = I_4, \qquad \mathrm{Tr}\,P_\pm = 2 .
$$

In biquaternion terms these are the **central** idempotents $\tfrac{1}{2}(e_0 \pm i_{\mathrm{Cl}} i)$ of the complexified biquaternion algebra $\mathbb{C}\otimes_\mathbb{R}\mathbb{B}$. Since $(i_{\mathrm{Cl}} i)^2 = +1$ and $i$ is central, they are central, and they split

$$
\mathbb{C}\otimes_\mathbb{R}\mathbb{B} \;\cong\; M_2(\mathbb{C}) \oplus M_2(\mathbb{C}),
$$

the decomposition of the complexified even algebra into its two chiral halves.

### Two families of idempotents, not to be confused

The chirality projectors are **not** the same as the pure-state idempotents $P_\pm = \tfrac{1}{2}(e_0 \pm \mu i)$ of the informational sector, in which $\mu$ is a unit pure real quaternion and $i$ is the biquaternion imaginary. Under the dictionary, with $\mu = \mu_k e_k$ and $\Phi(\mu)$ a spacelike bivector $b$ satisfying $b^2 = -I_4$,

$$
\tfrac{1}{2}\bigl(e_0 + \mu i\bigr) \;\longmapsto\; \tfrac{1}{2}\bigl(I_4 + b\,\omega\bigr) \;=\; \tfrac{1}{2}\bigl(I_4 + \Phi(\mu)\omega\bigr),
$$

which is idempotent, because $(b\omega)^2 = b^2\omega^2 = (-1)(-1) = +1$, but is **not central**: it does not commute with the even algebra, since $b$ does not. For example, $\tfrac{1}{2}(e_0 + ie_3)$ maps to $\tfrac{1}{2}(I_4 + \gamma^0\gamma^3)$, which squares to itself and does not commute with $\Phi(e_1) = \gamma^2\gamma^3$. So the dictionary separates two idempotent families that both carry the name $P_\pm$ in the corpus:

- the **chirality projectors** $\tfrac{1}{2}(1 \pm \gamma_5) \leftrightarrow \tfrac{1}{2}(e_0 \mp i_{\mathrm{Cl}} i)$, central, two of them, splitting the complexified algebra;
- the **state projectors** $\tfrac{1}{2}(1 + b\omega) \leftrightarrow \tfrac{1}{2}(e_0 + \mu i)$, non-central, parametrized by a unit vector and the Bloch sphere.

Both are idempotent; only the first is central. The distinction is the same as the distinction between splitting the algebra into chiral halves and selecting a state within it.

## Conjugation, the Norm Form, and the Matrix Representation

### Quaternion conjugation is Clifford reversal

The Clifford algebra carries the **reversal** anti-automorphism $\mathrm{rev}$, defined on a product by reversing the order of the factors, $\mathrm{rev}(\gamma^{\mu_1}\cdots\gamma^{\mu_k}) = \gamma^{\mu_k}\cdots\gamma^{\mu_1}$. On the even basis it acts as

$$
\mathrm{rev}(I_4) = I_4, \qquad \mathrm{rev}(\omega) = \omega, \qquad \mathrm{rev}(\gamma^\mu\gamma^\nu) = \gamma^\nu\gamma^\mu = -\gamma^\mu\gamma^\nu \quad (\mu \neq \nu),
$$

the sign $+$ on the scalar and the pseudoscalar following from the even number of transpositions. Under the dictionary this is exactly quaternion conjugation:

$$
\Phi(\bar{\tilde{Q}}) = \mathrm{rev}\bigl(\Phi(\tilde{Q})\bigr),
$$

checked on the eight real basis elements, whose images under $\bar{\cdot}$ carry precisely the signs $+$ on $e_0, i$ and $-$ on $e_k, ie_k$ that reversal carries on $I_4, \omega$ and the bivectors.

### The norm form

The biquaternion norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$. Its Clifford image is the product with the reversal,

$$
\Phi(\tilde{Q})\,\mathrm{rev}\bigl(\Phi(\tilde{Q})\bigr) = \Phi\bigl(\tilde{Q}\bar{\tilde{Q}}\bigr),
$$

which is central. When the norm form is **real** — in particular on both $\mathbb{M}_-$ and $\mathbb{M}_+$ — this is a scalar matrix,

$$
\Phi(\tilde{Q})\,\mathrm{rev}\bigl(\Phi(\tilde{Q})\bigr) = N(\tilde{Q})\,I_4, \qquad \tilde{Q} \in \mathbb{M}_- \text{ or } \mathbb{M}_+,
$$

verified with general real coefficients on each sector. For the material four-vectors this is the Minkowski interval. Writing $\tilde{V} = i v_0 e_0 + v_1e_1 + v_2e_2 + v_3e_3 \in \mathbb{M}_-$,

$$
N(\tilde{V}) = \tilde{V}\bar{\tilde{V}} = -v_0^2 + v_1^2 + v_2^2 + v_3^2 = -c^2t^2 + \mathbf{x}^2,
$$

which is the invariant interval of the companion articles. So the interval is the Clifford norm form constructed with the reversal, and the minus sign in the time direction is the $ict$ metric sign $\eta^{00} = -1$ — the sign of $-g$, not of the generators' metric.

### The matrix representation and the trace

The biquaternion algebra is $M_2(\mathbb{C})$ as a real algebra, and the dictionary is consistent with that matrix representation: the even Clifford algebra is the same copy of $M_2(\mathbb{C})$, and each biquaternion has both a $2\times 2$ matrix and an even Clifford representative. The corpus's trace formula is stated in the $2\times 2$ representation and is inherited unchanged:

$$
\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H}).
$$

Two cautions about traces, since the dictionary introduces a second one. First, the trace in the corpus formula is the trace of the $2\times 2$ matrix representing the biquaternion; it is not the trace of the $4\times 4$ Clifford matrix. Second, the two are different functions: the $4\times 4$ trace of an even element is $\mathrm{Tr}\,\Phi(\tilde{Q}) = 4\,\mathrm{Re}\,\mathrm{Sc}(\tilde{Q})$ — for example $\mathrm{Tr}\,\Phi(e_0) = 4$ and $\mathrm{Tr}\,\Phi(i) = \mathrm{Tr}\,\omega = 0$ — while the $2\times 2$ trace is $\mathrm{Tr}_2(\tilde{Q}) = 2Q_0$, so that

$$
\mathrm{Tr}\,\Phi(\tilde{Q}) = 2\,\mathrm{Re}\,\mathrm{Tr}_2(\tilde{Q}).
$$

The trace formula itself is a statement internal to $\mathbb{B}$ and needs no translation.

## Two Ways the Algebra Carries Physics: Multiplication and Conjugation

The dictionary so far has mapped objects; it is worth stating the two ways an element of $\mathbb{B}$ is *used*, because they are not interchangeable, and the difference is the source of the framework's most persistent obstruction.

**One element, two readings.** Because $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H} \cong M_2(\mathbb{C})$, the algebra is the endomorphism algebra of its own unique simple module, $\mathbb{B} = \mathrm{End}(S)$ with $S$ of complex dimension two. Every element is therefore at once an **object** of the algebra and a **linear operator** on $S$. The two mechanisms are those two readings.

**Mechanism one: multiplication, on the module.** A spinor is an element of the minimal left ideal $S = \mathbb{B}p$, $p = \tfrac12(e_0+ie_3)$, and $\mathbb{B}$ acts on it by left multiplication, $\psi\mapsto \rho(\tilde B)\psi$. Since $\mathbb{B} = \mathrm{End}(S)$, *every* complex-linear operator on the spinor module is some biquaternion, and this mechanism carries the whole half-integer-spin sector: the Dirac field, its two Weyl halves, the chirality projectors (central idempotents of the complexified algebra $\mathbb{C}\otimes_\mathbb{R}\mathbb{B}$, not of $\mathbb{B}$ itself), the mass $m$ and the central phase $\lambda = e^{i\theta}$ (central elements), and the gradient $\tilde{\nabla}$ when it acts on a field.

**Mechanism two: conjugation, on the algebra.** A four-vector is not in the module but in the algebra: the material sector $\mathbb{M}_- = \mathrm{span}_\mathbb{R}\{ie_0,e_1,e_2,e_3\}$. A Lorentz transformation acts on it by the rotor conjugation

$$
\tilde X \;\mapsto\; \tilde\Lambda\,\tilde X\,\tilde\Lambda^\dagger,
\qquad \tilde\Lambda\in\mathbb{B},\quad N(\tilde\Lambda)=1,
$$

not by multiplication. This mechanism carries the integer-spin sector: the four-vector, the gauge potential, the field strength, the four-current, and the rotors themselves as points of $SL(2,\mathbb{C})$.

**Why the two cannot be merged.** The vector carrier $\mathbb{M}_-$ is only a **real** vector space: multiplication by $i$ maps it to the other sector, $i\mathbb{M}_- = \mathbb{M}_+$ (O16 of the catalogue). A $\mathbb{B}$-module, by contrast, is complex-linear, $i$ acting as its complex structure. So $\mathbb{M}_-$ is not a $\mathbb{B}$-module, and a four-vector cannot be carried by multiplication. The two mechanisms are separated by the real-versus-complex distinction, and that distinction is forced by the algebra rather than chosen.

The same fact shows up as a closure failure. Left multiplication by a general element does **not** preserve $\mathbb{M}_-$: multiplying by $e_1$ sends $ie_0$ into $\mathbb{M}_+$, sends $e_2$ into $\mathbb{M}_-$, and sends a generic element of $\mathbb{M}_-$ into neither sector, whereas the rotor conjugation always stays inside $\mathbb{M}_-$. In the explicit model $\Phi(e_0)=I$, $\Phi(e_k)=-i\sigma_k$, both statements were checked on random samples: every one of $200$ rotor conjugations of a random element of $\mathbb{M}_-$ remained anti-Hermitian, and every one of $200$ left products fell outside the sector. The vector part is closed under central scalars and under the adjoint action, and under nothing else.

| Object | Carrier | Action | Spin |
|---|---|---|---|
| Dirac field $\psi$ | module $S$ | left multiplication | $\tfrac12$ |
| Weyl halves $\psi_L,\psi_R$ | two copies of $S$ | left multiplication | $\tfrac12$ |
| chirality projectors $\tfrac12(1\pm\gamma_5)$ | central idempotents of $\mathbb{C}\otimes_\mathbb{R}\mathbb{B}$ | on the complexified module | — |
| mass $m$, phase $\lambda$ | center $\mathbb{C}_{\mathbb{B}}$ | scalar multiplication | $0$ |
| gradient $\tilde{\nabla}$ acting on a field | $\mathbb{B}$ | left multiplication | — |
| four-vector (momentum, position) | $\mathbb{M}_-\subset\mathbb{B}$ | conjugation $\tilde\Lambda\tilde X\tilde\Lambda^\dagger$ | $1$ |
| gauge potential, four-current | $\mathbb{M}_-$ | conjugation | $1$ |
| field strength, Lorentz generator | the algebra's vector part | conjugation | $1$ |

**The consequence: multiplication is chirality-blind.** The two mechanisms differ again in what they do to the two chiral components of a Dirac module. Conjugation and central multiplication are the framework's gauge and Lorentz actions, and the question that the series' electroweak articles ask — can an action distinguish the left-handed from the right-handed fermion? — is answered by the mechanism, not by the group: left multiplication acts on the two components with the **same** representation, so no multiplication can give them inequivalent ones. This is the vector-like obstruction, and it is a property of $\mathbb{B}$ rather than of any particular gauge group.

What lies outside that mechanism is precisely the operations that must treat the two chiralities *differently* or *exchange* them in a single step. They are not multiplications and have no representative in $\mathbb{B}$: the parity-reflecting frame element $\gamma^0$ and the energy-sign split built on it, the internal matrices of charge conjugation and parity, the chiral gauge coupling the electroweak article requires, and the odd form of a first-order operator — the Feynman slash. The slash is the mildest case, because $\mathbb{B}$ carries a first-order operator of its own, the even gradient $\tilde{\nabla}$, as the next section relates; the others have no such substitute. All of them are catalogued together as **O22** in the companion catalogue of obstructions, where the vector-like property is stated as the algebraic fact it is.

## The Dirac Operator and the Gradient

The biquaternionic Dirac operator — the gradient $\tilde{\nabla}$ of the companion articles, written $D$ in the quaternion-analysis articles — is

$$
\tilde{\nabla} = e_0\,\partial_{ict} + e_1\,\partial_x + e_2\,\partial_y + e_3\,\partial_z,
$$

and it is a biquaternion-valued operator, hence **even** under the dictionary. Its Clifford representative is

$$
\Phi(\tilde{\nabla}) = I_4\,\partial_{ict} + (\gamma^2\gamma^3)\,\partial_x + (\gamma^3\gamma^1)\,\partial_y + (\gamma^1\gamma^2)\,\partial_z,
$$

an even operator. It is a square root of the d'Alembertian in the reversal sense,

$$
\Phi(\tilde{\nabla})\,\mathrm{rev}\bigl(\Phi(\tilde{\nabla})\bigr) = \Box\,I_4,
$$

which is the image of $\tilde{\nabla}\bar{\tilde{\nabla}} = \Box$, since reversal corresponds to quaternion conjugation. Its symbol squares to the norm form: $\Phi(\tilde{k})\,\mathrm{rev}(\Phi(\tilde{k})) = (k_0^2 + k_1^2 + k_2^2 + k_3^2)I_4$.

The gamma-matrix Dirac operator is the **odd** element

$$
\not\partial = \gamma^\mu\partial_\mu, \qquad \not\partial^2 = \bigl(-(1/c^2)\partial_t^2 + \Delta\bigr)I_4 = \Box\,I_4,
$$

where the second identity is the ordinary Clifford relation, verified symbolically on the symbols. So the algebra contains **two** square roots of $\Box$: the odd Dirac operator $\not\partial$ and the even gradient $\Phi(\tilde{\nabla})$, which are square roots in different graded pieces, the odd one with the ordinary product and the even one with the reversal. They are not the same operator, and the dictionary does not identify them; what relates them is the frame of the previous section, through which every odd element is written as a fixed odd element times an even one. The statement in the parent article that $\tilde{\nabla}$ "plays the role of the Dirac operator" is therefore a statement about the role — both are square roots of the wave operator and both express first-order relativistic equations — and not an identification of the two operators.

## Summary

This article is a dictionary between the Dirac gamma-matrix algebra and the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$.

**The two are the same algebra up to size.** The biquaternion algebra is the even subalgebra of the real Clifford algebra of the metric $g = \mathrm{diag}(+1,-1,-1,-1)$, $\mathbb{B} \cong \mathrm{Cl}_{1,3}^{+}$, of real dimension $8$; the full algebra has dimension $16$. The isomorphism $\Phi$ is fixed by $e_1 \mapsto \gamma^2\gamma^3$, $e_2 \mapsto \gamma^3\gamma^1$, $e_3 \mapsto \gamma^1\gamma^2$, $i \mapsto -\omega = -\gamma^0\gamma^1\gamma^2\gamma^3$, and is verified by exhaustive multiplication on a basis.

**The two signs of the metric are distinct but share the even part.** The algebra of this article's metric is $\mathrm{Cl}_{1,3} \cong M_2(\mathbb{H})$ in the standard counting, while the opposite-sign algebra $\mathrm{Cl}_{3,1}$ — three generators squaring to $+1$, one to $-1$ — is $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$; the two are non-isomorphic over $\mathbb{R}$. They nevertheless share the even subalgebra, $\mathrm{Cl}_{1,3}^{+} \cong \mathrm{Cl}_{3,1}^{+} \cong M_2(\mathbb{C}) \cong \mathbb{B}$, so the dictionary of even elements is the same for either sign of $g$; the sign changes only the character of the odd part and the reality of $\gamma_5$.

**The metric convention is stated once and held.** The Clifford metric is $g = \mathrm{diag}(+1,-1,-1,-1)$ — the standard **mostly-minus** convention — so $(\gamma^0)^2 = +I_4$ and $(\gamma^k)^2 = -I_4$, and the algebra is $\mathrm{Cl}_{1,3} \cong M_2(\mathbb{H})$ in the standard counting with no relabelling needed. The $ict$ metric is the separate object $\eta = \mathrm{diag}(-1,+1,+1,+1) = -g$, and it belongs to the gradient, not to the generators. The parent article's explicit matrices already use this metric and agree with those used here; the opposite-sign matrices are $i$ times them, and the even dictionary is unaffected.

**The dictionary of even basis elements is:** $e_0 \leftrightarrow I_4$, $e_k \leftrightarrow$ spacelike bivectors, $i \leftrightarrow -\omega$, and $ie_k \leftrightarrow$ timelike bivectors, **all with positive signs**. The single minus sits on $i$ itself and is the sign the correspondence leaves free.

**Products go to products.** $\Phi(\tilde{P}\tilde{Q}) = \Phi(\tilde{P})\Phi(\tilde{Q})$; the quaternion multiplication table becomes the multiplication table of the bivectors, and the Lorentz generators $\sigma^{\mu\nu} = \tfrac{1}{2}\gamma^\mu\gamma^\nu$ are half the corresponding biquaternions, with boosts in the imaginary-quaternion directions. Multiplication by $\omega$ is multiplication by $-i$.

**The odd part is reached by a frame.** The generators and trivectors are not biquaternions; every vector is $\gamma^0\Phi(w)$ with $w \in \mathbb{M}_+$ and every trivector is $\gamma^0\Phi(w)$ with $w \in \mathbb{M}_-$.

**The four real subspaces have simple images.** $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ are the spacelike and timelike bivector groups with and without the identity and pseudoscalar; $\mathbb{M}_+$ is the identity plus the timelike bivectors; and $\mathbb{M}_-$ is the pseudoscalar plus the spacelike bivectors.

**Chirality is the product of two complex structures.** $\gamma_5 = i_{\mathrm{Cl}}\omega = -\Phi_{\mathbb{C}}(i_{\mathrm{Cl}} i)$, the sign being that of $\Phi(i)$; its projectors are the central idempotents $\tfrac{1}{2}(e_0 \mp i_{\mathrm{Cl}} i)$, distinct from the non-central state idempotents $\tfrac{1}{2}(e_0 + \mu i)$.

**Conjugation is reversal, and the norm form is the Clifford norm with reversal**, giving the Minkowski interval on $\mathbb{M}_-$ and its mirror on $\mathbb{M}_+$.

**The dictionary does not identify the Dirac operator with the gradient.** Both square to $\Box$, but one is odd and one is even; the frame relates them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_1e_2 = e_3$ |
| $i$ | Scalar imaginary, $i^2 = -1$, central |
| $g = \mathrm{diag}(+1,-1,-1,-1)$ | Clifford metric of the generators (this article) |
| $\eta = \mathrm{diag}(-1,+1,+1,+1) = -g$ | $ict$ metric, belonging to the gradient |
| $\gamma^\mu$ | Gamma matrices, $\{\gamma^\mu,\gamma^\nu\} = 2g^{\mu\nu}I_4$ |
| $\omega = \gamma^0\gamma^1\gamma^2\gamma^3$ | Pseudoscalar, $\omega^2 = -I_4$ |
| $\Phi$ | Isomorphism $\mathbb{B} \to \mathrm{Cl}_{1,3}^{+}$ |
| $\Phi_C$ | Its $\mathbb{C}$-linear extension |
| $\gamma_5 = i_{\mathrm{Cl}}\omega$ | Chirality operator |
| $P_\pm = \tfrac{1}{2}(1 \pm \gamma_5)$ | Chirality projectors |
| $\sigma^{\mu\nu} = \tfrac{1}{4}[\gamma^\mu,\gamma^\nu]$ | Lorentz generators |
| $\mathrm{rev}$ | Clifford reversal anti-automorphism |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ | Norm form |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Anti-Hermitian and Hermitian subspaces |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}$ | Real-quaternion and complex subspaces |
| $S = \mathbb{B}p$, $p=\tfrac12(e_0+ie_3)$ | The simple (spinor) module; $\mathbb{B}=\mathrm{End}(S)$ |
| $\tilde{\nabla} = e_0\partial_{ict} + \sum_k e_k\partial_k$ | Biquaternionic gradient |
| $\not\partial = \gamma^\mu\partial_\mu$ | Gamma-matrix Dirac operator |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula (unchanged) |

## Further Reading

- Companion articles: *Biquaternion Algebra* (the definition, the four conjugations, and the four real subspaces); *Biquaternion Algebraic Representations* (the $2\times 2$ matrix representation, the trace, and the Clifford-algebra isomorphism on which this dictionary is built); *Clifford Algebras* (the general definition and the fundamental relation); *Clifford Algebras in Finite Dimensions* (the classification of the low-dimensional real Clifford algebras); *Clifford Algebras and Bott Periodicity* (the periodic structure); *The Dirac Equation in Biquaternionic Form* (the gradient, the mass term, and the plane-wave solutions); *Spinors* (the spinor representation); *The Spinor Module in Biquaternionic Form and Its Lorentz Action* (the module on which the even algebra acts); *The Spinor Representation of the Lorentz Group in Biquaternionic Form* (the Lorentz generators in biquaternion form); *Chiral Fermions in the Biquaternion Framework* and *Exercise: Chirality and the Weyl Spinors* ($\gamma_5$, the chiral projectors, and the Weyl spinors); *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* and *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* (the two sectors whose Clifford images are tabulated here); *Introduction to the Biquaternion Universe* (the algebra and the two sectors).
