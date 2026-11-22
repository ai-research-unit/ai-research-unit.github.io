# __The Fierz–Kofink Identities and the Classification of Spinors__

## Introduction

**The subject.** A spinor of the operators, paired with the sixteen operators of a basis, produces sixteen numbers. The article proves that the sixteen are not free: they satisfy a system of quadratic relations, the Fierz–Kofink identities, which say that the tuple of numbers is the coefficient tuple of an operator of rank one. It then classifies the operators by the dimension of the ideal they generate and by the multiplicity pattern of their spectrum, and identifies the two lists with the algebraic types.

**The order of the article.** *The Sixteen Bilinears* defines the numbers and the aggregate. *The Identities* proves the relations and reads them as the rank-one condition. *The Five Classes* states the classification by spectral partition and identifies the classes. *Constancy along the Orbit* proves invariance under the group. *The Reading of the Classes* relates the answer to the row of the elements.

**It assumes** *Spinors and Dirac Spinors*, *The Spin-$\tfrac32$ Bispinors and the Minimal Left Ideals* and *The Symmetric and Antisymmetric Parts of the Operator Space*. **The row of the elements is** where the corresponding classification is the list of four real forms of a biquaternion.

**The result in one line.** The sixteen bilinears of a spinor satisfy $Z^2=qZ$ with $Z$ the aggregate and $q$ the norm, and the operators fall into five classes, of dimensions $0,4,8,12,16$ of generated ideal.

**Boundaries.** The rank and the spectrum of a single operator are *The Spin-$\tfrac32$ Bispinors and the Rank Strata* and *The Spin-$\tfrac32$ Bispinors and the Spectral Strata*; the bilinears of the row of the elements are *The Fierz–Kofink Identities and the Classification of Spinors*.

Nothing below is a statement of physics. The units are $e_t,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_k^2=-e_t$; the module of the operators is $V_{3/2}=\operatorname{Sym}^3 S$ of complex dimension four; a spinor is an element of a minimal left ideal $I$ of $\operatorname{End}(\mathbb{B})$; $\langle S,T\rangle=\operatorname{tr}(S^{\star}T)$ is the trace form; and $\operatorname{tr}$ and $\det$ are the trace and the determinant of an operator, read from its spectrum on the algebra.

## The Sixteen Bilinears

**Definition.** Fix a basis $E_1,\dots,E_{16}$ of the operator space, self-adjoint for the trace form. For a spinor $\psi$ the **bilinear covariants** are the sixteen numbers

$$
\beta_i(\psi)=\langle\psi,E_i\psi\rangle,\qquad i=1,\dots,16,
$$

and the **aggregate** is the operator $Z(\psi)=\sum_i\beta_i(\psi)E^i$, where $E^i$ is the dual basis for the trace form.

**Proposition.** The aggregate is the operator of rank one $Z(\psi)\eta=\psi\,\langle\psi,\eta\rangle$. Its image is the line of $\psi$, its square is $qZ$ with $q=\langle\psi,\psi\rangle$, and the sixteen bilinears are its coefficients.

*Proof.* The right side is linear in $\eta$ and its value is a multiple of $\psi$, so its image is the line of $\psi$ and it is of rank one. Composing it with itself multiplies the scalar by $\langle\psi,\psi\rangle$, which is $q$. The coefficients of the operator in the dual basis are the values $\langle\psi,E_i\psi\rangle$ by the definition of the dual basis.

**Corollary.** The sixteen bilinears are the coefficients of an operator of rank one, so they number sixteen but describe a spinor of four coordinates and a phase.

*Proof.* A rank-one operator is determined by its line and a functional, which is $3+3=6$ projective parameters against the $16-1=15$ of a general operator.

**The reading.** Completeness is the statement that the sixteen operators are a basis and that the pairing with a fixed spinor reads every one of them. It is the operator-space form of the completeness of a basis of bilinears.

## The Identities

**Theorem (Fierz–Kofink).** For every spinor $\psi$ the sixteen bilinears satisfy

$$
\sum_{ij}\beta_i\beta_j\,E^iE^j=q\sum_i\beta_iE^i,
$$

and equivalently the quadratic relations $\beta_i\beta_j=\sum_k c_{ij}^{\,k}\beta_k$ with the structure constants of the operator algebra in the basis.

*Proof.* The first display is the square of the aggregate, which the previous Proposition computes as $qZ$. Expanding $Z^2$ in the basis gives the second form, with $c_{ij}^{\,k}$ the coefficient of $E^k$ in $E_iE_j$. Both displays are the same identity read on the operator and on its coefficients.

**Corollary.** The identities are the statement that the sixteen products of the basis close on themselves: the product of two members of the basis is a combination of members of the basis, and the aggregate inherits the closure.

*Proof.* $E_iE_j=\sum_kc_{ij}^{\,k}E_k$ is the closure, and substituting it into $Z^2$ gives the relations among the bilinears.

**The reading.** An identity of Fierz–Kofink type is not an accident of a particular frame. It is the associativity of the operator algebra, written in the basis of the bilinears, and it holds for every spinor and every basis.

## The Five Classes

**Definition.** The **class** of an element $T$ of the operator space is the dimension of the left ideal $\operatorname{End}(\mathbb{B})T$ that $T$ generates on the left.

**Theorem.** The class takes the five values $0,4,8,12,16$, and the value is four times the rank of $T$.

$$
\operatorname{class}(T)=4\operatorname{rank}(T),\qquad \operatorname{class}\in\{0,4,8,12,16\}.
$$

*Proof.* The left ideal generated by $T$ is the image of the map $S\mapsto ST$, which consists of the operators vanishing on the kernel of $T$ and therefore has dimension $4\operatorname{rank}T$. The rank of an operator on a four-dimensional space is one of $0,1,2,3,4$.

**Corollary.** The five classes are the five ranks, the class $0$ is the single operator zero, and the class $16$ is the open set of invertible operators.

*Proof.* The rank is zero only at the zero operator, and it is four exactly on the invertible operators, which form an open set.

**Theorem (the finer list).** The spectral partitions are the five partitions of four, with the orbit dimensions

$$
(4):\ 0,\qquad (3,1):\ 6,\qquad (2,2):\ 8,\qquad (2,1,1):\ 10,\qquad (1,1,1,1):\ 12,
$$

and they refine the classes at the two ends only.

*Proof.* The dimension of the orbit of a semisimple operator is sixteen minus the dimension of its centraliser: $16-16=0$ for the scalar, $16-10=6$ for the pattern $(3,1)$, $16-8=8$ for $(2,2)$, $16-6=10$ for $(2,1,1)$ and $16-4=12$ for four distinct eigenvalues. The class $0$ is the zero operator, whose partition is $(4)$ at the eigenvalue zero; the class $16$ contains the partition $(1,1,1,1)$ as its open part and the other partitions as the loci of coincidences.

**The reading.** Two fivefold lists occur and they are not the same list. The first counts the dimension of the ideal an operator generates, which is its rank multiplied by four; the second counts the multiplicity pattern of its spectrum. The algebraic types named in the menu distribute over both: the scalar is the partition $(4)$ of full rank, the nilpotent is the partition $(4)$ of rank at most three, the semisimple types are the partitions with distinct values, and the rank-deficient ones are the classes below sixteen.

## Constancy along the Orbit

**Proposition.** The spectral partition is invariant under conjugation by every invertible operator, hence under the copy, so each class is a union of orbits. For the semisimple classes the orbit is exactly the class.

*Proof.* Conjugation preserves the spectrum with multiplicity, so the partition cannot change along an orbit. Conversely two semisimple operators with the same spectrum are conjugate, since each is conjugate to its diagonal form; the diagonal forms with one multiplicity pattern are conjugate to one another.

**Corollary.** A spinor has a type, the type of the operator its bilinears build, and the type is constant on the orbit of the spinor under the group.

*Proof.* The aggregate is built from the spinor by a formula invariant under the group, so the group carries the aggregate of $\psi$ to the aggregate of $g\psi$, and the two are conjugate.

**The reading.** The classification is the orbit classification under another name, and the invariants that separate the classes are the coefficients of the characteristic polynomial together with the pattern of coincidences among them.

## The Reading of the Classes

**Proposition.** At the row of the elements a spinor is classified by the four real forms of a biquaternion, and at the row of the operators by the five spectral partitions. The two lists are indexed by different data: the first by the orbit of the conjugation of the algebra, the second by the multiplicity pattern of the four eigenvalues.

*Proof.* The real forms are the orbits of the conjugation on the four-dimensional algebra, a list of four. The spectral partitions are the coincidence patterns of four eigenvalues, a list of five. A form does not determine a partition, since a biquaternion of one real form has either two distinct eigenvalues or one repeated, and both patterns occur inside a single form.

**Corollary.** The two classifications are not one list in two notations, and the operator row has the strictly larger list.

*Proof.* Four and five are different counts, and the map from the second list to the first is not injective.

**The reading.** The identities are the statement that the sixteen products close, and the classification is the statement that the closure has five shapes. Neither statement needs a basis, and neither needs an array: the aggregate is an operator of rank one and the class is its multiplicity pattern.

## Further Reading

- [Spinors and Dirac Spinors](spinors-and-dirac-spinors.html), for the spinor, the Dirac spinor and the chirality operator
- [The Fierz–Kofink Identities and the Classification of Spinors](the-fierz-kofink-identities-and-the-classification-of-spinors.html), for the bilinears of the row of the elements and the four real forms
- [The Spin-$\tfrac32$ Bispinors and the Spectral Strata](the-spin-three-halves-bispinors-and-the-spectral-strata.html), for the stratum of a single spinor in detail
- [The Symmetric and Antisymmetric Parts of the Operator Space](the-symmetric-and-antisymmetric-parts-of-the-biquaternion-operator-space.html), for the trace form and the two squares
- [The Spectrum of a Biquaternion](the-spectrum-of-a-biquaternion.html), for the reading of a spectrum from the coefficients of an element
