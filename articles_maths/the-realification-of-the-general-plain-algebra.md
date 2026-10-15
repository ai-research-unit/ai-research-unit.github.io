# __The Realification of the General Plain Algebra__

## Introduction

The general plain algebra is the structure carried by the general plain bilinear product
$$
\tilde P\circ\tilde Q=\tilde P\tilde Q,
$$
the one product of *The 12 Products of the Biquaternion Complex Space* that makes $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ an associative unital algebra, over $\mathbb{C}$ and over $\mathbb{R}$. This article is the real reading of that algebra. It states what the change of scalars from $\mathbb{C}$ to $\mathbb{R}$ does to the algebra as a whole, and it isolates the four things that exist in the real reading and have no complex counterpart.

The general construction is not repeated here: the realification of a vector space, of a linear map and of a form, the two rules for forms and the table of the four effects are *The Realification and the Effect of the Change of Scalars*. This article applies that construction to the general plain algebra and states its outcome.

## The Change of Scalars

$\mathbb{B}$ is the complex vector space of dimension four on the basis $e_0,e_1,e_2,e_3$, with $e_1e_2=e_3$, and the field of scalars is read in the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$. Read over $\mathbb{R}$ the same set is the real vector space
$$
\mathbb{R}^8=\operatorname{span}_\mathbb{R}\{e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3\},
$$
and the product is the same multiplication table on the same elements. **Restriction of scalars** takes the $\mathbb{C}$-algebra to an $\mathbb{R}$-algebra; there is no new multiplication, only a smaller field. The complex structure is the operator
$$
J:\tilde Y\mapsto i\tilde Y,\qquad J^2=-\mathrm{id},
$$
an $\mathbb{R}$-linear endomorphism of $\mathbb{R}^8$, and $\mathbb{C}$-linear: it commutes with itself, $J(i\tilde Y)=i\,J\tilde Y$, by the criterion $TJ=JT$, the scalar $i$ being central. Multiplication by $i$ is left multiplication by the central element $i\in\mathbb{C}_{\mathbb{B}}$, so $J=L_i$ in the notation below.

Every property written with the addition, the product, the unit $e_0$ and quantification over the elements is a statement about the **ring** and does not move when the scalars are restricted to $\mathbb{R}$: associativity, the two-sided unit, the ideal lattice, the idempotents, the nilpotents, the zero divisors and the group of units are the same in the two readings. This is the content of the remark that the ideals, the idempotents and the zero divisors do not change. What does move is every notion that names the field: $\mathbb{B}$ is **central simple over $\mathbb{C}$** and **simple but not central over $\mathbb{R}$**, because the centre $\mathbb{C}_{\mathbb{B}}$ is a field strictly larger than $\mathbb{R}e_0$.

## The Realification of the Form and of the Product

The product carries the general plain bilinear form $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)$. Over $\mathbb{C}$ a nondegenerate symmetric bilinear form is classified by its rank alone, so it has no inertia to double; its realification is instead the **split** pair $(\operatorname{Re}B,\operatorname{Im}B)$, and on $\mathbb{R}^8$ the form has signature
$$
(4,4),\qquad \text{Gram matrix } \operatorname{diag}(1,-1,-1,-1,-1,1,1,1),
$$
with $B_{\mathbb{R}}(JP,JQ)=-B_{\mathbb{R}}(P,Q)$: the complex structure **reverses** a bilinear form. The other three general products carry the forms $N$, $H$, $K$, whose realifications are $(4,4)$, $(8,0)$ and $(2,6)$ respectively; the Hermitian ones double their complex inertia and are **preserved** by $J$. The four Gram matrices are the blocks $\mathrm{D}$ and $\pm\mathrm{D}$ of the diagonal above.

The four conjugations of the algebra — the natural ${}^{\natural}$, the complex bar, the Hermitian star ${}^{*}$ and the anti-Hermitian ${}^{\flat}$ — are $\mathbb{C}$-antilinear and therefore $\mathbb{R}$-linear: they commute with the real scalars, and each is an $\mathbb{R}$-linear endomorphism of $\mathbb{R}^8$. Their $\mathbb{C}$-antilinearity is antilinearity with respect to $J$, and it is read inside the real algebra as the relation $\varsigma J=-J\varsigma$. In the real basis a $\mathbb{C}$-linear endomorphism has the block shape $\left(\begin{smallmatrix}A&-B\\ B&A\end{smallmatrix}\right)$ and commutes with $J$, while a $\mathbb{C}$-antilinear one has the shape $\left(\begin{smallmatrix}A&B\\ B&-A\end{smallmatrix}\right)$ and anticommutes with it.

## The Effect on the Twelve Structures

The twelve structures are the six $A$ structures (bilinear in both slots, called algebras over $\mathbb{C}$) and the six $S$ structures (sesquilinear in the second slot, called sesqualgebras over $\mathbb{C}$). The passage to $\mathbb{R}$ acts on them **uniformly** and changes no product rule:

- an $A$ structure keeps its second slot $\mathbb{C}_{\mathbb{B}}$-linear and remains an algebra, now over $\mathbb{R}$;
- an $S$ structure had its second slot $\mathbb{C}_{\mathbb{B}}$-conjugate-linear, and over $\mathbb{R}$ the involution disappears, since the only automorphism of $\mathbb{R}$ is the identity: a sesquilinear law with the identity involution **is** a bilinear law. The structure is therefore an $\mathbb{R}$-**algebra** as well, and the $A$/$S$ distinction migrates from the field to the centre, where it is the relation $LJ=\pm JL$ of the left multiplications by central elements.

Every product law is a polynomial identity with integer coefficients in the structure constants, so it is visible over the prime field and does not change: the failures of associativity, of the Jacobi identity and of the Jordan identity found over $\mathbb{C}$ are exactly the failures over $\mathbb{R}$, on the same witnesses.

## What Is Specific to the Real Interpretation

Four things are specific to the real reading.

**The real subalgebras.** A subalgebra of the complex reading is a complex subspace, of even real dimension. Over $\mathbb{R}$ there are subalgebras of every dimension at most eight. Among the coordinate subspaces the closed spans have dimensions $1,2,4,8$ with counts $1,7,7,1$, so there is no closed coordinate span of odd dimension above one; a subalgebra of odd dimension nevertheless exists, for instance
$$
\mathbb{R}\{e_0,\ e_1+ie_2,\ ie_1-e_2\},
$$
of dimension three, whose two non-unit generators are orthogonal and of square zero with vanishing product. Closure is a condition on a subspace, not on a coordinate span.

**The Galois-twisted automorphisms.** Every $\mathbb{R}$-linear automorphism of $\mathbb{B}$ restricts on the centre to an automorphism of $\mathbb{C}$ read over $\mathbb{R}$, and there is an exact sequence
$$
1\longrightarrow \operatorname{Aut}_{\mathbb{C}}(\mathbb{B})\longrightarrow \operatorname{Aut}_{\mathbb{R}}(\mathbb{B})\xrightarrow{\ \rho\ }\{\mathrm{id},\kappa\}\cong\mathbb{Z}/2,
$$
where $\kappa(\lambda)=\bar\lambda$ is the Galois conjugation. The real automorphism group is therefore **twice** the complex one, the extra coset being conjugate-linear; the derivations do not grow, $\operatorname{Der}_{\mathbb{R}}(\mathbb{B})$ agreeing with $\operatorname{Der}_{\mathbb{C}}(\mathbb{B})$, and the reason lies in the centrality of $i$.

**The trace form.** The trace form of the regular representation,
$$
\tau(\tilde P,\tilde Q)=\operatorname{Tr}\bigl(L_{\tilde P}L_{\tilde Q}\bigr)=8\,\operatorname{Re}B(\tilde P,\tilde Q),
$$
is a symmetric bilinear form of signature $(4,4)$ with zero radical, invariant under every automorphism. Its normalisation carries the dimension ratio: the complex trace counts $\mathrm{Sc}(\tilde X)$ with the factor $4$ and the real trace with the factor $8$, and $\tau$ is the real invariant form of the algebra.

**The real models.** Over $\mathbb{C}$ the algebra is $M_2(\mathbb{C})$ acting on $\mathbb{C}^2$. Over $\mathbb{R}$ the same elements act on the realification $\mathbb{R}^4=\mathbb{C}^2_{\mathbb{R}}$, and on the left regular module $\mathbb{R}^8$, giving the readings $M_2(\mathbb{C})$ and $M_4(\mathbb{C})_L$. The Clifford reading of the same ring, the even Clifford algebra of the Minkowski form of signature $(1,3)$, is a third real model; it is the subject of *Biquaternion Other Algebraic Element Representations* and is not developed here.

## Summary

Read over $\mathbb{R}$ the general plain algebra is the same associative unital product on the same elements, a simple $\mathbb{R}$-algebra on $\mathbb{R}^8$ with centre $\mathbb{C}_{\mathbb{B}}$; its second slot stays $\mathbb{C}_{\mathbb{B}}$-linear, its form $B$ realifies to signature $(4,4)$, and every ring-theoretic property is unchanged. The four conjugations are all $\mathbb{R}$-linear, the six sesquilinear structures become $\mathbb{R}$-algebras because $\mathbb{R}$ carries no involution, and the $A$/$S$ distinction is read in the centre. Four things are specific to the real reading: the odd-dimensional subalgebras, the Galois-twisted automorphism group, the trace form $8\operatorname{Re}B$, and the real models $M_2(\mathbb{C})$ and $M_4(\mathbb{C})_L$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{R}^8$ | the realification of $\mathbb{B}$, basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ |
| $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre, of complex dimension $1$ and real dimension $2$ |
| $J=L_i$ | multiplication by $i$, of square $-1$, the complex structure |
| $\varsigma$ | a conjugation, $\mathbb{C}$-antilinear and hence $\mathbb{R}$-linear |
| $B$, $(4,4)$ | the general plain bilinear form and the signature of its realification |
| $\rho:\operatorname{Aut}_{\mathbb{R}}(\mathbb{B})\to\{\mathrm{id},\kappa\}$ | the restriction to the centre, kernel $\operatorname{Aut}_{\mathbb{C}}(\mathbb{B})$ |
| $\tau(\tilde P,\tilde Q)=\operatorname{Tr}(L_{\tilde P}L_{\tilde Q})$ | the trace form, $=8\operatorname{Re}B$, signature $(4,4)$ |

## Further Reading

- *The Realification and the Effect of the Change of Scalars* (`articles_maths/the-realification-and-the-effect-of-the-change-of-scalars.md`), for the general construction, the two rules of the realification of a form, the table of the four effects and the change of scalars from $\mathbb{C}$ to $\mathbb{R}$.
- *Biquaternion Other Algebraic Element Representations* (`articles_maths/biquaternion-other-algebraic-element-representations.md`), for the Clifford reading $\mathbb{B}\cong\mathrm{Cl}^+_{1,3}(\mathbb{R})$, which is a real model of the same ring and is owned there.
- *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-algebraic-structures-over-the-biquaternion-c-space.md`) and *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternion-c-space.md`), for the twelve structures and the four forms of which this article is the real reading.
- *The Specificities of the General Plain Algebra* (`articles_maths/the-specificities-of-the-general-plain-algebra.md`), for the left alternativity that isolates the general plain product among the twelve, a criterion that holds in the two readings.
