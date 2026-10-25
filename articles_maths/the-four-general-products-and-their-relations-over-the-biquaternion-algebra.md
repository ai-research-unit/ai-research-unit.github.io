# __The Four General Products and Their Relations over the Biquaternion Algebra__

## Introduction

The underlying complex vector space of $\mathbb{B}$ carries **four general products**, one to each choice of the two slots: the first factor is read as it stands or through the natural conjugation ${}^{\natural}$, the second as it stands or through the Hermitian conjugation ${}^{*}$, and the two choices are independent. The four are the general plain bilinear product $\tilde Q_1\tilde Q_2$, the general quaternionic bilinear product $\tilde Q_1^{\natural}\tilde Q_2$, the general plain sesquilinear product $\tilde Q_1\tilde Q_2^{*}$ and the general quaternionic sesquilinear product $\tilde Q_1^{\natural}\tilde Q_2^{*}$. No two of the four agree on every pair.

This article does three things. It defines the four on the coordinates, each with its scalar–vector form, and reads the two decisions on the pair: the block of scalar parts and the block of vector parts. Each case closes with the conjugation it inserts, its fixed subspaces and the form that follows; the fourth carries the natural conjugation as the fundamental symmetry of the Krein form. It collects the identities that link the four — how each conjugation in a slot separates a factor into scalar and vector parts, how a product conjugates, how the four scalar parts and the four vector parts are related, how the left multiplications of the four are the plain ones read through the conjugations, and how the four collapse on the real quaternion subspace. It then compares the four by their algebraic properties: the property table, bilinearity, associativity, the units, the alternative and flexible identities, the degree-three identity, the left multiplications, and the question of which of the four is a multiplication in the sense of algebra.

The four are also one rule with a conjugation inserted in each slot. The two insertions commute, the four readings form a group $\mathbb{Z}_2\times\mathbb{Z}_2$, and the reading of the group on a general algebra gives the slot family, whose second slot governs the composition and whose first slot governs the form. That construction, the group and the table of the slots are *Introduction to the Operators of the Biquaternion Algebra*, §*The Four Readings and Their Group*.

The article assumes the algebra, the element, the basis and the four conjugations from *The Biquaternion Algebra and Its Vector Spaces*. The forms and the algebraic norms are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the split of each general product into a symmetric and an antisymmetric part is *Symmetric and Antisymmetric Decomposition of the Four General Products*; the restrictions to the remarkable subspaces are *Remarkable Subspaces and the Four General Products, Forms and Norms*.

## The Four General Products

Each rule is written on the coordinates of a pair, with its scalar–vector form, and the conjugation of each slot is read independently.

### The General Plain Bilinear Product $\tilde Q_1\tilde Q_2$

**Definition.** The **general plain bilinear product** multiplies the coordinates of the two elements on the basis,
$$
\tilde Q_1\tilde Q_2=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}Q_{1\mu} Q_{2\nu}\,e_\mu e_\nu .
$$

Written on the four units, the product is
$$
\tilde Q_1\tilde Q_2=\bigl(Q_{1t}Q_{2t}-Q_{1x}Q_{2x}-Q_{1y}Q_{2y}-Q_{1z}Q_{2z}\bigr)
+\bigl(Q_{1t}Q_{2x}+Q_{1x}Q_{2t}+Q_{1y}Q_{2z}-Q_{1z}Q_{2y}\bigr)\vec e_x
+\bigl(Q_{1t}Q_{2y}-Q_{1x}Q_{2z}+Q_{1y}Q_{2t}+Q_{1z}Q_{2x}\bigr)\vec e_y
+\bigl(Q_{1t}Q_{2z}+Q_{1x}Q_{2y}-Q_{1y}Q_{2x}+Q_{1z}Q_{2t}\bigr)\vec e_z .
$$

The rule is linear in the coordinates $Q_{1t},\dots,Q_{1z}$ and linear in the coordinates $Q_{2t},\dots,Q_{2z}$.

**The scalar–vector form.** Collecting the scalar part and the vector part of the two elements,
$$
\boxed{\;
\tilde Q_1\tilde Q_2=\bigl(Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)\bigr)+Q_{1t}\vec Q_2+Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2
\;}.
$$

The scalar part is $\mathrm{Sc}(\tilde Q_1\tilde Q_2)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_{1\mu} Q_{2\mu}$ with $\varepsilon=(1,-1,-1,-1)$, and the vector part is the one displayed.

**Neither slot is conjugated.** Both factors enter as they stand, so the case carries no involution and no eigenspace splitting; its symmetry is the associativity of the multiplication. The product is the multiplication of the algebra and the only one of the four that is associative, and its scalar part, the plain form, is the only one of the four that is the scalar part of a unital associative product.

### The General Quaternionic Bilinear Product $\tilde Q_1^{\natural}\tilde Q_2$

**Definition.** The **general quaternionic bilinear product** reads the first element through the conjugation ${}^{\natural}$ and leaves the second as it is. The coordinates of the first element enter as
$$
(Q_1^{\natural})_t=Q_{1t} , \qquad (Q_1^{\natural})_x=-Q_{1x} , \qquad (Q_1^{\natural})_y=-Q_{1y} , \qquad (Q_1^{\natural})_z=-Q_{1z} ,
$$
and the product is
$$
\tilde Q_1^{\natural}\tilde Q_2=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}(Q_1^{\natural})_\mu Q_{2\nu}\,e_\mu e_\nu
=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}\varepsilon_\mu Q_{1\mu} Q_{2\nu}\,e_\mu e_\nu .
$$

Written on the four units, the product is
$$
\tilde Q_1^{\natural}\tilde Q_2=\bigl(Q_{1t}Q_{2t}+Q_{1x}Q_{2x}+Q_{1y}Q_{2y}+Q_{1z}Q_{2z}\bigr)
+\bigl(Q_{1t}Q_{2x}-Q_{1x}Q_{2t}-Q_{1y}Q_{2z}+Q_{1z}Q_{2y}\bigr)\vec e_x
+\bigl(Q_{1t}Q_{2y}+Q_{1x}Q_{2z}-Q_{1y}Q_{2t}-Q_{1z}Q_{2x}\bigr)\vec e_y
+\bigl(Q_{1t}Q_{2z}-Q_{1x}Q_{2y}+Q_{1y}Q_{2x}-Q_{1z}Q_{2t}\bigr)\vec e_z .
$$

The rule is linear in the coordinates $Q_{1t},\dots,Q_{1z}$ and linear in the coordinates $Q_{2t},\dots,Q_{2z}$.

**The scalar–vector form.** The scalar part of the first factor stays $Q_{1t}$ and its vector part becomes $-\vec Q_1$, so the two pairings change sign where that vector part enters,
$$
\boxed{\;
\tilde Q_1^{\natural}\tilde Q_2=\bigl(Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)\bigr)+Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2
\;}.
$$

The scalar part is $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)=\sum_{\mu\in\{t,x,y,z\}}Q_{1\mu} Q_{2\mu}$, and the vector part is the one displayed.

**The natural sign in the first slot.** The first factor is read through ${}^{\natural}$, which is a $\mathbb{C}$-linear anti-automorphism and an involution, with $+1$-eigenspace the centre $\mathbb{C}_{\mathbb{B}}$ and $-1$-eigenspace the vector subspace $\mathbb{V}_{\mathbb{B}}$; in the coefficient basis it is $\operatorname{diag}(1,-1,-1,-1)$. The insertion separates the scalar part of the first factor from its vector part, $\tilde Q_1^{\natural}\tilde Q_2=(Q_{1t}e_t)\tilde Q_2-\vec Q_1\tilde Q_2$, and it is the whole difference from the plain case, which differs by the vector part of the first factor alone. The case is $\mathbb{C}$-bilinear and has $e_t$ as a left unit alone.

### The General Plain Sesquilinear Product $\tilde Q_1\tilde Q_2^{*}$

**Definition.** The **general plain sesquilinear product** leaves the first element as it is and reads the second through the conjugation ${}^{*}$. The coordinates of the second element enter as
$$
Q^{*}_0=\overline{Q_t} , \qquad Q^{*}_1=-\overline{Q_x} , \qquad Q^{*}_2=-\overline{Q_y} , \qquad Q^{*}_3=-\overline{Q_z} ,
$$
and the product is
$$
\tilde Q_1\tilde Q_2^{*}=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}Q_{1\mu} (Q_2^{*})_\nu\,e_\mu e_\nu
=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}\varepsilon_\nu Q_{1\mu} \overline{Q_{2\nu}}\,e_\mu e_\nu .
$$

Written on the four units, the product is
$$
\tilde Q_1\tilde Q_2^{*}=\bigl(Q_{1t}\overline{Q_{2t}}+Q_{1x}\overline{Q_{2x}}+Q_{1y}\overline{Q_{2y}}+Q_{1z}\overline{Q_{2z}}\bigr)
+\bigl(-Q_{1t}\overline{Q_{2x}}+Q_{1x}\overline{Q_{2t}}-Q_{1y}\overline{Q_{2z}}+Q_{1z}\overline{Q_{2y}}\bigr)\vec e_x
+\bigl(-Q_{1t}\overline{Q_{2y}}+Q_{1x}\overline{Q_{2z}}+Q_{1y}\overline{Q_{2t}}-Q_{1z}\overline{Q_{2x}}\bigr)\vec e_y
+\bigl(-Q_{1t}\overline{Q_{2z}}-Q_{1x}\overline{Q_{2y}}+Q_{1y}\overline{Q_{2x}}+Q_{1z}\overline{Q_{2t}}\bigr)\vec e_z .
$$

The rule is linear in the coordinates $Q_{1t},\dots,Q_{1z}$ and conjugate-linear in the coordinates $Q_{2t},\dots,Q_{2z}$, conjugation of the coefficients happening inside the product.

**The scalar–vector form.** The scalar part of the second factor becomes $\overline{Q_t}$ and its vector part becomes $-\overline{\vec Q}$, so the two pairings change sign and are read against the conjugate vector,
$$
\boxed{\;
\tilde Q_1\tilde Q_2^{*}=\bigl(Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})\bigr)-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}
\;}.
$$

The scalar part is $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\sum_{\mu\in\{t,x,y,z\}}Q_{1\mu}\overline{Q_{2\mu}}$, conjugate-linear in the coordinates of the second element; the vector part is the one displayed.

**The star in the second slot.** The second factor is read through ${}^{*}$, which is conjugate-linear over $\mathbb{C}$ and an anti-automorphism, with $+1$-eigenspace the Hermitian subspace $\mathbb{M}_+$ and $-1$-eigenspace the anti-Hermitian subspace $\mathbb{M}_-$. The insertion makes the rule conjugate-linear in the second argument, so the case is sesquilinear and not bilinear; it is the **derived operation** of $\mathbb{B}$ with its involution, and $e_t$ is a right unit alone. Its scalar part is the Hermitian form, the one definite form of the four.

### The General Quaternionic Sesquilinear Product $\tilde Q_1^{\natural}\tilde Q_2^{*}$

**Definition.** The **general quaternionic sesquilinear product** reads the first element through ${}^{\natural}$ and the second through ${}^{*}$, the two being read independently. The coordinates enter as $(Q_1^{\natural})_\mu$ in the first factor and $(Q_2^{*})_\nu$ in the second, and the product is
$$
\tilde Q_1^{\natural}\tilde Q_2^{*}=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}(Q_1^{\natural})_\mu (Q_2^{*})_\nu\,e_\mu e_\nu
=\sum_{\mu\in\{t,x,y,z\}}\sum_{\nu\in\{t,x,y,z\}}\varepsilon_\mu\varepsilon_\nu Q_{1\mu} \overline{Q_{2\nu}}\,e_\mu e_\nu .
$$

Written on the four units, the product is
$$
\tilde Q_1^{\natural}\tilde Q_2^{*}=\bigl(Q_{1t}\overline{Q_{2t}}-Q_{1x}\overline{Q_{2x}}-Q_{1y}\overline{Q_{2y}}-Q_{1z}\overline{Q_{2z}}\bigr)
+\bigl(-Q_{1t}\overline{Q_{2x}}-Q_{1x}\overline{Q_{2t}}+Q_{1y}\overline{Q_{2z}}-Q_{1z}\overline{Q_{2y}}\bigr)\vec e_x
+\bigl(-Q_{1t}\overline{Q_{2y}}-Q_{1x}\overline{Q_{2z}}-Q_{1y}\overline{Q_{2t}}+Q_{1z}\overline{Q_{2x}}\bigr)\vec e_y
+\bigl(-Q_{1t}\overline{Q_{2z}}+Q_{1x}\overline{Q_{2y}}-Q_{1y}\overline{Q_{2x}}-Q_{1z}\overline{Q_{2t}}\bigr)\vec e_z .
$$

The rule is linear in the coordinates $Q_{1t},\dots,Q_{1z}$ and conjugate-linear in the coordinates $Q_{2t},\dots,Q_{2z}$.

**The scalar–vector form.** The scalar part of the first factor is $Q_{1t}$ and its vector part is $-\vec Q_1$; the scalar part of the second is $\overline{Q_{2t}}$ and its vector part is $-\overline{\vec Q_2}$, so the dot product enters with a negative sign and the cross product with a positive one, read against the conjugate vector,
$$
\boxed{\;
\tilde Q_1^{\natural}\tilde Q_2^{*}=\bigl(Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})\bigr)-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1+\vec Q_1\times\overline{\vec Q_2}
\;}.
$$

The scalar part is $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$, conjugate-linear in the coordinates of the second element; the vector part is the one displayed.

**The two insertions together, and the fundamental symmetry.** The scalar part is the Krein form, $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})$, with the definite companion $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$; the natural conjugation $J={}^{\natural}$ is its **fundamental symmetry**:
$$
J^2=\mathrm{id},\qquad
\langle\tilde Q_2,J\tilde Q_1\rangle_{\natural*}=\langle J\tilde Q_2,\tilde Q_1\rangle_{\natural*},\qquad
\langle\tilde Q_1,J\tilde Q_1\rangle_{\natural*}=\lVert\tilde Q_1\rVert_E^2>0\quad(\tilde Q_1\neq0).
$$
The bridge between the indefinite and the definite form is
$$
\boxed{\;\langle\tilde Q_2,\tilde Q_1\rangle_{\natural*}=\langle\tilde Q_2,J\tilde Q_1\rangle_{*}=\langle\tilde Q_2,\tilde Q_1^{\natural}\rangle_{*}\;}
$$
The eigenspaces of $J$ are the centre and the vector subspace, of complex dimensions $1$ and $3$; they are definite of the two signs and Krein-orthogonal, so $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathbb{V}_{\mathbb{B}}$ is a fundamental decomposition. Among the fundamental symmetries, $J$ is the unique one that is a unital $\mathbb{C}$-algebra anti-automorphism: such a symmetry fixes $e_t$, so its $+1$-eigenspace is a positive line containing $e_t$, of complex dimension one, and is therefore the centre; it is ${}^{\natural}$. It is not the only fundamental symmetry: every positive definite line $\mathbb{C}(e_t+\tilde V)$ gives the reflection in it, and $J$ is the member $\tilde V=0$.

## The Two Choices and the Remaining Conjugations

The two conjugations of the slots are independent, and the four rules above are the four outcomes:

$$
\tilde Q_1\tilde Q_2 , \qquad
\tilde Q_1^{\natural}\tilde Q_2 , \qquad
\tilde Q_1\tilde Q_2^{*} , \qquad
\tilde Q_1^{\natural}\tilde Q_2^{*} .
$$

Conjugating the first element of the pair and conjugating the second are two involutions of the pair, and they commute, ${}^{\natural}$ and ${}^{*}$ being involutions of the element that commute with each other. The two choices made independently are exactly what produces four rules, and the four are pairwise distinct: no two of the four agree on every pair of elements.

**The two remaining conjugations add nothing new here.** The complex conjugation $\bar{\cdot}$ is an automorphism of the algebra, and the anti-Hermitian conjugation is $-\,{}^{*}$, so neither is one of the two conjugations carried by the four rules. A scalar part read with the complex conjugation in one slot is one of the four scalar parts with the slots exchanged,

$$
\mathrm{Sc}\bigl(\bar{\tilde Q}_1\tilde Q_2\bigr)=\mathrm{Sc}\bigl(\tilde Q_2^{\natural}\tilde Q_1^{*}\bigr) , \qquad
\mathrm{Sc}\bigl(\tilde Q_1\bar{\tilde Q}_2\bigr)=\mathrm{Sc}\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}\bigr) ,
$$

and the conjugation $\flat=-\,{}^{*}$ multiplies the corresponding scalar part by $-1$. The four general products therefore carry the four scalar parts between them, and the two conjugations left out of the list add no new one.


## How Each Factor Enters

The ${}^{\natural}$ in the first slot and the ${}^{*}$ in the second are what distinguish the four from one another, and the two conjugations act on the two factors in the same way: each reverses the sign of the vector part and leaves the scalar part alone, the star conjugating the coefficients on the way. The splitting identities of this section are read on each of the four.

Separating the scalar part of the first factor from its vector part, the general plain bilinear product and the ${}^{\natural}$-product are

$$
\tilde Q_1\tilde Q_2=(Q_{1t}e_t)\tilde Q_2+\vec Q_1\tilde Q_2 , \qquad
\tilde Q_1^{\natural}\tilde Q_2=(Q_{1t}e_t)\tilde Q_2-\vec Q_1\tilde Q_2 ,
$$

the vector part being read as an element where it multiplies. Adding and subtracting,

$$
\boxed{\;
\tilde Q_1\tilde Q_2+\tilde Q_1^{\natural}\tilde Q_2=2Q_{1t}\tilde Q_2 , \qquad
\tilde Q_1\tilde Q_2-\tilde Q_1^{\natural}\tilde Q_2=2\,\vec Q_1\tilde Q_2
\;}.
$$

The same separation applied to the two sesquilinear products gives

$$
\tilde Q_1\tilde Q_2^{*}+\tilde Q_1^{\natural}\tilde Q_2^{*}=2Q_{1t}\tilde Q_2^{*} , \qquad
\tilde Q_1\tilde Q_2^{*}-\tilde Q_1^{\natural}\tilde Q_2^{*}=2\,\vec Q_1\tilde Q_2^{*} .
$$

So the ${}^{\natural}$ in the first slot separates the scalar part of the first factor from its vector part, and the four general products are the two pairs of that separation: the general plain bilinear product and the ${}^{\natural}$-product are separated by the vector part of $\tilde Q_1$, the two sesquilinear ones by the same vector part after the second factor has been conjugated. The two pairs differ from one another by the ${}^{*}$ in the second slot.

One reading follows. The ${}^{\natural}$-product agrees with the general plain bilinear product in its first argument exactly when the vector part of that argument annihilates the second factor,

$$
\tilde Q_1^{\natural}\tilde Q_2=\tilde Q_1\tilde Q_2 \quad\Longleftrightarrow\quad \vec Q_1\tilde Q_2=0 ,
$$

which holds in particular for every central $\tilde Q_1$, the vector part being zero; no two of the four general products agree on every pair, since the vector part of a general element is different from zero.


## The Conjugate of a Product

Conjugating a product conjugates the factors and reverses their order, by the two anti-automorphism rules $(\tilde Q_1\tilde Q_2)^{\natural}=\tilde Q_2^{\natural}\tilde Q_1^{\natural}$ and $(\tilde Q_1\tilde Q_2)^{*}=\tilde Q_2^{*}\tilde Q_1^{*}$. Applied to the four general products,

$$
\boxed{\;
(\tilde Q_1\tilde Q_2)^{\natural}=\tilde Q_2^{\natural}\tilde Q_1^{\natural} , \qquad
(\tilde Q_1\tilde Q_2^{*})^{\natural}=\bar{\tilde Q}_2\tilde Q_1^{\natural} , \qquad
(\tilde Q_1^{\natural}\tilde Q_2)^{\natural}=\tilde Q_2^{\natural}\tilde Q_1 , \qquad
(\tilde Q_1^{\natural}\tilde Q_2^{*})^{\natural}=\bar{\tilde Q}_2\tilde Q_1
\;},
$$

$$
(\tilde Q_1\tilde Q_2)^{*}=\tilde Q_2^{*}\tilde Q_1^{*} , \qquad
(\tilde Q_1\tilde Q_2^{*})^{*}=\tilde Q_2\tilde Q_1^{*} , \qquad
(\tilde Q_1^{\natural}\tilde Q_2)^{*}=\tilde Q_2^{*}\bar{\tilde Q}_1 , \qquad
(\tilde Q_1^{\natural}\tilde Q_2^{*})^{*}=\tilde Q_2\bar{\tilde Q}_1 .
$$

Two of the eight identities exchange the two slots between two of the products, and they are the ones worth keeping. The ${}^{*}$ of the ${}^{*}$-product, and the ${}^{\natural}$ of the ${}^{\natural}$-product, return the same product with the two slots exchanged:

$$
(\tilde Q_1\tilde Q_2^{*})^{*}=\tilde Q_2\tilde Q_1^{*} , \qquad
(\tilde Q_1^{\natural}\tilde Q_2)^{\natural}=\tilde Q_2^{\natural}\tilde Q_1 .
$$

That is exactly the symmetry the corresponding scalar parts have, and it explains them: conjugating the first identity and taking the scalar part gives $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\overline{\mathrm{Sc}(\tilde Q_2\tilde Q_1^{*})}$, and conjugating the second gives $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)=\mathrm{Sc}(\tilde Q_2^{\natural}\tilde Q_1)$. The scalar part of the ${}^{*}$-product is conjugate-symmetric and the scalar part of the ${}^{\natural}$-product is symmetric, and in each case the reason is the identity above.


## The Four Scalar Parts

The scalar part of each of the four general products is read on the coordinates in one of four ways,

| product | scalar part | signs and conjugation |
|---|---|---|
| $\tilde Q_1\tilde Q_2$ | $\sum_\mu\varepsilon_\mu Q_{1\mu} Q_{2\mu}$ | the signs $\varepsilon_\mu$ in both factors |
| $\tilde Q_1^{\natural}\tilde Q_2$ | $\sum_\mu Q_{1\mu} Q_{2\mu}$ | no sign at all |
| $\tilde Q_1\tilde Q_2^{*}$ | $\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | the conjugate in the second factor |
| $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | $\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$ | the signs in the first factor and the conjugate in the second |

with $\varepsilon=(1,-1,-1,-1)$; the first two are linear in the coordinates of both factors and the last two are conjugate-linear in the coordinates of the second. The four are related two by two, the two bilinear ones by the bilinear dot product and the two sesquilinear ones by its Hermitian companion:

$$
\mathrm{Sc}(\tilde Q_1\tilde Q_2)+\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)=2Q_{1t}Q_{2t} , \qquad
\mathrm{Sc}(\tilde Q_1\tilde Q_2)-\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)=-2(\vec Q_1,\vec Q_2) ,
$$

$$
\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})+\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})=2Q_{1t}\overline{Q_{2t}} , \qquad
\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})-\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})=2(\vec Q_1,\overline{\vec Q_2}) .
$$

The sums separate the scalar parts of the two factors, the differences the vector part of the first factor against the second: the two scalar parts of a pair are the same reading with the sign of the vector part of the first factor flipped, and their mean and their half-difference are the two extreme readings.

Three identities move a scalar part from one writing to another. The natural sign may be carried from one factor to the other,

$$
\boxed{\;
\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{\natural})
\;},
$$

and the same holds with the star, $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})=\mathrm{Sc}(\tilde Q_1\bar{\tilde Q}_2)$, while the scalar part is unchanged when both factors are conjugated by the natural sign,

$$
\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{\natural})=\mathrm{Sc}(\tilde Q_1\tilde Q_2) .
$$

The symmetry in the two slots follows from the conjugates of the previous section and is stated here with the four scalar parts: the two bilinear scalar parts are symmetric,

$$
\mathrm{Sc}(\tilde Q_1\tilde Q_2)=\mathrm{Sc}(\tilde Q_2\tilde Q_1) , \qquad
\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)=\mathrm{Sc}(\tilde Q_2^{\natural}\tilde Q_1) ,
$$

and the two sesquilinear ones are conjugate-symmetric,

$$
\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\overline{\mathrm{Sc}(\tilde Q_2\tilde Q_1^{*})} , \qquad
\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})=\overline{\mathrm{Sc}(\tilde Q_2^{\natural}\tilde Q_1^{*})} .
$$

The two sesquilinear identities are the conjugate-symmetry of the two sesquilinear scalar parts; that symmetry is a property of the scalar part and not of the product, since none of the four general products is commutative.


## The Four Vector Parts

The vector parts obey the same two splitting identities as the scalar parts. The splitting holds first at the level of the elements,

$$
\tilde Q_1^{\natural}\tilde Q_2=2Q_{1t}\tilde Q_2-\tilde Q_1\tilde Q_2 , \qquad
\tilde Q_1^{\natural}\tilde Q_2^{*}=2Q_{1t}\tilde Q_2^{*}-\tilde Q_1\tilde Q_2^{*} ,
$$

and reading the vector part of each side gives

$$
\mathrm{Vec}(\tilde Q_1^{\natural}\tilde Q_2)=2Q_{1t}\vec Q_2-\mathrm{Vec}(\tilde Q_1\tilde Q_2) , \qquad
\mathrm{Vec}(\tilde Q_1^{\natural}\tilde Q_2^{*})=-2Q_{1t}\overline{\vec Q_2}-\mathrm{Vec}(\tilde Q_1\tilde Q_2^{*}) .
$$

The first says that the vector part of the ${}^{\natural}$-product is the reflection of the vector part of the general plain bilinear product in $Q_{1t}\vec Q_2$; the second, that the vector part of the sesquilinear pair reflects in $-Q_{1t}\overline{\vec Q_2}$. In full, the four vector parts are two mixed terms and a cross term in each case, and the two signs — the sign of the cross term and the sign of the vector part of the first factor — are what tell the four apart:

| product | vector part | cross term |
|---|---|---|
| $\tilde Q_1\tilde Q_2$ | $Q_{1t}\vec Q_2+Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2$ | $+$ |
| $\tilde Q_1^{\natural}\tilde Q_2$ | $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2$ | $-$ |
| $\tilde Q_1\tilde Q_2^{*}$ | $-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$ | $-$ |
| $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | $-Q_{1t}\overline{\vec Q_2}-\overline{Q_{2t}}\vec Q_1+\vec Q_1\times\overline{\vec Q_2}$ | $+$ |

Deleting the cross term, the first and the second rows are reflections of each other in $Q_{1t}\vec Q_2$, and the third and the fourth in $-Q_{1t}\overline{\vec Q_2}$; the cross term then distinguishes within each pair, and the ${}^{*}$ in the second slot conjugates the coordinates of $\vec Q_2$, reverses the sign of the $Q_{1t}$-term and of the cross term, and leaves the sign of the $Q_{2t}$-term alone.


## The Left Multiplications

The left multiplications of the four general products are the general plain bilinear ones read through the two conjugations. Writing $L_{\tilde Q_1}$ and $R_{\tilde Q_1}$ for the left and right multiplications of the general plain bilinear product, $\tilde Q_3\mapsto\tilde Q_1\tilde Q_3$ and $\tilde Q_3\mapsto\tilde Q_3\tilde Q_1$,

$$
\tilde Q_1\tilde Q_3^{*}=\bigl(R_{\tilde Q_1^{*}}(\tilde Q_3)\bigr)^{*} , \qquad
\tilde Q_1^{\natural}\tilde Q_3=L_{\tilde Q_1^{\natural}}(\tilde Q_3) , \qquad
\tilde Q_1^{\natural}\tilde Q_3^{*}=\bigl(R_{\bar{\tilde Q}_1}(\tilde Q_3)\bigr)^{*} .
$$

The ${}^{\natural}$-product is the left multiplication of the general plain bilinear product re-indexed by the natural sign; the other two are the conjugates of the right multiplications of the general plain bilinear product by the star and by the conjugate of the first factor. The distinction decides which of the four general products have a monoid of left multiplications, and it is worth recording, although the property table itself is §*The Property Table*, below.

For the general plain bilinear product the left multiplications compose by $L_{\tilde Q_1}\circ L_{\tilde Q_4}=L_{\tilde Q_1\tilde Q_4}$, the associativity of the product, so they form a monoid, the image of $\mathbb{B}$ in its endomorphism ring. For the ${}^{\natural}$-product,

$$
L^{\natural}_{\tilde Q_1}\circ L^{\natural}_{\tilde Q_4}
=L_{\tilde Q_1^{\natural}}\circ L_{\tilde Q_4^{\natural}}
=L_{\tilde Q_1^{\natural}\tilde Q_4^{\natural}}
=L^{\natural}_{\tilde Q_4\tilde Q_1} ,
$$

since $\tilde Q_1^{\natural}\tilde Q_4^{\natural}=(\tilde Q_4\tilde Q_1)^{\natural}$; the left multiplications are again closed under composition, in reversed order, and they form a monoid isomorphic to the opposite of the multiplicative monoid of $\mathbb{B}$.

For the two sesquilinear products the composition leaves the class. For the ${}^{*}$-product,

$$
L^{*}_{\tilde Q_1}\circ L^{*}_{\tilde Q_4}(\tilde Q_3)
=\tilde Q_1\bigl(\tilde Q_4\tilde Q_3^{*}\bigr)^{*}
=\tilde Q_1\tilde Q_3\tilde Q_4^{*} ,
$$

which is $\mathbb{C}$-linear in $\tilde Q_3$; every left multiplication of the ${}^{*}$-product is conjugate-linear, so the composition is not one of them, and the left multiplications of the ${}^{*}$-product do not form a monoid. The same computation with $\overline{\tilde Q}_1$ in place of $\tilde Q_1$ settles the fourth operation, whose left multiplications are the conjugates of the right multiplications of the general plain bilinear product: the composition of two of them is linear and the class is not closed.

## The Annihilators

**Definition.** The left and the right annihilator of $\tilde Q$ in the general plain bilinear product are the kernels of its left and right multiplications of §*The Left Multiplications*,

$$
A(\tilde Q)=\{\tilde X:\tilde Q\tilde X=0\}=\ker L_{\tilde Q},\qquad
B(\tilde Q)=\{\tilde X:\tilde X\tilde Q=0\}=\ker R_{\tilde Q}.
$$

**Theorem (the trichotomy).** The quaternionic norm $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ separates the elements into three classes, and the dimension of the annihilator is the same on both sides:

$$
\tilde Q=0:\ \dim A=\dim B=4;\qquad
\langle\tilde Q\rangle_{\natural}\neq0:\ \dim A=\dim B=0;\qquad
\tilde Q\neq0,\ \langle\tilde Q\rangle_{\natural}=0:\ \dim A=\dim B=2.
$$

*Proof.* At the origin both translations vanish. For a unit both are bijections. For a non-zero null element the image of $L_{\tilde Q}$ is the left ideal $\tilde Q\mathbb{B}$, non-zero and proper, since $\tilde Q\tilde X=e_t$ has no solution by the norm criterion (*N-Regularity and Degeneracy in the Biquaternion Algebra*, §*The Two Cases*); a non-zero proper left ideal is minimal and a complex plane (*Ideals and Peirce Decompositions of the Biquaternion Algebra*, §*The Decomposition into Minimal Left and Right Ideals*), so the kernel has dimension $4-2=2$. The right side is the same.

**Proposition (two planes, not one).** On the punctured null cone the two annihilators are distinct complex planes whose intersection is the line $\mathbb{C}\tilde Q^{\natural}$.

*Proof.* Both contain $\tilde Q^{\natural}$, since $\tilde Q\tilde Q^{\natural}=\tilde Q^{\natural}\tilde Q=0$, and both have dimension $2$; they are not equal, because for $\tilde Q=e_t+i\vec e_x$ the element $\tilde X=(e_t-i\vec e_x)\vec e_y/2$ lies in $A(\tilde Q)$ and not in $B(\tilde Q)$.

**Remark (the four products).** An annihilator is the kernel of a left multiplication, so the formulas of §*The Left Multiplications* give the annihilators of the other three products as plain annihilators of conjugated elements: $\ker L^{*}_{\tilde Q}=B(\tilde Q^{*})$, $\ker L^{\natural}_{\tilde Q}=A(\tilde Q^{\natural})$ and $\ker L^{\natural*}_{\tilde Q}=B(\bar{\tilde Q})$. In particular the two annihilators of the ${}^{\natural}$-product coincide, the natural conjugation being a $\mathbb{C}$-linear anti-automorphism of order two (*Annihilators of the General Quaternionic Algebra*, §*The Two Annihilators Coincide*); in the plain product they are genuinely two.

## The Restriction to the Quaternion Subspace

On the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the elements whose coefficients are real, the complex conjugation is the identity, so the star coincides with the natural sign: the two sesquilinear rules then read as the natural conjugates of the two bilinear ones with the slots exchanged, and the two conjugate-linear scalar parts become linear.

For $\bar{\tilde Q}_1=\tilde Q_1$ and $\bar{\tilde Q}_2=\tilde Q_2$, the two sesquilinear products coincide with the natural twists of the two bilinear ones,

$$
\tilde Q_1\tilde Q_2^{*}=\tilde Q_1\tilde Q_2^{\natural} , \qquad
\tilde Q_1^{\natural}\tilde Q_2^{*}=\tilde Q_1^{\natural}\tilde Q_2^{\natural}=(\tilde Q_2\tilde Q_1)^{\natural} ,
$$

so the four general products take the four values $\tilde Q_1\tilde Q_2$, $\tilde Q_1\tilde Q_2^{\natural}$, $\tilde Q_1^{\natural}\tilde Q_2$ and $(\tilde Q_2\tilde Q_1)^{\natural}$, of which the second and the fourth are the natural conjugates of the two products in the reversed order. The scalar parts follow: the second scalar part restricts to the third,

$$
\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\sum_\mu Q_{1\mu} Q_{2\mu}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2) \qquad (\bar{\tilde Q}_1=\tilde Q_1,\ \bar{\tilde Q}_2=\tilde Q_2),
$$

and the fourth restricts to the first. The four scalar parts therefore come in two linear and two conjugate-linear pairs off the subspace and in two linear pairs on it: on the subspace the coefficients are fixed by the complex conjugation, so the star is the natural sign and only the signs $\varepsilon_\mu$ remain.


## The Property Table

The last two rows are the **algebra rows**, and they are the reason the comparison is made. They ask which of the four general products is a multiplication of an algebra of each of the two kinds the corpus has, and each is read with the corpus's own definition of the object and with nothing added to it. **Multiplication of a bilinear $\mathbb{C}$-algebra** is the product of an algebra in the sense of *Algebras*: a $\mathbb{C}$-module with a product additive in each variable and $\mathbb{C}$-bilinear, with no associativity and no unit assumed, so $(\lambda\tilde Q_1)\tilde Q_2 = \lambda(\tilde Q_1\tilde Q_2)$ and $\tilde Q_1(\lambda\tilde Q_2) = \lambda(\tilde Q_1\tilde Q_2)$. **Multiplication of a sesqualgebra over $\mathbb{C}$** is the product of an algebra in the sense of *Sesqualgebras*: additive in each variable, $\mathbb{C}$-linear in the first and conjugate-linear in the second, so $(\lambda\tilde Q_1)\tilde Q_2 = \lambda(\tilde Q_1\tilde Q_2)$ and $\tilde Q_1(\lambda\tilde Q_2) = \bar\lambda(\tilde Q_1\tilde Q_2)$, the base involution being the conjugation $\varsigma(z)=\bar z$. The bilinear case is the trivial-involution collapse of the sesquilinear one, so the two kinds overlap in general; they do not overlap here. A product of full type carries only one involution (*Sesqualgebras*, §*The Collapse at the Identity*), and $\mathbb{B}$ is faithful, its products generate it and it has no nonzero left annihilator, so each of the four general products carries exactly one involution and lies in exactly one of the two rows.

| property | $\tilde Q_1\tilde Q_2$ | $\tilde Q_1^{\natural}\tilde Q_2$ | $\tilde Q_1\tilde Q_2^{*}$ | $\tilde Q_1^{\natural}\tilde Q_2^{*}$ |
|---|---|---|---|---|
| $\mathbb{C}$-linear in the first argument | yes | yes | yes | yes |
| $\mathbb{C}$-linear in the second argument | yes | yes | no | no |
| associative | yes | no | no | no |
| commutative | no | no | no | no |
| $1$ is a left identity | yes | yes | no | no |
| $1$ is a right identity | yes | no | yes | no |
| alternative | yes | no | no | no |
| flexible | yes | no | no | no |
| degree-three identity | yes | no | no | no |
| left multiplications form a monoid | yes | yes | no | no |
| multiplication of an algebra over $\mathbb{C}$ | yes | yes | no | no |
| multiplication of a sesqualgebra over $\mathbb{C}$ | no | no | yes | yes |

The alternative row is satisfied automatically by the general plain bilinear product, which is associative, and it is the three other columns that the row decides. The degree-three row records the identity $\tilde Q_1(\tilde Q_1\tilde Q_1)=(\tilde Q_1\tilde Q_1)\tilde Q_1$ for the operation in question, which is how power associativity is tested for a product of this kind; in this and the two rows above it, juxtaposition stands for the operation of the row. The last two rows ask which of the four general products is a multiplication of an algebra of the two kinds the corpus has, with the definitions of the paragraph above the table and with nothing added to them. The test is the scalar rules alone, and it is decided by the second slot. When the second slot is read without a conjugation, as in $\tilde Q_1\tilde Q_2$ and in $\tilde Q_1^{\natural}\tilde Q_2$, the product is $\mathbb{C}$-bilinear and belongs to the bilinear row; when it carries the star, as in $\tilde Q_1\tilde Q_2^{*}$ and in $\tilde Q_1^{\natural}\tilde Q_2^{*}$, the product is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second and belongs to the sesquilinear row. The witness for each exclusion is one scalar, $\lambda = i$, and one pair, $\tilde Q_1 = \tilde Q_2 = e_t$: for the two bilinear products $\tilde Q_1(i\tilde Q_2) = ie_t$ while $\bar\imath(\tilde Q_1\tilde Q_2) = -ie_t$, so they are not $\varsigma$-sesquilinear for the conjugation; and for the two star-products $\tilde Q_1(i\tilde Q_2) = -ie_t$ while $i(\tilde Q_1\tilde Q_2) = ie_t$, so they are not $\mathbb{C}$-bilinear. The four therefore split two and two by the involution each carries, the bilinear row reading yes, yes, no, no and the sesquilinear row no, no, yes, yes. Neither row separates the third column from the fourth, and none should: the two star-products differ only in the first slot, and ${}^{\natural}$ is $\mathbb{C}$-linear, so both are sesquilinear for the same conjugation. What separates them is the unit, and it is the row "$1$ is a right identity" above: the general plain sesquilinear product has $e_t$ on the right and the complex quaternionic one has not. Equivalently, only the general plain sesquilinear product is the **derived operation** $\tilde Q_1\star\tilde Q_2 = \tilde Q_1\tilde Q_2^{*}$ of $\mathbb{B}$ with its conjugate-linear involution, the standard example of *Sesqualgebras* and the structure of *Introduction to the General Plain Sesqualgebra*. The bilinear row is weakened in the same way by the absence of a qualifier: the sharper statement, that exactly one of the four general products is the multiplication of an **associative unital** $\mathbb{C}$-algebra, is §*Which of the Four Is a Multiplication* below, and it holds because the ${}^{\natural}$-product is neither associative nor two-sidedly unital.


## Bilinearity and Sesquilinearity

The first two rows are read off the definitions. Each of the four general products is $\mathbb{C}$-linear in the first argument: the first factor is either untouched or conjugated by the $\mathbb{C}$-linear map ${}^{\natural}$, and the rest of the computation is linear in it. In the second argument, the general plain bilinear product and the ${}^{\natural}$-product are $\mathbb{C}$-linear, while the two products carrying the star are conjugate-linear, since ${}^{*}$ conjugates the coefficients of the second factor before the multiplication.

The distinction is not a technicality of the definitions: it separates the two rows of the scalar and vector tables above that involve $\overline{\vec Q}$, and it is the reason the fourth column carries no unit and no monoid. It also settles what the four can be used for. A $\mathbb{C}$-bilinear operation on $\mathbb{B}$ defines on $\mathbb{B}$ the structure of an algebra over $\mathbb{C}$, associative or not; a conjugate-linear operation defines no such thing, and the two sesquilinear products are the multiplications of a sesqualgebra over $\mathbb{C}$ instead. The first of the two is nonetheless the multiplication of a sesqualgebra over $\mathbb{C}$ with its conjugation, being the derived operation of the algebra with the star, and that is a multiplication in the second sense the corpus admits (*Introduction to the General Plain Sesqualgebra*); the second is not, since it reads the first factor through the $\mathbb{C}$-linear ${}^{\natural}$ as well. The four remain binary operations of the same kind, with the same two-step rule for their computation.

**The two exchanges, and the class.** The four general products are split against an exchange of the two arguments, and there are two of them. The **exchange by a conjugation** $c$, $f^{c}(\tilde{Q}_1,\tilde{Q}_2)=c(f(\tilde{Q}_2,\tilde{Q}_1))$, composes the swap with $c$ and keeps the class of the two sesquilinear products, whose parts under it are sesquilinear again; the conjugation and the swap repair each other's parity, and this is the exchange the twelve names are read against. The **plain exchange** swaps the arguments and does not keep the class: a part of a sesquilinear product taken under it is only $\mathbb{R}$-bilinear, since the swap moves the conjugate-linear slot to the other side, and its two halves are the operations of *The Sesquilinear Symmetrised Product* and *The Sesquilinear Commutator*. For the plain sesquilinear product and $c=\overline{\cdot}$ the two parts are the scalar part and the vector part of the product, $Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$ and $-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1-\vec Q_1\times\overline{\vec Q_2}$; for the general quaternionic sesquilinear product they are the symmetrisation of $\tilde{Q}_1^{\natural}$ with $\tilde{Q}_2^{*}$ and half their commutator. The two exchanges and their two splits are read in *Symmetric and Antisymmetric Decomposition of the Four General Products*, §*The Exchange Behind the Split* and §*The Method of the Decomposition*.


## The Failure of Associativity

The general plain bilinear product is associative, being the complex-linear extension of the associative quaternion product. The other three products fail it, and each fails it on a triple of basis elements:

$$
(\tilde Q_1^{\natural}\tilde Q_2)^{\natural}\tilde Q_3\neq\tilde Q_1^{\natural}(\tilde Q_2^{\natural}\tilde Q_3)
\quad\text{for}\quad \tilde Q_1=\tilde Q_2=-\vec e_y,\ \tilde Q_3=\vec e_y ,
$$

where the left-hand side is $\vec e_y$ and the right-hand side is $-\vec e_y$; and

$$
(\tilde Q_1\tilde Q_2^{*})\tilde Q_3^{*}\neq\tilde Q_1(\tilde Q_2\tilde Q_3^{*})^{*}
\quad\text{for}\quad \tilde Q_1=-\vec e_z,\ \tilde Q_2=\tilde Q_3=\vec e_y ,
$$

where the left-hand side is $\vec e_z$ and the right-hand side is $-\vec e_z$. For the fourth product,

$$
(\tilde Q_1^{\natural}\tilde Q_2^{*})^{\natural}\tilde Q_3^{*}\neq\tilde Q_1^{\natural}(\tilde Q_2^{\natural}\tilde Q_3^{*})^{*}
\quad\text{for}\quad \tilde Q_1=-\vec e_z,\ \tilde Q_2=\vec e_z,\ \tilde Q_3=e_t ,
$$

with left-hand side $e_t$ and right-hand side $-e_t$. In each case the two sides differ by the sign of a single basis element, and the reason is the same in all three: associativity of the general plain bilinear product lets the parentheses be dropped, and the operation then conjugates a factor and so transposes two of them. For the ${}^{\natural}$-product, for instance, $(\tilde Q_1^{\natural}\tilde Q_2)^{\natural}=\tilde Q_2^{\natural}\tilde Q_1$, so the two sides of the associative identity read $\tilde Q_2^{\natural}\tilde Q_1\tilde Q_3$ and $\tilde Q_1^{\natural}\tilde Q_2^{\natural}\tilde Q_3$, which differ by the transposition of $\tilde Q_1$ and $\tilde Q_2^{\natural}$ alone.

The failure is not repaired by the symmetry of the scalar parts, because that symmetry is a statement about the scalar parts alone. In the first two counterexamples the two sides have the same scalar part, namely zero, and differ in the vector part, and in the third the scalar part changes sign; associativity is a statement about elements, and it is decided on the vector parts.


## Identities and Units

The unit $1=e_t$ of the algebra is a unit for the general plain bilinear product on both sides. For the other three the two sides must be asked separately: ${}^{\natural}$ and ${}^{*}$ both fix the unit, $1^{\natural}=1^{*}=1$, but each of the three operations conjugates the other factor.

For the ${}^{\natural}$-product, $1^{\natural}\tilde Q_2=\tilde Q_2$, so $1$ is a left identity; and $\tilde Q_1^{\natural}1=\tilde Q_1^{\natural}$, which equals $\tilde Q_1$ only when $\tilde Q_1$ is fixed by ${}^{\natural}$, so $1$ is not a right identity, and there is no right identity, since a right identity $E$ would give $\tilde Q_1^{\natural}E=\tilde Q_1$ for all $\tilde Q_1$, hence $E=1$ on taking $\tilde Q_1=1$ and then $\tilde Q_1^{\natural}=\tilde Q_1$ for all $\tilde Q_1$, which is false.

For the ${}^{*}$-product the two sides exchange roles. Here $\tilde Q_1\tilde Q_2^{*}$ leaves the first factor untouched, so $\tilde Q_1 1^{*}=\tilde Q_1$ and $1$ is a right identity, while $1\tilde Q_2^{*}=\tilde Q_2^{*}$ is not $\tilde Q_2$ in general, so $1$ is not a left identity and there is no left identity. This is the one entry of the naive table that is easy to get wrong: because $\tilde Q_2^{*}=\overline{Q_{2t}}e_t-\overline{\vec Q_2}$, the unit is conjugated to itself, and the star product is unital on the right and not on the left.

For the fourth product neither $1^{\natural}\tilde Q_2^{*}=\tilde Q_2^{*}$ nor $\tilde Q_1^{\natural}1=\tilde Q_1^{\natural}$ returns its argument, and the same argument as above shows there is no identity on either side.


## Alternative, Flexible and Power Associative

The three remaining rows record weaker forms of associativity, and each is settled by a short computation on basis elements, recorded below.

The **left alternative** identity is $\tilde Q_1(\tilde Q_1\tilde Q_2)=(\tilde Q_1\tilde Q_1)\tilde Q_2$, and a single failure of either the left or the right law denies alternativity, so it settles the row; it fails for the ${}^{\natural}$-product at $\tilde Q_1=\vec e_z$, $\tilde Q_2=-\vec e_z$, where the left-hand side is $\vec e_z$ and the right-hand side is $-\vec e_z$, for the ${}^{*}$-product at $\tilde Q_1=-\vec e_z$, $\tilde Q_2=\vec e_z$, with the same two values, and for the fourth product at $\tilde Q_1=e_t$, $\tilde Q_2=ie_t$, where the two sides are $ie_t$ and $-ie_t$. The **flexible** identity is $(\tilde Q_1\tilde Q_2)\tilde Q_1=\tilde Q_1(\tilde Q_2\tilde Q_1)$; it fails for the ${}^{\natural}$-product at $\tilde Q_1=\vec e_z$, $\tilde Q_2=e_t$, the two sides being $-e_t$ and $e_t$, for the ${}^{*}$-product at $\tilde Q_1=-\vec e_y$, $\tilde Q_2=e_t$, the two sides being $e_t$ and $-e_t$, and for the fourth product at $\tilde Q_1=ie_t$, $\tilde Q_2=e_t$, with the same two values. The **degree-three** identity $\tilde Q_1(\tilde Q_1\tilde Q_1)=(\tilde Q_1\tilde Q_1)\tilde Q_1$ fails for all three products: for the ${}^{\natural}$-product and for the ${}^{*}$-product at $\tilde Q_1=\vec e_z$, where the two sides are $-\vec e_z$ and $\vec e_z$ in the first case and $\vec e_z$ and $-\vec e_z$ in the second, and for the fourth product at $\tilde Q_1=i\vec e_z$, where the two sides are $i\vec e_z$ and $-i\vec e_z$.

The general plain bilinear product satisfies all three, being associative, and it is the only one of the four that does. The pattern is the one the table shows: the four general products have the four displayed scalar parts and are told apart by their vector parts, and every one of these identities is an identity of elements, hence decided on the vector parts.


## Which of the Four Is a Multiplication

The four rules are not unrelated: each is the **general plain bilinear product with a conjugation inserted in one or both slots**:

$$
\tilde Q_1^{\natural}\tilde Q_2 = \natural(\tilde Q_1)\,\tilde Q_2 , \qquad
\tilde Q_1\tilde Q_2^{*} = \tilde Q_1\,\natural(\bar{\tilde Q}_2) , \qquad
\tilde Q_1^{\natural}\tilde Q_2^{*} = \natural(\tilde Q_1)\,\natural(\bar{\tilde Q}_2) ,
$$

the general plain bilinear product itself being read with no insertion. Here the complex conjugation $\bar{\cdot}$ conjugates the coefficients, ${}^{\natural}$ negates the vector units, the two commute, and $\tilde Q_2^{*} = \natural(\bar{\tilde Q}_2) = \bar{\tilde Q_2^{\natural}}$. The map ${}^{\natural}$ is a $\mathbb{C}$-linear anti-automorphism of $\mathbb{B}$, and $\bar{\cdot}$ is an automorphism of its underlying real algebra that is conjugate-linear over $\mathbb{C}$ (*The Group of Involutions*). Two rows of the table are read off from the insertion: the reversed order in which the left multiplications of the $\natural$-product compose follows from the anti-automorphism, $\natural(\tilde Q_1\tilde Q_2) = \natural(\tilde Q_2)\natural(\tilde Q_1)$, and the conjugate-linearity in the second argument of the two star-products follows from the conjugate-linearity of $\bar{\cdot}$.

Only the general plain bilinear product is a multiplication in the sense of algebra. It is $\mathbb{C}$-bilinear in both arguments, associative, commutative in its scalar part alone, and unital with a two-sided unit; it is the product that makes $\mathbb{B}$ an associative algebra with unit over $\mathbb{C}$, and it is the one whose associated structures — the remarkable subspaces, the Jordan and the Lie structures of *Symmetric and Antisymmetric Decomposition of the Four General Products*, the zero divisors and the idempotents — the rest of the category develops.

The ${}^{\natural}$-product is $\mathbb{C}$-bilinear, and that is all: it is not associative and it is unital on the left only. It defines on the underlying vector space a non-associative algebra structure in the weak sense, one that agrees with the general plain bilinear product on the centre and disagrees on the vector parts; it is the product whose scalar part is the signless sum $\sum_\mu Q_{1\mu} Q_{2\mu}$.

The two products carrying the star are not multiplications of a bilinear $\mathbb{C}$-algebra at all: being conjugate-linear in their second argument they cannot be. Both are multiplications of a sesqualgebra over the conjugation, and within the pair they are separated by the unit. The general plain sesquilinear product is the derived operation $\tilde Q_1\star\tilde Q_2 = \tilde Q_1\tilde Q_2^{*}$ of $\mathbb{B}$ with its conjugate-linear involution, that is the standard example of the category, and $e_t$ is a right unit of it; the general quaternionic sesquilinear product reads the first factor through the $\mathbb{C}$-linear ${}^{\natural}$ as well and has no right unit, so it is a sesquilinear multiplication that is not the derived one (*Introduction to the General Plain Sesqualgebra*). The classification of the four general products is therefore: one multiplication of an associative unital algebra, one bilinear product that fails associativity and two-sidedness, and two multiplications of a sesqualgebra, of which the complex one is the derived operation with the right unit and the complex quaternionic one is not the derived operation and has no right unit.

The order of the four general products is the order of the two slots: the first slot is read plain or through ${}^{\natural}$ and runs the outer loop, the second plain or through ${}^{*}$ and runs the inner loop, so the quaternionic bilinear product is the second case and the plain sesquilinear product the third. The general plain bilinear product is the multiplication of the associative unital algebra; the general quaternionic bilinear product is the same multiplication with ${}^{\natural}$ in the first slot, non-associative and unital on the left alone; the general plain sesquilinear product is the derived operation, the multiplication the sesqualgebra takes; and the general quaternionic sesquilinear product is the same derived operation with ${}^{\natural}$ in the first slot, with no unit at all.

Each of the four general products is read as a multiplication in an article of its own: the general plain bilinear product in *The Biquaternion Algebra and Its Vector Spaces*, the general quaternionic bilinear product in *Introduction to the General Quaternionic Algebra*, the general plain sesquilinear product in *Introduction to the General Plain Sesqualgebra*, and the general quaternionic sesquilinear product in *Introduction to the General Quaternionic Sesqualgebra*; the entries of the table above are the statements those four articles prove or quote.

The four rules are also one rule with a conjugation inserted in each slot. The two insertions commute, the four readings form a group $\mathbb{Z}_2\times\mathbb{Z}_2$, and read on a general algebra with its two anti-involutions they give the slot family: the second slot carries the $\mathbb{C}$-bilinearity in the second argument, the left unit and the monoid of left multiplications, the first slot carries the right unit, and associativity and the scalar square are decided by the counterexamples above. That construction, the group of the readings and the table of the slots are *Introduction to the Operators of the Biquaternion Algebra*, §*The Four Readings and Their Group*.


## Summary

The four general products of the underlying complex space of $\mathbb{B}$ are read on one and the same pair, each with either element read as it stands or through a conjugation: the natural ${}^{\natural}$ in the first slot and the Hermitian ${}^{*}$ in the second. They are the general plain bilinear product $\tilde Q_1\tilde Q_2$, the general quaternionic bilinear product $\tilde Q_1^{\natural}\tilde Q_2$, the general plain sesquilinear product $\tilde Q_1\tilde Q_2^{*}$ and the general quaternionic sesquilinear product $\tilde Q_1^{\natural}\tilde Q_2^{*}$, and no two agree on every pair. The two remaining conjugations add no new scalar part, since $\mathrm{Sc}(\bar{\tilde Q}_1\tilde Q_2)=\mathrm{Sc}(\tilde Q_2^{\natural}\tilde Q_1^{*})$ and $\mathrm{Sc}(\tilde Q_1\bar{\tilde Q}_2)=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})$.

The conjugation in a slot separates the scalar part of that factor from its vector part: $\tilde Q_1\tilde Q_2\pm\tilde Q_1^{\natural}\tilde Q_2$ is $2Q_{1t}\tilde Q_2$ or $2\vec Q_1\tilde Q_2$, and the same two identities hold with $\tilde Q_2^{*}$ in place of $\tilde Q_2$; they hold again for the vector parts. The ${}^{\natural}$ of the ${}^{\natural}$-product and the ${}^{*}$ of the ${}^{*}$-product return the product with its slots exchanged, which is why the scalar parts of those two are symmetric and conjugate-symmetric, while no one of the four products is commutative. The four scalar parts are $\sum_\mu\varepsilon_\mu Q_{1\mu}Q_{2\mu}$, $\sum_\mu Q_{1\mu}Q_{2\mu}$, $\sum_\mu Q_{1\mu}\overline{Q_{2\mu}}$ and $\sum_\mu\varepsilon_\mu Q_{1\mu}\overline{Q_{2\mu}}$, in the order of the two slots. The case with both slots conjugated is the one that carries a symmetry: the natural conjugation is the fundamental symmetry of the Krein form, with bridge $\langle\tilde Q_2,\tilde Q_1\rangle_{\natural*}=\langle\tilde Q_2,J\tilde Q_1\rangle_{*}$, and it is the unique such symmetry that is a unital $\mathbb{C}$-algebra anti-automorphism.

The comparison gives the property table. Each of the four is $\mathbb{C}$-linear in the first argument; the general plain bilinear product and the ${}^{\natural}$-product are $\mathbb{C}$-linear in the second, the two products carrying the star are conjugate-linear there. The general plain bilinear product is associative, has the two-sided unit $1$, is alternative, flexible and satisfies the degree-three identity, and its left multiplications form a monoid. The ${}^{\natural}$-product is $\mathbb{C}$-bilinear, has the left unit $1$ alone, and fails associativity, the alternative identities, flexibility and the degree-three identity, as do the two sesquilinear products, which have no identity and whose left multiplications do not form a monoid. The left multiplications of the four are the plain ones read through the conjugations: $L^{*}_{\tilde Q_1}=(\cdot)^{*}\circ R_{\tilde Q_1^{*}}$, $L^{\natural}_{\tilde Q_1}=L_{\tilde Q_1^{\natural}}$ and $L^{\natural*}_{\tilde Q_1}=(\cdot)^{*}\circ R_{\bar{\tilde Q}_1}$.

The annihilators are the kernels of these multiplications: the plain ones have dimension $4$ at the origin, $0$ at a unit and $2$ on the punctured cone, where the left and the right annihilator are distinct planes meeting in the line $\mathbb{C}\tilde Q^{\natural}$; the annihilators of the other three products are plain annihilators of conjugated elements, and those of the ${}^{\natural}$-product coincide.

Exactly one of the four is a multiplication of an associative unital $\mathbb{C}$-algebra, the general plain bilinear product; the ${}^{\natural}$-product is $\mathbb{C}$-bilinear but neither associative nor two-sidedly unital. The two products carrying the star are multiplications of a sesqualgebra over $\mathbb{C}$; among them the general plain sesquilinear product is the derived operation of $\mathbb{B}$ with its involution and has $e_t$ as a right unit, while the general quaternionic one has neither property.

The four are told apart on one element by the square: $\mathrm{Sc}(\tilde Q\tilde Q)=Q_t^2-(\vec Q,\vec Q)$, $\mathrm{Sc}(\tilde Q^{\natural}\tilde Q)=Q_t^2+(\vec Q,\vec Q)$, $\mathrm{Sc}(\tilde Q\tilde Q^{*})=\sum_\mu\lvert Q_\mu\rvert^2$ and $\mathrm{Sc}(\tilde Q^{\natural}\tilde Q^{*})=\lvert Q_t\rvert^2-\sum_k\lvert Q_k\rvert^2$, and only the ${}^{\natural}$-square is a scalar element, $\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_t$; the idempotents and the roots that follow from them are *Square Roots of One and the Idempotents of the Biquaternion Algebra*, and the square-roots article of each of the other three products.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\tilde Q_2$ | the general plain bilinear product |
| $\tilde Q_1^{\natural}\tilde Q_2$ | the general quaternionic bilinear product |
| $\tilde Q_1\tilde Q_2^{*}$ | the general plain sesquilinear product |
| $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | the general quaternionic sesquilinear product |
| $\tilde Q_1=Q_{1t}e_t+\vec Q_1$, $\tilde Q_2=Q_{2t}e_t+\vec Q_2$ | the two elements and their four complex coordinates |
| $\tilde Q_1^{\natural}$, $\tilde Q_1^{*}$ | the two conjugations, in coordinates |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ | the Hermitian form, the scalar part of the plain sesquilinear product |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})$ | the Krein form, the scalar part of the quaternionic sesquilinear product |
| $J={}^{\natural}$ | the natural conjugation, the fundamental symmetry of the Krein form |
| $\vec Q_1=Q_{1x}\vec e_x+Q_{1y}\vec e_y+Q_{1z}\vec e_z$ | the vector part, read as an element where it multiplies |
| $(\vec Q_1,\vec Q_2)=\sum_kQ_{1k}Q_{2k}$ | the complex bilinear dot product |
| $\vec Q_1\times\vec Q_2$ | the complex bilinear cross product |
| $\overline{\vec Q}$ | the coefficientwise conjugate of the vector part |
| $\varepsilon=(1,-1,-1,-1)$ | the sign vector |
| $\mathrm{Sc}$, $\mathrm{Vec}$ | the scalar part and the vector part of an element |
| $L_{\tilde Q_1}$, $R_{\tilde Q_1}$ | the left and right multiplications of the general plain bilinear product |
| $L^{\natural}_{\tilde Q_1}$, $L^{*}_{\tilde Q_1}$, $L^{\natural*}_{\tilde Q_1}$ | the left multiplications of the three other products |
| $A(\tilde Q)=\ker L_{\tilde Q}$, $B(\tilde Q)=\ker R_{\tilde Q}$ | the left and the right annihilator of the general plain bilinear product |
| $\mathbb{H}_{\mathbb{B}}$ | the real quaternion subspace, the elements with real coefficients |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ | the quaternionic norm, the scalar part of the ${}^{\natural}$-square |

## Further Reading

- [The Biquaternion Algebra and Its Vector Spaces](the-biquaternion-algebra-and-its-vector-spaces.html), for the algebra, the element, the basis and the four conjugations.
- [Introduction to the Operators of the Biquaternion Algebra](the-four-general-products-and-operators.html), for the four readings, the group they form, the slot family and the table of the slots.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the four scalar parts as forms and their diagonals as algebraic norms.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the twelve products and the two halves of each general product.
- [Remarkable Subspaces and the Four General Products, Forms and Norms](remarkable-subspaces-and-the-four-general-products-forms-and-norms.html), for the four products read on the remarkable subspaces.
- [Remarkable Subspaces and the Two General Products](remarkable-subspaces-and-the-two-general-products.html), for the same reading in the algebra over the real scalars.
- [Algebras: A General Introduction](algebras-a-general-introduction.html) and [Non-Associative Algebras and the Property Ladder](non-associative-algebras-and-the-property-ladder.html), for the algebra axioms and the identities of the table.
- [Introduction to the General Plain Sesqualgebra](introduction-to-the-general-plain-sesqualgebra.html), [Introduction to the General Quaternionic Algebra](introduction-to-the-general-quaternionic-algebra.html) and [Introduction to the General Quaternionic Sesqualgebra](introduction-to-the-general-quaternionic-sesqualgebra.html), for the three other products read as multiplications in their own structures.
- [Annihilators of the General Quaternionic Algebra](annihilators-of-the-general-quaternionic-algebra.html), for the annihilators of the ${}^{\natural}$-product, which coincide.
