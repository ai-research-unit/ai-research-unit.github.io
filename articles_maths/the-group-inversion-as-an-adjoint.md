
# __The Group Inversion as an Adjoint__

## Introduction

The inversion of a group is its canonical involution, and on the group algebra it is the operator that reverses the order of a product. With respect to the natural pairing of the category it is self-adjoint, and it is exactly the operator that turns the left regular representation into the right one: the adjoint of the left multiplication by $a$ is the left multiplication by $a^{-1}$, and the parameter that appears is the inverted one. This article identifies the inversion with the adjoint operation on the indices of the translations, records the unit and the counit of the group algebra and the identities they satisfy with the inversion, and fixes the identification of the inversion with the involution of the group algebra. It is the second article of the `* Operator Theory` group; the pairing and the adjoint are from *Involutions on the Operator Layer*, the translations and the sandwich from *Left and Right Multiplication in a Group* and *The Signed Sandwich on a Group*, and the coalgebra structure named here is developed in a later category.

Throughout, $k[G]$ is the group algebra with basis $G$, $\Sigma_{\iota}$ is the linear extension of the inversion, $L_a,R_b$ are the translations, and the pairing and adjoint are those fixed in *Involutions on the Operator Layer*.

## The Inversion and the Translations

**Theorem (the inversion is the adjoint index).** For every $a,b\in G$,

$$
(L_a)^{*}=L_{a^{-1}}=L_{\iota(a)}, \qquad (R_b)^{*}=R_{b^{-1}}=R_{\iota(b)},
$$

and for a two-sided translation $(L_aR_b)^{*}=L_{a^{-1}}R_{b^{-1}}$.

**Proof.** The two translation formulas are proved in *Involutions on the Operator Layer*, from the orthonormality of the basis. For the two-sided operator, $(L_aR_b)^{*}=(R_b)^{*}(L_a)^{*}=R_{b^{-1}}L_{a^{-1}}=L_{a^{-1}}R_{b^{-1}}$, using that the two families commute.

**Corollary (the adjoint operation on the index).** The assignment $T\mapsto T^{*}$ on the translations is the inversion of the parameter: the adjoint of the left regular representation is the left regular representation of the inverted element, and the map $a\mapsto L_a$ intertwines the inversion with the adjoint.

**Proof.** That $(L_a)^{*}=L_{a^{-1}}=L_{\iota(a)}$ is the theorem. The intertwining is the equation $L_{\iota(a)}=L_a^{*}$, read as the commuting square of the isomorphism $a\mapsto L_a$ with the inversion on $G$ and the adjoint on $L(G)$.

**Proposition (the sandwich and the inversion).** For the unsigned sandwich $\Sigma_{a,b}(x)=axb$ one has $\Sigma_{a,b}^{*}=\Sigma_{a^{-1},b^{-1}}$; hence the sandwich is unitary for every pair $(a,b)$ and it is self-adjoint exactly when $a^{2}=b^{2}=e$.

**Proof.** Solving $\Sigma_{a,b}(x)=y$ gives $x=a^{-1}yb^{-1}$, so the matrix of $\Sigma_{a,b}$ is carried to that of $\Sigma_{a^{-1},b^{-1}}$ by transposition. The sandwich is invertible with inverse $\Sigma_{a^{-1},b^{-1}}$, which is its adjoint, hence unitary; it is self-adjoint exactly when $a=a^{-1}$ and $b=b^{-1}$.

**Remark (the inversion as the adjoint of the left multiplication).** The phrase of the title is the theorem in its exact form: the adjoint of the left multiplication by $a$ is the left multiplication by the inverse of $a$, so that the inversion is the operation the adjoint performs on the index of the translation. When the group is abelian and the parameters are identified with their translations, the adjoint is inversion itself on the operator's index.

## The Unit and the Counit

**Definition.** The **counit** is the $k$-linear map $\varepsilon:k[G]\to k$ with $\varepsilon(g)=1$ for every $g$, the augmentation; the **unit** is the $k$-linear map $u:k\to k[G]$ with $u(1)=e$; the **comultiplication** is the $k$-linear map $\Delta:k[G]\to k[G]\otimes_k k[G]$ with $\Delta(g)=g\otimes g$; and the **inversion** is the linear extension $\Sigma_{\iota}$.

**Proposition (the counit, the unit and the pairing with the identity).** The counit is the augmentation, $\varepsilon(x)=\sum_g x_g$; the pairing with the basis dual $\delta_e$ is the coefficient at the identity, $\langle\delta_e,x\rangle=x_e$; the two agree on the basis, where both take the value $1$, and differ on a general $x$ exactly when $\sum_g x_g\neq x_e$. The unit places the identity, $u(1)=e$.

**Proof.** $\langle\delta_e,x\rangle=\sum_g\delta_e(g)x_g=x_e$ and $\varepsilon(x)=\sum_g x_g$ from $\varepsilon(g)=1$; on a basis element both give $1$. The unit is $u(1)=e$ by definition, and it is the $k$-linear map right inverse to $\varepsilon$ on the identity.

**Theorem (the identities of the inversion, the unit and the counit).** In $k[G]$,

$$
(\varepsilon\otimes\mathrm{id})\Delta=\mathrm{id}=(\mathrm{id}\otimes\varepsilon)\Delta,
\qquad
m(\mathrm{id}\otimes\Sigma_{\iota})\Delta=u\varepsilon=m(\Sigma_{\iota}\otimes\mathrm{id})\Delta,
$$

where $m$ is the multiplication of $k[G]$. The first two say that the counit is the identity for the comultiplication; the last two say that the inversion is the inverse for the multiplication in the sense of the comultiplication.

**Proof.** On a basis element $g$: $(\varepsilon\otimes\mathrm{id})\Delta(g)=1\otimes g=g$ and $(\mathrm{id}\otimes\varepsilon)\Delta(g)=g\otimes1=g$ after the identification of $k\otimes_k k[G]$ with $k[G]$. And $m(\mathrm{id}\otimes\Sigma_{\iota})\Delta(g)=m(g\otimes g^{-1})=gg^{-1}=e=u\varepsilon(g)$, with the other order $m(\Sigma_{\iota}\otimes\mathrm{id})\Delta(g)=g^{-1}g=e$. So the inversion is the operator that inverts each basis element in the multiplication.

**Corollary (the inversion is characterised by the identities).** The inversion $\Sigma_{\iota}$ is the unique $k$-linear automorphism of $k[G]$ with $\Sigma_{\iota}(g)=g^{-1}$ for every $g$, and it is the unique map making the identities hold.

**Proof.** Uniqueness is linearity and the values on the basis, which determine the map; and it is an anti-automorphism of order two, so it is an automorphism exactly when $G$ is abelian.

## The Identification with the Involution of the Group Algebra

**Proposition (the extensions of the group involutions).** Every involution $\sigma$ of $G$ extends to a $k$-linear anti-automorphism $\Sigma_{\sigma}$ of $k[G]$ of order two, and $\Sigma_{\sigma}$ is an involution of the group algebra in the sense of *Involutive Rings*. The inversion is the instance $\sigma=\iota$, and $\Sigma_{\iota}$ is the antipode.

**Proof.** The linear extension of an anti-automorphism is an anti-automorphism, and the extension of an involution is an involution because $\Sigma_{\sigma}^{2}=\Sigma_{\sigma^{2}}=\mathrm{id}$. The identification with *Involutive Rings* is that a $k$-algebra anti-automorphism of order two is exactly an involution of the algebra.

**Proposition (the commutation of the two operations).** The adjoint and the extension of a group involution commute: $\Sigma_{\sigma}^{*}=\Sigma_{\sigma}$ for every involution $\sigma$, and $(L_a\Sigma_{\sigma})^{*}=\Sigma_{\sigma}L_{a^{-1}}$.

**Proof.** For $\sigma=\iota$ this is self-adjointness of the inversion, from *Involutions on the Operator Layer*; for a general involution the same computation applies, since the matrix of $\Sigma_{\sigma}$ in the basis $G$ is symmetric: $\langle\Sigma_{\sigma}g,h\rangle=\delta_{\sigma(g),h}=\delta_{g,\sigma(h)}=\langle g,\Sigma_{\sigma}h\rangle$, using $\sigma^{2}=\mathrm{id}$. Then $(L_a\Sigma_{\sigma})^{*}=\Sigma_{\sigma}^{*}L_a^{*}=\Sigma_{\sigma}L_{a^{-1}}$.

**Remark (two structures, not one).** The group involution $\sigma$ on the elements and the adjoint on the operators are two structures. They are related by the proposition, which says that the extension of $\sigma$ is self-adjoint, but they are not the same structure: the adjoint is an anti-involution of the operator algebra, whereas the extension of $\sigma$ is an anti-involution of the group algebra, and the two act on different objects. The agreement for the inversion is the content of this article and is proved by the pairing, never assumed.

## Summary

The inversion of $G$ is the canonical involution, and on the operator layer it is the adjoint operation on the indices of the translations: $(L_a)^{*}=L_{a^{-1}}=L_{\iota(a)}$, $(R_b)^{*}=R_{b^{-1}}$, and the two-sided sandwich is unitary with $\Sigma_{a,b}^{*}=\Sigma_{a^{-1},b^{-1}}$. The adjoint of the left regular representation is the left regular representation of the inverted element, so the map $a\mapsto L_a$ intertwines the inversion with the adjoint.

On the group algebra the inversion is the antipode: with the unit $u(1)=e$, the counit $\varepsilon$ the augmentation and the comultiplication $\Delta(g)=g\otimes g$, the identities $(\varepsilon\otimes\mathrm{id})\Delta=\mathrm{id}=(\mathrm{id}\otimes\varepsilon)\Delta$ and $m(\mathrm{id}\otimes\Sigma_{\iota})\Delta=u\varepsilon=m(\Sigma_{\iota}\otimes\mathrm{id})\Delta$ hold, and $\Sigma_{\iota}$ is the unique $k$-linear map with $\Sigma_{\iota}(g)=g^{-1}$ for every $g$. The counit is the augmentation $\varepsilon(x)=\sum_g x_g$, whereas the pairing with $\delta_e$ reads the coefficient at the identity, the two agreeing on the basis and differing in general. Every group involution $\sigma$ extends to an involution $\Sigma_{\sigma}$ of the group algebra, and each such extension is self-adjoint, so the adjoint commutes with the extension; but the involution on the elements and the adjoint on the operators remain two structures, and their agreement is proved and not assumed.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(L_a)^{*}=L_{a^{-1}}$, $(R_b)^{*}=R_{b^{-1}}$ | the adjoint inverts the parameter |
| $\Sigma_{a,b}^{*}=\Sigma_{a^{-1},b^{-1}}$ | the sandwich is unitary |
| $u(1)=e$ | the unit of the group algebra |
| $\varepsilon(g)=1$ | the counit, the augmentation |
| $\Delta(g)=g\otimes g$ | the comultiplication |
| $\Sigma_{\iota}$, the antipode | the linear extension of the inversion |
| $m(\mathrm{id}\otimes\Sigma_{\iota})\Delta=u\varepsilon$ | the antipode identity |
| $\Sigma_{\sigma}^{*}=\Sigma_{\sigma}$ | every extended involution is self-adjoint |

## Further Reading

- Marshall Hall, *The Theory of Groups* (Macmillan, 1959), for the group algebra, the regular representation and the antipode.
- Donald S. Passman, *The Algebraic Structure of Group Rings* (Wiley, 1977), for the group algebra, its augmentation, its comultiplication and its antipode.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the involution of an algebra and the adjoint under a form.
- Christian Kassel, *Quantum Groups* (Springer, Graduate Texts in Mathematics 155, 1995), for the coalgebra and Hopf structure of the group algebra, used here only as a forward reference.
