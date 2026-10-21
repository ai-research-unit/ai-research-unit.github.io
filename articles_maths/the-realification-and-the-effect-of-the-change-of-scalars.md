# __The Realification and the Effect of the Change of Scalars__

## Introduction

The biquaternion ring $\mathbb{B}$ is one ring and it carries two scalar readings: the complex reading, in which the scalars are $\mathbb{C}$ and the products of the twelve algebraic structures are $\mathbb{C}$-bilinear or $\mathbb{C}$-sesquilinear, and the real reading, in which the scalars are $\mathbb{R}$ and every one of the twelve products is $\mathbb{R}$-bilinear. The passage from the first to the second is a construction, and this article owns that construction and its effect on the objects the corpus builds on the ring.

The construction has one name in the corpus, **realification**: keep the elements, the addition and the product, take the scalars to be the subfield $\mathbb{R}$ of the centre $\mathbb{C}_{\mathbb{B}}$, and read every object attached to the complex reading — vector space, linear map, form, operator, subalgebra, module — with that smaller field of scalars. It is **restriction of scalars** followed by the forgetting of the complex structure $J$, and the double description is the useful one: restriction of scalars is the bookkeeping of the field, and the forgetting of $J$ is the geometric content.

Two sibling articles state the theory and are cited and not repeated. This article owns what is left and what is general: the realification of a vector space, of a linear map, of a form and of an operator, the four effects the passage has on a structure, and the reading of the twelve algebraic structures under those effects. Its last section reads the four things specific to the biquaternion instance: the odd real subalgebras, the Galois-twisted automorphisms, the trace form and the real models.

**Boundary.** The products are *The Four General Products of the Biquaternion $\mathbb{C}$ Space* and *The 12 Products of the Biquaternion Complex Space*; the forms are *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*; the realified forms, their Gram matrices and their signatures are **The Realification of the Four Forms**, quoted here in the general case and not re-derived; The real reading of the ring itself, with its multiplication table and its admissible bases, is **The Realification and the Effect of the Change of Scalars**, the entry of the General Plain Algebra block over $\mathbb{R}$. The general theory of restriction and extension of scalars and of real forms is *Change of Rings*, *Extension of Scalars* and *Real Forms and the Descent of an Algebra*.

## The Realification of a Vector Space

**Definition (the realification of a complex vector space).** Let $V$ be a vector space over $\mathbb{C}$, of complex dimension $n$. Its **realification** $V_{\mathbb{R}}$ is the same set with the same addition, with the scalars restricted to $\mathbb{R}$. It is written $\operatorname{Res}_{\mathbb{C}/\mathbb{R}} V$, and the construction is **restriction of scalars**.

**Proposition (the dimension doubles).** If $e_1,\dots,e_n$ is a $\mathbb{C}$-basis of $V$, then
$$
e_1,\dots,e_n,\ i e_1,\dots,i e_n
$$
is an $\mathbb{R}$-basis of $V_{\mathbb{R}}$, and $\dim_{\mathbb{R}} V_{\mathbb{R}}=2\dim_{\mathbb{C}} V$.

*Proof.* Every element is $\sum_\mu\lambda_\mu e_\mu$ with $\lambda_\mu\in\mathbb{C}$, and writing $\lambda_\mu=a_\mu+ib_\mu$ with $a_\mu,b_\mu\in\mathbb{R}$ gives $\sum_\mu a_\mu e_\mu+\sum_\mu b_\mu (ie_\mu)$, so the displayed family spans. If $\sum_\mu a_\mu e_\mu+\sum_\mu b_\mu ie_\mu=0$ then $\sum_\mu(a_\mu+ib_\mu)e_\mu=0$ with $a_\mu+ib_\mu\in\mathbb{C}$, so each $a_\mu+ib_\mu=0$ and then each $a_\mu=b_\mu=0$; the family is free.

**Definition (the complex structure).** On $V_{\mathbb{R}}$ the multiplication by $i$ is the real-linear map
$$
J:V_{\mathbb{R}}\longrightarrow V_{\mathbb{R}},\qquad J(v)=iv ,
$$
written also $J=\operatorname{Res}_{\mathbb{C}/\mathbb{R}}(i\cdot)$.

**Proposition (the properties of $J$).** The map $J$ is $\mathbb{R}$-linear, satisfies $J^2=-\mathrm{id}$, has no real eigenvalue, and its invariant subspaces are the complex subspaces of $V$: an $\mathbb{R}$-subspace $W\subseteq V_{\mathbb{R}}$ is a $\mathbb{C}$-subspace of $V$ exactly when $JW=W$.

*Proof.* The map $J$ is $\mathbb{R}$-linear because multiplication is additive and $J(\lambda v)=i\lambda v=\lambda\,J(v)$ for $\lambda\in\mathbb{R}$; it satisfies $J^2=-\mathrm{id}$ because $i^2=-1$; an eigenvector of eigenvalue $\lambda\in\mathbb{R}$ would satisfy $iv=\lambda v$, whence $(-\lambda^2+0)v=0$ and $\lambda^2+1=0$, impossible. For the last statement, $W$ is a $\mathbb{C}$-subspace when it is closed under multiplication by $i$, which is $JW\subseteq W$, and a subspace closed under $J$ has $\dim J W=\dim W$ and hence $JW=W$.

**Theorem (the pair recovers the space, the map is the content).** The complex vector space $V$ is recovered from the pair $(V_{\mathbb{R}},J)$: the complex scalars are the maps $a\,\mathrm{id}+bJ$ with $a,b\in\mathbb{R}$, and the multiplication by $\lambda=a+ib$ is the real-linear map $a\,\mathrm{id}+bJ$. Conversely, forgetting $J$ leaves $V_{\mathbb{R}}$. The realification therefore **loses** exactly $J$ and nothing else.

*Proof.* The displayed map sends $v$ to $av+ibv=\lambda v$ and is real-linear; the assignment $\lambda\mapsto a\,\mathrm{id}+bJ$ is a ring isomorphism $\mathbb{C}\to\mathbb{R}[t]/(t^2+1)$ onto the algebra generated by $\mathrm{id}$ and $J$, by $J^2=-\mathrm{id}$. Hence the complex linear structure is the real linear structure together with $J$.

**Remark (realification is not the inverse of complexification).** The complexification of $V_{\mathbb{R}}$ is $\mathbb{C}\otimes_{\mathbb{R}}V_{\mathbb{R}}$, of complex dimension $2n$, and it is **not** $V$: it is $V\oplus\bar V$, the sum of the space and its conjugate. The realification lowers the scalar field and doubles the dimension over the new field; the complexification raises it and doubles the dimension again. The two constructions are not inverse, and only the pair $(V_{\mathbb{R}},J)$ returns $V$ (*Change of Rings*, *Extension of Scalars*).

## The Realification of a Linear Map

**Theorem (the criterion for $\mathbb{C}$-linearity).** Let $T:V\to W$ be a map of complex vector spaces. Then $T$ is $\mathbb{C}$-linear if and only if $T$ is $\mathbb{R}$-linear on the realifications and commutes with the complex structures,
$$
T J_V = J_W T .
$$

*Proof.* If $T$ is $\mathbb{C}$-linear then it is $\mathbb{R}$-linear and $T(iv)=iT(v)$, which is the displayed identity. Conversely if $T$ is $\mathbb{R}$-linear and commutes with $J$, then $T\bigl((a+ib)v\bigr)=T(av+bJ_Vv)=aT(v)+bJ_WT(v)=(a+ib)T(v)$, so $T$ is $\mathbb{C}$-linear.

**Definition (the conjugate-linear maps).** A map $S:V\to W$ is **conjugate-linear**, or $\mathbb{C}$-antilinear, if it is additive in the arguments and $S(\lambda v)=\bar\lambda\,S(v)$ for $\lambda\in\mathbb{C}$.

**Theorem (the conjugate-linear maps are the anticommuting ones).** A map $S:V\to W$ is conjugate-linear if and only if it is $\mathbb{R}$-linear on the realifications and anticommutes with the complex structures,
$$
S J_V = - J_W S .
$$

*Proof.* If $S$ is conjugate-linear then it is $\mathbb{R}$-linear and $S(iv)=S(i\,v)=-iS(v)$, which is the display. Conversely $\mathbb{R}$-linearity with $S J_V=-J_W S$ gives $S\bigl((a+ib)v\bigr)=a\,S(v)-b\,J_WS(v)=(a-ib)S(v)$.

**Corollary (the maps that appear in the passage).** The realifications bring in the conjugate-linear maps, which are no part of the complex-linear structure: the $\mathbb{R}$-linear endomorphisms of $V_{\mathbb{R}}$ split as
$$
\operatorname{End}_{\mathbb{R}}(V_{\mathbb{R}})=\operatorname{End}_{\mathbb{C}}(V)\oplus \operatorname{Ant}_{\mathbb{C}}(V),
$$
the commuting and the anticommuting endomorphisms, of real dimensions $2n^2$ and $2n^2$ and of complex dimensions $n^2$ and $n^2$.

*Proof.* Write $T\in\operatorname{End}_{\mathbb{R}}(V_{\mathbb{R}})$ and put $P=\tfrac12(T-JTJ^{-1})$ and $N=\tfrac12(T+JTJ^{-1})$. Then $T=P+N$, and $P J=JP$ while $N J=-JN$, so $P$ is $\mathbb{C}$-linear and $\langle\cdot,\cdot\rangle_{\natural}$ conjugate-linear by the two criteria; the two families are disjoint, since a map that is both satisfies $N=0$. Each family has real dimension $4n^2/2=2n^2$, and the complex dimension of a conjugate-linear family is $n^2$ by the convention of the next proposition.

**Proposition (the matrix form in the real basis).** Let $T$ be $\mathbb{R}$-linear on $V_{\mathbb{R}}$ with real matrix $M$ in the real basis $e_1,\dots,e_n,ie_1,\dots,ie_n$, written in the two blocks of the complex basis and its multiple by $i$. Then

- $T$ is $\mathbb{C}$-linear with complex matrix $A+iB$ if and only if
$$
M=\begin{pmatrix} A & -B \\ B & A\end{pmatrix};
$$
- $T$ is conjugate-linear with the same lettering, $T(v)=(A+iB)\bar v$ in the complex coordinates, if and only if
$$
M=\begin{pmatrix} A & B \\ B & -A\end{pmatrix}.
$$

*Proof.* For a complex coordinate $z=x+iy$, a $\mathbb{C}$-linear map sends $z\mapsto(A+iB)z=(Ax-By)+i(Bx+Ay)$, which is the first block matrix acting on the column $(x,y)$; a conjugate-linear map sends $z\mapsto(A+iB)\bar z=(Ax+By)+i(Bx-Ay)$, which is the second.

**Remark (the two block shapes are the two criteria).** The block matrices are the criteria of this section written in coordinates. The $\mathbb{C}$-linear shape $\begin{pmatrix}A&-B\\B&A\end{pmatrix}$ is the commutation $T\,J=J\,T$; the conjugate-linear shape $\begin{pmatrix}A&B\\B&-A\end{pmatrix}$ is the anticommutation $T\,J=-J\,T$. A conjugate-linear map has no $\mathbb{C}$-linear reading, and that is what makes the difference between the two readings structural and not merely notational.

## The Realification of a Form

**Definition (the realification of a form).** Let $\Phi:V\times V\to\mathbb{C}$ be additive in each argument and $\mathbb{C}$-linear or conjugate-linear in each. Its **realification** is the real-valued form
$$
\Phi_{\mathbb{R}}(P,Q)=\operatorname{Re}\Phi(P,Q).
$$

**Theorem (the two kinds realify differently).** Let $\Phi$ be nondegenerate on a complex space of dimension $n$.

1. If $\Phi$ is a symmetric $\mathbb{C}$-**bilinear** form, then $\Phi_{\mathbb{R}}$ and the form $\operatorname{Im}\Phi$ are two real symmetric bilinear forms, and $\Phi_{\mathbb{R}}$ has signature $(n,n)$ after the identification $\mathbb{R}^{2n}$.
2. If $\Phi$ is a **Hermitian** form, $\Phi(P,Q)=\overline{\Phi(Q,P)}$, then $\Phi$ is real-valued at the two equal arguments and its imaginary part is alternating, $\operatorname{Im}\Phi(P,Q)=-\operatorname{Im}\Phi(Q,P)$, which is the companion of the two sesquilinear forms of the corpus and is no part of the realification: the realification is the real part $\Phi_{\mathbb{R}}=\operatorname{Re}\Phi$, a real symmetric bilinear form, and if the complex inertia of $\Phi$ is $(n,m)$ then the signature of $\Phi_{\mathbb{R}}$ is $(2p,2q)$.

*Proof.* (1) A nondegenerate symmetric bilinear form over $\mathbb{C}$ is classified by its rank alone, so on a suitable $\mathbb{C}$-basis its Gram matrix is $\mathrm{I}_n$. In the real basis $e_1,\dots,e_n,ie_1,\dots,ie_n$ the entries are $\Phi(e_\mu,e_\nu)=\delta_{\mu\nu}$, $\Phi(e_\mu,ie_\nu)=i\delta_{\mu\nu}$, $\Phi(ie_\mu,ie_\nu)=-\delta_{\mu\nu}$; taking real parts gives the block matrix $\operatorname{diag}(\mathrm{I}_n,-\mathrm{I}_n)$, of signature $(n,n)$, and taking imaginary parts gives the second real symmetric bilinear form of the same block structure shifted by $J$. (2) The Hermitian property gives $\Phi(P,P)=\overline{\Phi(P,P)}$, so the algebraic norm is real, and the imaginary part is alternating, $\operatorname{Im}\Phi(P,Q)=-\operatorname{Im}\Phi(Q,P)$; the real part $\operatorname{Re}\Phi$ is a real symmetric bilinear form. A Hermitian form diagonalises with real eigenvalues; writing the algebraic norm as $\sum_\mu\varepsilon_\mu\lvert z_\mu\rvert^2$ and passing to $z_\mu=x_\mu+iy_\mu$ gives $\sum_\mu\varepsilon_\mu(x_\mu^2+y_\mu^2)$, whose signature is $(2p,2q)$.

**Corollary (the four realified signatures).** For the four forms of the corpus the theorem gives

| form | complex reading | realified signature |
|---|---|---|
| general plain bilinear $\langle\cdot,\cdot\rangle$ | symmetric bilinear, rank $4$ | $(4,4)$ |
| general plain sesquilinear (Hermitian) $\langle\cdot,\cdot\rangle_{*}$ | Hermitian, inertia $(4,0)$ | $(8,0)$ |
| general quaternionic bilinear $\langle\cdot,\cdot\rangle_{\natural}$ | symmetric bilinear, rank $4$ | $(4,4)$ |
| general quaternionic sesquilinear (Krein) $\langle\cdot,\cdot\rangle_{\natural*}$ | Hermitian, inertia $(1,3)$ | $(2,6)$ |

the four entries of **The Realification of the Four Forms**, §*The Four Gram Matrices*, quoted here as the instances of the two rules.

**Proposition (the action of the complex structure on the two kinds).** On the realifications,
$$
\Phi_{\mathbb{R}}(JP,JQ)=-\Phi_{\mathbb{R}}(P,Q)
$$
for the two bilinear forms, and
$$
\Phi_{\mathbb{R}}(JP,JQ)=+\Phi_{\mathbb{R}}(P,Q)
$$
for the two sesquilinear forms.

*Proof.* For a $\mathbb{C}$-bilinear form, $\Phi(iP,iQ)=i^2\Phi(P,Q)=-\Phi(P,Q)$, and taking real parts gives the first display. For a Hermitian form, $\Phi(iP,iQ)=i\bar i\,\Phi(P,Q)=\Phi(P,Q)$, and the second follows. The sign is the same statement as the block shapes of the two Gram matrices: the bilinear realification has the two blocks $\mathrm{D}$ and $-\mathrm{D}$ while the Hermitian one repeats its block.

**Remark (the two rules and the four signatures).** The four signatures of the corpus are not four unrelated computations: they are two rules applied twice. The two **bilinear** forms of the corpus realify to the split signature $(n,n)=(4,4)$, because over $\mathbb{C}$ a symmetric bilinear form has no inertia beyond its rank. The two **Hermitian** forms realify by doubling their complex inertia, $(4,0)\mapsto(8,0)$ and $(1,3)\mapsto(2,6)$. A reader who expects one rule for the four has one rule too many; the two slots of the general product are what decides which rule applies, exactly as in *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*.

## The Four Effects on a Structure

**Theorem (the dictionary).** Let a structure be built from the ring $\mathbb{B}$ by its operations. Then two statements about it are distinguished. A statement **about the ring** is expressed using the addition, the product, the identity and quantification over the elements of $\mathbb{B}$ alone. A statement **about the scalars** mentions the field of scalars, a dimension over that field, a tensor product over that field, or requires a map to be scalar-linear. A statement about the ring has the same truth value in the two readings; a statement about the scalars may change.

*Proof.* The change of scalars replaces the structure map $k\to Z(\mathbb{B})$ and leaves the additive group and the product untouched; a statement about the ring is evaluated on that same group and product and so is unchanged, while a statement naming $k$ is evaluated against the structure map and may change.

The effect of the passage on the objects the corpus builds is then read off object by object.

**Theorem (the four effects).** The realification acts on the standard objects as follows.

| object | over $\mathbb{C}$ | realification over $\mathbb{R}$ |
|---|---|---|
| the space $\mathbb{B}$ | complex dimension $4$ | real dimension $8$ |
| a $\mathbb{C}$-linear map | — | $\mathbb{R}$-linear, commuting with $J$ |
| a conjugate-linear map | no real-linear reading required | $\mathbb{R}$-linear, anticommuting with $J$; brought in by the passage |
| a symmetric bilinear form | rank only | two real forms, realified signature $(n,n)$ |
| a Hermitian form | complex inertia $(n,m)$ | one real form, signature $(2p,2q)$ |
| a $\mathbb{C}$-subspace | dimension $m$ | an $\mathbb{R}$-subspace of dimension $2m$; the odd-dimensional real subspaces are the ones the complex reading cannot produce |
| a subalgebra closed under the product | classified over $\mathbb{C}$ | more subalgebras, by the failure of the converse of "complex subspace is a real subspace" |
| an $\mathbb{R}$-algebra automorphism | the $\mathbb{C}$-linear ones | enlarged by the conjugate-linear coset, the Galois twist of $\mathbb{C}/\mathbb{R}$ |
| a left multiplication and its trace | $\operatorname{Tr}_{\mathbb{C}}(L_{\tilde Q_1})=4\,\mathrm{Sc}(\tilde Q_1)$ | $\operatorname{Tr}_{\mathbb{R}}(L_{\tilde Q_1})=8\,\mathrm{Re}\,\mathrm{Sc}(\tilde Q_1)$, twice the real part |
| the endomorphism ring | $M_n(\mathbb{C})$ | $M_{2n}(\mathbb{R})$; the $\mathbb{B}$-linear part is unchanged as a set |
| ideals, idempotents, zero divisors, nilpotents, units, the centre | — | **unchanged**, because $i\in\mathbb{B}$ |

*Proof.* The dimension is the doubling of the basis, and the two kinds of linear map are the two criteria of the previous sections. The two rows on forms are the two rules of the realification of a form. The subspace row is the even-dimension restriction of the complex reading, which the real reading does not inherit: a real subspace closed under the product need not be a complex subspace. The last row is the key case of the dictionary: an additive subgroup closed under left multiplication by every element of $\mathbb{B}$ is closed under multiplication by $i$ whenever $i$ lies in $\mathbb{B}$, so every ideal, and with it the idempotents and the zero divisors of a product, is automatically a complex subspace;

**Remark (what the four effects are not).** The four effects are not four independent losses. The first two are one doubling; the third is the appearance of the anticommuting maps; the fourth is the doubling of a degree-two invariant. What looks like a fifth effect, the growth of the automorphism group, is the same appearance of the conjugate-linear maps read on the group of the units.

## The Effect on the Twelve Algebraic Structures

**Theorem (the twelve over $\mathbb{R}$).** The twelve products of *The 12 Products of the Biquaternion Complex Space* are defined by the four general products on the complex space. Read over $\mathbb{R}$,

1. all twelve are $\mathbb{R}$-bilinear, so all twelve are algebras in the broad sense over $\mathbb{R}$;
2. the six of the $A$ family are $\mathbb{C}_{\mathbb{B}}$-linear in the second slot, and the six of the $S$ family are $\mathbb{C}_{\mathbb{B}}$-conjugate-linear in it;
3. no product of the $S$ family is a sesqualgebra over $\mathbb{R}$ with a nontrivial involution, and the count of sesqualgebras over $\mathbb{R}$ among the twelve is zero.

*Proof.* (1) A $\mathbb{C}$-bilinear or $\mathbb{C}$-sesquilinear product is additive in each argument and linear over $\mathbb{R}$ in each, so it is $\mathbb{R}$-bilinear. (2) The second slot of a general product is read through the identity or through the star ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, and ${}^{*}$ restricted to the centre is $i\mapsto-i$; on a central scalar $\lambda$ it acts as the conjugation. (3) A sesqualgebra over a field requires an involution of that field; the only automorphism of $\mathbb{R}$ is the identity, and a sesquilinear product with the identity involution is bilinear. The verification of (1) and (2) is by direct computation on the real basis, and it agrees with the "scalars" column of the table of the twelve, which reads $\mathbb{C}$ for the $A$ family and $(\mathbb{C},\bar{\cdot})$ for the $S$ family.

**Corollary (the counts, in the two senses of the word algebra).** The word *algebra* has two senses in the corpus, and the passage between the readings changes the two counts in opposite directions.

| sense | over $\mathbb{C}$ | over $\mathbb{R}$ |
|---|---|---|
| broad: a module with a bilinear multiplication | $6$ algebras and $6$ sesqualgebras | $12$ algebras and $0$ sesqualgebras |
| associative unital | $1$, the general plain algebra | $1$, the same |
| of the twelve structures, the number that are algebras | $6$ | $12$ |

*Proof.* The broad count is the theorem above and the definition of a sesqualgebra over $(\mathbb{C},\varsigma)$, whose two scalar rules are the two slots of the $S$ family. The associative unital count is that only the general plain product of the twelve is associative, by *Introduction to the Biquaternion Algebra*, §*Associativity*, and by the collapse theorem of *Sesqualgebras* for the sesquilinear family — the statement is about the ring and so is the same in the two readings.

**Theorem (the centre carries the distinction, and the products do not merge).** After the realification the six products of the $S$ family are no longer distinguished from the six of the $A$ family by the field $\mathbb{R}$; they are distinguished by the centre $\mathbb{C}_{\mathbb{B}}$, over which the first six are linear and the second six conjugate-linear. The distinction is an object of the reading and not of the product: the product, its table and every ring property are the same before and after.

*Proof.* The criteria of §*The Realification of a Linear Map* apply to the second slot, with $V=W=\mathbb{B}$ and with $\mathbb{C}_{\mathbb{B}}$ in place of $\mathbb{C}$. The last clause is the dictionary.

**Remark (the trap of the real part).** A computation of the twelve restricted to the real part of the space — the quaternionic elements $Q_te_t+\vec Q$, a real space of dimension four — sees ten operations and not twelve, because two pairs coincide there: the antisymmetric plain product with the antisymmetric quaternionic sesquilinear product, and the symmetric quaternionic product with the symmetric plain sesquilinear product. The corpus records the count of ten in the comment of *The 12 Products of the Biquaternion Complex Space*, with the caution that such a computation "can hide an obstruction or a structure that distinguishes the two members of a coincident pair". Twelve distinct operations require the full eight-dimensional real space, and the distinction of the twelve is a statement about the ring read on the whole space.

## What Is Specific to the Biquaternion Instance

Four things are specific to the real reading of $\mathbb{B}$.

**The odd real subalgebras.** Over $\mathbb{C}$ a subalgebra of $\mathbb{B}$ is a complex subspace, of even real dimension; over $\mathbb{R}$ there are subalgebras of every dimension up to eight. Among the coordinate subspaces of the real basis the closed spans have real dimensions $1,2,4,8$ with counts $1,7,7,1$, so no closed coordinate span has odd dimension above one — and a subalgebra of odd dimension nevertheless exists:

$$
\mathbb{R}\{e_t,\ \vec e_x+i\vec e_y,\ i\vec e_x-\vec e_y\},
$$

of real dimension three, whose two non-unit generators are orthogonal, of square zero and of vanishing product. Closure is a condition on a subspace, not on a coordinate span.

**The Galois-twisted automorphisms.** Every $\mathbb{R}$-linear automorphism of $\mathbb{B}$ restricts on the centre to an automorphism of $\mathbb{C}$ read over $\mathbb{R}$, and there is an exact sequence

$$
1\longrightarrow\operatorname{Aut}_{\mathbb{C}}(\mathbb{B})\longrightarrow\operatorname{Aut}_{\mathbb{R}}(\mathbb{B})\xrightarrow{\ \rho\ }\{\mathrm{id},\kappa\}\cong\mathbb{Z}/2,
$$

$\kappa(\lambda)=\bar\lambda$ being the Galois conjugation. The real automorphism group is therefore twice the complex one, the extra coset being conjugate-linear: it is the structure that fixes the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ pointwise and negates it on the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, represented by the coefficient conjugation $\bar{\cdot}$. The derivations do not grow, $\operatorname{Der}_{\mathbb{R}}(\mathbb{B})$ agreeing with $\operatorname{Der}_{\mathbb{C}}(\mathbb{B})$, and the reason is the centrality of $i$. The coset is the descent of *Real Forms and the Descent of an Algebra*.

**The trace form.** The **trace form** of the left regular representation,

$$
\tau(\tilde Q_1,\tilde Q_2)=\operatorname{Tr}_{\mathbb{R}}\bigl(L_{\tilde Q_1}L_{\tilde Q_2}\bigr)=8\,\operatorname{Re}\langle\tilde Q_1,\tilde Q_2\rangle,
$$

is a symmetric bilinear form of signature $(4,4)$ with zero radical, invariant under every automorphism of the algebra. Its normalisation carries the dimension ratio of the dictionary: the complex trace counts $\mathrm{Sc}$ with the factor $4$ and the real trace with the factor $8$, and $\tau$ is the real invariant form of the algebra, the reading of the general plain bilinear form in which the invariance is a one-line statement.

**The real models.** Over $\mathbb{C}$ the algebra is $M_2(\mathbb{C})$ acting on $\mathbb{C}^2$, the complex spinor module. Over $\mathbb{R}$ the same elements act on the realification $\mathbb{R}^4=\mathbb{C}^2_{\mathbb{R}}$ and on the left regular module $\mathbb{R}^8$, the two readings $M_2(\mathbb{C})$ and $\mathsf{M}_4^{L}$ of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* and *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*. The Clifford reading of the same ring, the even Clifford algebra of the Minkowski form of signature $(1,3)$, is a third real model; it is the subject of *Biquaternion Other Algebraic Element Representations* and is not developed here.

## Summary

The realification keeps the elements, the addition and the product, restricts the scalars to $\mathbb{R}$, and forgets the complex structure $J$; the pair $(V_{\mathbb{R}},J)$ is the complex space again, and nothing else is lost. A $\mathbb{C}$-linear map becomes an $\mathbb{R}$-linear map commuting with $J$, and the passage brings in the conjugate-linear maps, which are the $\mathbb{R}$-linear maps anticommuting with $J$ and have no $\mathbb{C}$-linear reading. A symmetric complex bilinear form realifies to the split signature $(n,n)$ and to a second real form, its imaginary part; a Hermitian form realifies to one real form of doubled inertia. The dimension doubles, the subobjects change shape, the automorphism group grows by the conjugate-linear coset, and the ideals, the idempotents, the zero divisors and every other object read from the ring alone do not move at all.

Read on the twelve algebraic structures, the passage turns the six $\mathbb{C}$-bilinear products and the six $\mathbb{C}$-sesquilinear ones into twelve $\mathbb{R}$-bilinear products; the sesqualgebra structure disappears with the nontrivial involution of the base field, and the distinction survives as linearity against conjugate-linearity over the centre $\mathbb{C}_{\mathbb{B}}$.

Four things are specific to the biquaternion instance and are collected at the end. A three-dimensional real subalgebra exists, $\mathbb{R}\{e_t,\vec e_x+i\vec e_y,i\vec e_x-\vec e_y\}$, although no closed coordinate span has odd dimension above one. The real automorphism group is the complex one doubled by the conjugate-linear Galois coset, and the coset is represented by the coefficient conjugation, which fixes $\mathbb{H}_{\mathbb{B}}$ pointwise and negates it on $i\mathbb{H}_{\mathbb{B}}$; the derivations do not grow. The trace form $\tau(\tilde Q_1,\tilde Q_2)=\operatorname{Tr}_{\mathbb{R}}(L_{\tilde Q_1}L_{\tilde Q_2})=8\operatorname{Re}\langle\tilde Q_1,\tilde Q_2\rangle$ is a symmetric bilinear form of signature $(4,4)$, of zero radical, invariant under every automorphism. The real models are the complex spinor one, the regular one $\mathsf{M}_4^{L}$ on $\mathbb{R}^8$, and the even Clifford algebra of the Minkowski form of signature $(1,3)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V_{\mathbb{R}}=\operatorname{Res}_{\mathbb{C}/\mathbb{R}}V$ | the realification of a complex vector space, of doubled real dimension |
| $J$ | the complex structure, the $\mathbb{R}$-linear multiplication by $i$, with $J^2=-\mathrm{id}$ |
| $T J=J T$ | the criterion for $\mathbb{C}$-linearity of an $\mathbb{R}$-linear map |
| $S J=-J S$ | the criterion for conjugate-linearity |
| $\operatorname{Ant}_{\mathbb{C}}(V)$ | the conjugate-linear endomorphisms, the anticommuting part of $\operatorname{End}_{\mathbb{R}}(V_{\mathbb{R}})$ |
| $\Phi_{\mathbb{R}}=\operatorname{Re}\Phi$ | the realification of a form |
| $(n,n)$ | the realified signature of a nondegenerate symmetric complex bilinear form |
| $(2p,2q)$ | the realified signature of a Hermitian form of complex inertia $(n,m)$ |
| $\mathbb{C}\otimes_{\mathbb{R}}V_{\mathbb{R}}\cong V\oplus\bar V$ | the complexification of the realification, which is not $V$ |
| $A$ family / $S$ family | the six products linear, and the six conjugate-linear, over the centre $\mathbb{C}_{\mathbb{B}}$ |
| $\tau(\tilde Q_1,\tilde Q_2)=\operatorname{Tr}_{\mathbb{R}}(L_{\tilde Q_1}L_{\tilde Q_2})=8\operatorname{Re}\langle\tilde Q_1,\tilde Q_2\rangle$ | the trace form of the left regular representation, symmetric bilinear of signature $(4,4)$, zero radical, invariant under every automorphism |
| $\rho:\operatorname{Aut}_{\mathbb{R}}(\mathbb{B})\to\{\mathrm{id},\kappa\}\cong\mathbb{Z}/2$ | the Galois twist of the automorphism group; the real group is twice the complex one, the extra coset conjugate-linear, represented by the coefficient conjugation |
| $\mathbb{R}\{e_t,\vec e_x+i\vec e_y,i\vec e_x-\vec e_y\}$ | the three-dimensional real subalgebra, its two non-unit generators orthogonal, of square zero and of vanishing product |

## Further Reading

- **The Realification of the Eight Derived Structures** (`articles_maths/the-realification-of-the-eight-derived-structures.md`), for the general case applied to the four forms of the corpus, the four Gram matrices, the four signatures, the restrictions to the remarkable subspaces and the realified null cones.
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`) and *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-algebraic-structures-over-the-biquaternion-c-space.md`), for the twelve products, their table and their two-slot construction, on which §*The Effect on the Twelve Algebraic Structures* rests.
- *Change of Rings* (`articles_maths/change-of-rings.md`), *Extension of Scalars* (`articles_maths/extension-of-scalars.md`) and *Real Forms and the Descent of an Algebra* (`articles_maths/real-forms-and-the-descent-of-an-algebra.md`), for the general theory of the restriction and the extension of scalars and of the real forms.
